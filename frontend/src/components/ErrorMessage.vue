<script setup>
defineProps({
    error: String
})
</script>

<template>
    <div class="error-message" id="error-message">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 15a1.5 1.5 0 1 1 1.5-1.5A1.5 1.5 0 0 1 12 17zm1-4h-2V7h2z"/>
        </svg>
        <span>{{ error }}</span>
    </div>
</template>

<style scoped>
.error-message {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 16px;
    background: rgba(244, 113, 181, 0.1);
    border: 1px solid rgba(244, 113, 181, 0.3);
    border-radius: 12px;
    color: var(--accent);
    font-size: 15px;
    font-weight: 500;
    line-height: 1.5;
    animation: fadeIn 0.3s ease-in-out;
}

.error-message svg {
    flex-shrink: 0;
    width: 20px;
    height: 20px;
    fill: var(--accent);
}
</style>