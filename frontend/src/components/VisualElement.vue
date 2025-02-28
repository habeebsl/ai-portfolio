<script setup>
import portrait from '@/assets/images/portrait1.jpeg'
</script>

<template>
    <div class="visual-element">
        <div class="glow-effect"></div>
        <img :src="portrait" alt="Habeeb Salami" class="profile-image">
        <div class="tech-sphere"></div>
        <div class="code-sphere"></div>
    </div>
</template>

<style scoped>
.visual-element {
    position: relative;
    height: 340px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.profile-image {
    height: 280px;
    border-radius: 24px;
    object-fit: cover;
    position: relative;
    z-index: 2;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.glow-effect {
    position: absolute;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    filter: blur(100px);
    opacity: 0.12;
    z-index: 1;
}

.tech-sphere, .code-sphere {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(5px);
    z-index: 3;
}

.tech-sphere {
    width: 90px;
    height: 90px;
    top: 40px;
    right: 40px;
    animation: float 6s ease-in-out infinite;
}

.code-sphere {
    width: 60px;
    height: 60px;
    bottom: 50px;
    left: 30px;
    animation: float 8s ease-in-out infinite reverse;
}

@media (max-width: 768px) {
    .visual-element {
        height: 280px;
    }

    .profile-image {
        height: 240px;
    }

    .tech-sphere {
        width: 70px;
        height: 70px;
    }

    .code-sphere {
        width: 50px;
        height: 50px;
    }
}
</style>