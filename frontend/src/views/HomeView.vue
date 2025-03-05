<script setup>
import { onMounted, ref, onUnmounted, nextTick, computed, watchEffect, watch } from 'vue';
import HeroSection from '@/components/HeroSection.vue';
import ChatContainer from '@/components/ChatContainer.vue';
import InputWrapper from '@/components/InputWrapper.vue';
import ScrollButton from '@/components/ScrollButton.vue';
import { useMessage } from '@/stores/messageStore';
import { apiService, connectWebsocket } from '@/services/api';

const messageStore = useMessage()
const chatWrapperRef = ref(null)
const scrollTop = ref(0)
const scrollHeight = ref(0)
const clientHeight = ref(0)

const isNearBottom = computed(() => {
    console.log('Checking isNearBottom', {
        scrollTop: scrollTop.value,
        scrollHeight: scrollHeight.value,
        clientHeight: clientHeight.value
    });
    
    const threshold = 200;
    return scrollHeight.value - scrollTop.value - clientHeight.value <= threshold;
});

const updateScrollMetrics = () => {
  if (chatWrapperRef.value) {
    scrollTop.value = chatWrapperRef.value.scrollTop;
    scrollHeight.value = chatWrapperRef.value.scrollHeight;
    clientHeight.value = chatWrapperRef.value.clientHeight;
  }
};

const scrollToBottom = () => {
    chatWrapperRef.value.scrollTop = chatWrapperRef.value.scrollHeight;
}

onMounted(() => {
    if (chatWrapperRef.value) {
        scrollToBottom()
        updateScrollMetrics();
    }
});

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

watchEffect(async () => {
    const userMessage = messageStore.currentUserMessage
    if (userMessage && messageStore.sendMessage) {
        messageStore.appendMessage("user", userMessage)
        messageStore.appendMessage("assistant", "", true)
        messageStore.sending = true
        const session_id = await retrieveSessionID()
        connectWebsocket(session_id, userMessage)
    }
})

watch(
    () => messageStore.conversations[messageStore.conversations.length - 1],
    async (latestMessage) => {
        if (latestMessage && latestMessage.showCursor) {
            updateScrollMetrics()
        }
    }
)
</script>

<template>
    <div class="app-container">
        <HeroSection v-if="messageStore.conversations.length === 0" />
        <div v-else class="chat-wrapper" ref="chatWrapperRef" @scroll="updateScrollMetrics">
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