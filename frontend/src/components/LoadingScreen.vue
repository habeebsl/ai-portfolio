<script setup>
defineProps({
progress: Number
})
</script>

<template>
    <div class="container">
        <div class="loading-wrapper">
            <img 
                src="/favicon/android-chrome-192x192.png" 
                alt="Loading Icon" 
                class="logo"
            />
            <div class="progress-bar">
                <div class="progress-fill" :style="{ transform: `translateX(${-(100 - progress)}%)` }"></div>
            </div>
        </div>
    </div>
</template>
  
<style>
.container {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

.loading-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
}

.logo {
    width: 50px;
    height: 50px;
    animation: float 3s infinite ease-in-out;
}

.progress-bar {
    width: 200px;
    height: 4px;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 999px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    width: 100%;
    background: linear-gradient(90deg, #60a5fa, #a78bfa);
    border-radius: 999px;
    transform: translateX(-100%);
    transition: transform 0.3s ease-out;
}
</style>