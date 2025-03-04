<script setup>
import HeroContent from '@/components/HeroContent.vue';
import VisualElement from '@/components/VisualElement.vue';
</script>

<template>
    <div class="hero-section">
        <HeroContent />
        <VisualElement />
    </div>
</template>

<style scoped>
.hero-section {
    max-width: 1000px;
    margin: 40px auto 30px;
    padding: 0 24px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    align-items: center;
    position: relative;
}

@media (max-width: 768px) {
    .hero-section {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 20px;
        margin: 30px auto 20px;
        max-height: calc(100vh - 100px);
        overflow-y: auto;
    }
}
</style>