<script setup>
import HeroButtonContainer from '@/components/HeroButtonContainer.vue';
</script>

<template>
    <div class="hero-buttons">
        <HeroButtonContainer name="Contact" url="/contact" :isRouterLink="true">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M13 19L22 12L13 5" />
                <path d="M22 12H2" />
            </svg>
        </HeroButtonContainer>
        <HeroButtonContainer name="Get Resume" url="https://drive.usercontent.google.com/u/0/uc?id=1gbS64L1dpQm67Xz6yZoaK6Yy9SfCpK18&export=download">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                <polyline points="7 10 12 15 17 10" />
                <line x1="12" y1="15" x2="12" y2="3" />
            </svg>
        </HeroButtonContainer>
    </div>
</template>

<style scoped>
.hero-buttons {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}

@media (max-width: 768px) {
    .hero-buttons {
        justify-content: center;
        gap: 12px;
    }
}
</style>