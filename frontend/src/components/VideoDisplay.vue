<script setup>
import PopupContainer from './PopupContainer.vue';
import { useProject } from '@/stores/projectStore';

const projectStore = useProject()

const handleBackClick = () => {
    projectStore.showVideo = false;
};
</script>

<template>
    <PopupContainer 
        v-if="projectStore.showVideo"
        @close="handleBackClick"
    >
        <iframe
            :src="projectStore.VideoUrl"
            class="video-frame"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen"
            allowfullscreen
        ></iframe>
    </PopupContainer>
</template>

<style scoped>
.video-frame {
    width: 100%;
    height: 100%;
    border: none;
    border-radius: 16px;
    object-fit: contain;
}
</style>