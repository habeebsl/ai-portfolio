<script setup>
import { ref, onMounted, watchEffect } from 'vue'
import TypingIndicator from './TypingIndicator.vue';
import { useMessage } from '@/stores/messageStore';

const messageStore = useMessage()
const textareaRef = ref(null)
const content = ref('')
const maxHeight = ref(200)
let initialHeight = 0
let resizeTimeout = null

const updateHeight = () => {
  const textArea = textareaRef.value
  if (!textArea) return
  
  textArea.style.height = 'auto'
  const newHeight = Math.max(
    initialHeight,
    Math.min(textArea.scrollHeight, maxHeight.value)
  )
  
  if (textArea.offsetHeight !== newHeight) {
    textArea.style.height = `${newHeight}px`
  }
}

const throttledResize = () => {
  if (resizeTimeout) return
  
  resizeTimeout = setTimeout(() => {
    updateHeight()
    resizeTimeout = null
  }, 100)
}

const handleEnter = (e) => {
    if (e.key === 'Enter' && !e.shiftKey && !messageStore.sending) {
        e.preventDefault();
        if (!content.value.trim()) return;
        messageStore.currentUserMessage = content.value
        messageStore.sendMessage = true
        content.value = ''
    }
}

const handleSend = () => {
    if (!content.value.trim()) return;
    messageStore.currentUserMessage = content.value
    messageStore.sendMessage = true
    content.value = ''
}

watchEffect(() => {
    if (messageStore.showError) {
        content.value = messageStore.currentUserMessage
    }
})

onMounted(async () => {
    const textArea = textareaRef.value
    if (textArea) {
        initialHeight = textArea.scrollHeight
        updateHeight()
    }
})
</script>

<template>
    <div class="input-container">
        <textarea 
            @keydown="handleEnter" 
            @input="throttledResize"
            class="input-field" 
            id="message-input" 
            ref="textareaRef"
            v-model="content"
            placeholder="Ask anything..."
        ></textarea>
        <button :disabled="messageStore.sending" @click="handleSend" class="send-button" id="submit-btn">
            <svg v-if="!messageStore.sending" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M22 2L11 13M22 2L15 22L11 13M11 13L2 9L22 2"/>
            </svg>
            <TypingIndicator v-else />
        </button>
    </div>
</template>

<style scoped>
.input-container {
    display: flex;
    max-width: 1000px;
    margin: 0 auto;
    position: relative;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    overflow: hidden;
    transition: all 0.2s ease;
}

.input-container:focus-within {
    border-color: rgba(255, 255, 255, 0.1);
    background: rgba(255, 255, 255, 0.04);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.input-field {
    width: 100%;
    padding: 18px 66px 18px 20px;
    background: transparent;
    border: none;
    color: var(--text);
    font-size: 15px;
    line-height: 1.6;
    font-family: inherit;
    resize: none;
    outline: none;
    position: relative;
    z-index: 2;
}

.send-button {
    position: absolute;
    right: 12px;
    top: 50%;
    transform: translateY(-50%);
    width: 42px;
    height: 42px;
    border: none;
    border-radius: 12px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    color: white;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 2;
    transition: all 0.2s ease;
}

.send-button:hover {
    transform: translateY(-50%) scale(1.05);
    box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
}
</style>