<script setup>
import MessageCard from '@/components/MessageCard.vue';
import ErrorMessage from './ErrorMessage.vue';
import { useMessage } from '@/stores/messageStore';
import { watch, nextTick, onMounted } from 'vue';

const messageStore = useMessage();

const scrollToBottom = async (bypass = false) => {
  await nextTick();
  const chatWrapper = document.querySelector('.chat-wrapper');
  if (chatWrapper) {
    const threshold = 500;
    const current = chatWrapper.scrollHeight - chatWrapper.scrollTop - chatWrapper.clientHeight
    const isNearBottom = current <= threshold;

    if (isNearBottom || bypass) {
      chatWrapper.scrollTop = chatWrapper.scrollHeight;
    }
  }
};

watch(
  () => messageStore.conversations.length,
  () => scrollToBottom()
);

onMounted(() => {
    scrollToBottom(true);
});
</script>

<template>
  <div class="chat-container">
    <MessageCard 
        v-for="(convo, index) in messageStore.conversations" 
        :key="index"
        :avatar="convo.role === 'user' ? 'You' : 'AI'"
        :message="convo.content"
        :showCursor="convo.showCursor ? true : false"
    />
    <ErrorMessage v-if="messageStore.showError" :error="messageStore.currentError" />
  </div>
</template>

<style scoped>
.chat-container {
    max-width: 1000px;
    width: calc(100% - 48px);
    margin: 0 auto;
    padding: 24px;
    margin-top: 40px;
}
</style>