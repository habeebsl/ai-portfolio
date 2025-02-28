<script setup>
defineProps({
    visible: Boolean
})

const emit = defineEmits(['scroll'])
</script>

<template>
    <button :class="`scroll-bottom-button ${visible ? 'visible' : ''}`" @click="emit('scroll')">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 5v14M5 12l7 7 7-7"/>
        </svg>
    </button>
</template>

<style scoped>
.scroll-bottom-button {
    position: fixed;
    bottom: 126px;
    right: 24px;
    background: var(--primary);
    border: none;
    border-radius: 50%;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.3s ease;
    z-index: 1000;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

.scroll-bottom-button svg {
    color: white;
}

.scroll-bottom-button.visible {
    opacity: 1;
    transform: translateY(0);
}

.scroll-bottom-button:hover {
    transform: scale(1.05);
    background: var(--primary-light);
}
</style>