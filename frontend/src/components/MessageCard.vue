<script setup>
defineProps({
    avatar: {
        type: String,
        required: true,
        validator: value => ["You", "AI"].includes(value)
    },
    message: String,
    showCursor: Boolean
})
</script>

<template>
    <div class="message-container user-message">
        <div class="avatar">{{ avatar }}</div>
        <div class="message-content">
            <p>
                <span v-if="avatar === 'AI'" v-html="message"></span>
                <span v-else>{{ message }}</span>
                <span v-if="showCursor" class="cursor"></span>
            </p>
            
        </div>
    </div>
</template>

<style scoped>
.message-container {
    display: flex;
    gap: 16px;
    padding: 20px;
    margin: 20px 0;
    background: linear-gradient(165deg, rgba(255, 255, 255, 0.03), rgba(255, 255, 255, 0.01) 100%);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 18px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.message-container:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(99, 102, 241, 0.2);
    border-color: rgba(255, 255, 255, 0.1);
}

.avatar {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text);
    font-weight: 600;
    font-size: 16px;
}

.message-content {
    flex: 1;
    font-size: 15px;
    line-height: 1.7;
    color: var(--text);
}

.cursor {
    display: inline-block;
    width: 7px;
    height: 7px;
    background-color: white;
    border-radius: 50%;
    animation: cursor-pulse 1.5s ease-in-out infinite;
    margin-left: 5px;
    vertical-align: middle;
}
</style>