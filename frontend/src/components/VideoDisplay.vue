<script setup>
import { ref, watch, nextTick } from 'vue';
import PopupContainer from './PopupContainer.vue';
import { useProject } from '@/stores/projectStore';

const projectStore = useProject();
const isLoading = ref(true);
const videoContainer = ref(null);

const handleBackClick = () => {
    projectStore.showVideo = false;
};

const handleIframeLoad = () => {
    setTimeout(() => {
        isLoading.value = false;
    }, 300); // Small delay for smoother transition
};

// Reset loading state when a new video is opened
watch(() => projectStore.showVideo, async (newValue) => {
    if (newValue) {
        isLoading.value = true;
        await nextTick();
    }
});
</script>

<template>
    <PopupContainer 
        v-if="projectStore.showVideo"
        @close="handleBackClick"
    >
        <div ref="videoContainer" class="video-container">
            <!-- Modern loading state -->
            <Transition name="fade">
                <div v-if="isLoading" class="loading-overlay">
                    <div class="loading-content">
                        <div class="modern-spinner">
                            <div class="spinner-ring"></div>
                            <div class="spinner-ring"></div>
                            <div class="spinner-ring"></div>
                        </div>
                        <p class="loading-text">Loading video</p>
                    </div>
                </div>
            </Transition>
            
            <!-- Video iframe with better loading handling -->
            <iframe
                :src="projectStore.VideoUrl"
                class="video-frame"
                :style="{ opacity: isLoading ? 0 : 1 }"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen"
                allowfullscreen
                @load="handleIframeLoad"
                loading="lazy"
            ></iframe>
        </div>
    </PopupContainer>
</template>

<style scoped>
.video-container {
    position: relative;
    width: 100%;
    height: 100%;
    overflow: hidden;
}

.loading-overlay {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.6));
    backdrop-filter: blur(8px);
    z-index: 10;
    border-radius: 16px;
}

.loading-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
}

.modern-spinner {
    position: relative;
    width: 60px;
    height: 60px;
}

.spinner-ring {
    position: absolute;
    width: 100%;
    height: 100%;
    border: 2px solid transparent;
    border-top: 2px solid var(--primary);
    border-radius: 50%;
    animation: modernSpin 1.2s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
}

.spinner-ring:nth-child(2) {
    width: 80%;
    height: 80%;
    top: 10%;
    left: 10%;
    border-top-color: var(--secondary);
    animation-duration: 1.8s;
    animation-direction: reverse;
}

.spinner-ring:nth-child(3) {
    width: 60%;
    height: 60%;
    top: 20%;
    left: 20%;
    border-top-color: rgba(255, 255, 255, 0.6);
    animation-duration: 1.5s;
}

.loading-text {
    color: rgba(255, 255, 255, 0.9);
    font-size: 0.875rem;
    font-weight: 500;
    margin: 0;
    letter-spacing: 0.5px;
}

.video-frame {
    width: 100%;
    height: 100%;
    border: none;
    border-radius: 16px;
    transition: opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Modern fade transition */
.fade-enter-active,
.fade-leave-active {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
    transform: scale(0.95);
}

@keyframes modernSpin {
    0% {
        transform: rotate(0deg);
        opacity: 1;
    }
    50% {
        opacity: 0.8;
    }
    100% {
        transform: rotate(360deg);
        opacity: 1;
    }
}

@media (max-width: 768px) {
    .modern-spinner {
        width: 48px;
        height: 48px;
    }
    
    .loading-text {
        font-size: 0.8rem;
    }
}
</style>