<script setup>
import { useMessage } from '@/stores/messageStore';

const props = defineProps({
    prompt: String
})

const messageStore = useMessage()

const handleClick = () => {
    messageStore.currentUserMessage = props.prompt
    messageStore.sendMessage = true
}

</script>

<template>
    <div @click="handleClick" class="suggestion-box">
        <div class="suggestion-text">{{ prompt }}</div>
    </div>
</template>

<style scoped>
.suggestion-box {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 12px 14px;
    transition: all 0.2s ease;
    cursor: pointer;
}

.suggestion-box:hover {
    transform: translateY(-2px);
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.1);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.suggestion-text {
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.4;
}
</style>