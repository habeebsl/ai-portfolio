<template>
    <div class="typing-indicator">
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    </div>
</template>

<style scoped>
.typing-indicator {
    display: flex;
    gap: 4px;
    padding: 0;
    justify-content: center;
    align-items: center;
}

.typing-dot {
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background-color: #fff;
    animation: typingBounce 1.4s infinite ease-in-out;
}

.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }
</style>