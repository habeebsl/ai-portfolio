<script setup>
import { RouterLink } from 'vue-router';
defineProps({
    name: String,
    url: String,
    isRouterLink: {
        type: Boolean,
        default: false,
    }
})
</script>

<template>
    <RouterLink v-if="isRouterLink" :to="url" class="hero-button">
        <span class="button-text">{{ name }}</span>
        <slot></slot>
    </RouterLink>
    <a v-else :href="url" class="hero-button">
        <span class="button-text">{{ name }}</span>
        <slot></slot>
    </a>
</template>

<style>
.hero-button {
    --button-bg: rgba(99, 102, 241, 0.1);
    --button-border: rgba(99, 102, 241, 0.2);
    --button-glow: rgba(99, 102, 241, 0.15);
    
    position: relative;
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 16px 32px;
    border-radius: 16px;
    background: var(--button-bg);
    border: 1px solid var(--button-border);
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 500;
    font-size: 15px;
    color: var(--text);
    text-decoration: none;
    transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
    overflow: hidden;
}

.hero-button::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(
        135deg,
        rgba(99, 102, 241, 0.2),
        rgba(34, 211, 238, 0.2)
    );
    opacity: 0;
    transition: opacity 0.4s ease;
}

.hero-button::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        135deg,
        var(--primary),
        var(--secondary)
    );
    filter: blur(40px);
    opacity: 0;
    z-index: -1;
    transition: opacity 0.4s ease;
}

.hero-button span {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    transition: transform 0.3s ease;
}

.hero-button svg {
    stroke: var(--primary);
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.hero-button:hover {
    --button-bg: rgba(99, 102, 241, 0.15);
    --button-border: rgba(99, 102, 241, 0.3);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px var(--button-glow);
}

.hero-button:hover::before {
    opacity: 1;
}

.hero-button:hover::after {
    opacity: 0.4;
}

.hero-button:hover svg {
    stroke: var(--secondary);
}

.hero-button:active {
    transform: translateY(1px);
    box-shadow: 0 4px 12px var(--button-glow);
}
</style>