<script setup>
import { useMessage } from '@/stores/messageStore';

const messageStore = useMessage()
const emit = defineEmits(['scroll'])
</script>

<template>
    <div @click="emit('scroll')" class="new-message-notification">
        {{messageStore.newMessageCount}} new message{{messageStore.newMessageCount > 1 ? 's' : ''}}
    </div>
</template>


<style>
.new-message-notification {
    position: fixed;
    bottom: 126px;
    left: 50%;
    transform: translateX(-50%) translateY(20px);
    background: var(--primary);
    color: white;
    padding: 12px 24px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    z-index: 1000;
    opacity: 0;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 8px;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

.new-message-notification::before {
    content: '●';
    color: white;
    animation: pulse 2s infinite;
}

.new-message-notification.visible {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}

.new-message-notification:hover {
    background: var(--primary-light);
    transform: translateX(-50%) translateY(-2px);
}
</style>