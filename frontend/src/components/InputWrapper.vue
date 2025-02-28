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
    position: sticky;
    bottom: 0;
    left: 0;
    right: 0;
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
    padding: 24px 0;
    margin-top: auto;
}

.input-content {
    max-width: 1000px;
    width: calc(100% - 48px);
}
</style>