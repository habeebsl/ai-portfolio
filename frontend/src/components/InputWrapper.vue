<script setup>
import SuggestionCard from '@/components/SuggestionCard.vue';
import SuggestionsContainer from '@/components/SuggestionsContainer.vue';
import InputContainer from '@/components/InputContainer.vue';
import { useMessage } from '@/stores/messageStore';

const messageStore = useMessage()
</script>

<template>
    <div class="input-wrapper">
        <div class="input-content">
            <SuggestionsContainer v-if="messageStore.conversations.length === 0">
                <SuggestionCard 
                    v-for="(prompt, index) in messageStore.promptSuggestions"
                    :key="index"
                    :prompt="prompt"
                />
            </SuggestionsContainer>
            <InputContainer />
        </div>
    </div>
</template>

<style scoped>
.input-wrapper {
    flex-shrink: 0; /* Prevent shrinking */
    width: 100%;
    display: flex;
    justify-content: center;
    background: linear-gradient(
        to bottom,
        transparent,
        var(--background) 20%
    );
    backdrop-filter: blur(28px);
    -webkit-backdrop-filter: blur(28px);
    z-index: 100;
    box-shadow: 0 -10px 20px rgba(0, 0, 0, 0.1);
    padding: 20px 0;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.input-content {
    max-width: 1000px;
    width: calc(100% - 48px);
}

/* Mobile specific fixes */
@media (max-width: 768px) {
    .input-wrapper {
        padding: 16px 0 max(16px, env(safe-area-inset-bottom)); /* Respect safe area */
        position: relative; /* Avoid fixed positioning issues on mobile */
    }
    
    .input-content {
        width: calc(100% - 32px);
    }
}

/* iOS Safari specific fixes */
@supports (-webkit-touch-callout: none) {
    .input-wrapper {
        padding-bottom: max(20px, env(safe-area-inset-bottom));
    }
}
</style>