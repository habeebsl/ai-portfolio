<script setup>
import { onMounted, watchEffect, ref, onUnmounted, nextTick, watch } from 'vue';
import HeroSection from '@/components/HeroSection.vue';
import ChatContainer from '@/components/ChatContainer.vue';
import InputWrapper from '@/components/InputWrapper.vue';
import ScrollButton from '@/components/ScrollButton.vue';
import { useMessage } from '@/stores/messageStore';
import { apiService, connectWebsocket } from '@/services/api';

const messageStore = useMessage()
const chatWrapperRef = ref(null)
const threshold = 200
const isNearBottom = ref(true)

const retrieveSessionID = async () => {
    try {
        const response = await apiService.getSessionId();

        if (!response.data.error) {
            return response.data.message;
        }
        console.log("No session Id, Creating new one")
        const newResponse = await apiService.createSessionId();
        console.log(newResponse.data.message)
        return newResponse.data.message;
    } catch (error) {
        console.error("Session retrieval error:", error);
        messageStore.currentError = "Session error: " + error.message;
        messageStore.showError = true;
        return null;
    }
};

const checkScroll = () => {
    if (chatWrapperRef.value) {
        const { scrollTop, scrollHeight, clientHeight } = chatWrapperRef.value;
        const distanceFromBottom = scrollHeight - scrollTop - clientHeight;
        isNearBottom.value = distanceFromBottom <= threshold;
    }
};
const scrollToBottom = () => {
    chatWrapperRef.value.scrollTop = chatWrapperRef.value.scrollHeight;
}

watchEffect(async () => {
    const userMessage = messageStore.currentUserMessage
    if (userMessage && messageStore.sendMessage) {
        messageStore.appendMessage("user", userMessage)
        messageStore.appendMessage("assistant", "", true)
        const session_id = await retrieveSessionID()
        connectWebsocket(session_id, userMessage)
    }
})

watch(
    () => messageStore.conversations,
    async (newConversations) => {
        if (newConversations.length > 0) {
            if (chatWrapperRef.value) {
                chatWrapperRef.value.addEventListener('scroll', checkScroll);
            }
            await nextTick();
            checkScroll();
        }
    },
    { immediate: true }
)

watch(
    () => messageStore.conversations[messageStore.conversations.length - 1],
    async (latestMessage) => {
        if (latestMessage && latestMessage.showCursor) {
            await nextTick()     
            checkScroll()
        }
    }
)

onMounted(async () => {
  if (chatWrapperRef.value && messageStore.conversations.length > 0) {
    chatWrapperRef.value.addEventListener('scroll', checkScroll);
  }
  checkScroll()
});

onUnmounted(() => {
    if (chatWrapperRef.value) {
        chatWrapperRef.value.removeEventListener('scroll', checkScroll);
    }
});
</script>

<template>
    <div class="app-container">
        <HeroSection v-if="messageStore.conversations.length === 0" />
        <div v-else class="chat-wrapper" ref="chatWrapperRef">
            <ChatContainer />
            <ScrollButton @scroll="scrollToBottom" :visible="!isNearBottom" />
        </div>
        <InputWrapper />
    </div>
</template>

<style scoped>
.app-container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100%;
    overflow: hidden;
}

.chat-wrapper {
    flex-grow: 1;
    width: 100%;
    overflow-y: auto;
    scroll-behavior: smooth;
}
</style>