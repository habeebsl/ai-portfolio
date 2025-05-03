<script setup>
import PopupContainer from './PopupContainer.vue';
import { useProject } from '@/stores/projectStore';

const projectStore = useProject()

const handleBackClick = () => {
  projectStore.showInfo = false;
};
</script>

<template>
    <PopupContainer 
        v-if="projectStore.showInfo"
        @close="handleBackClick"
    >
        <div class="card">
            <h1 class="name">
                {{ projectStore.projectName }}
            </h1>
            <div class="description">
                <p>{{ projectStore.infoData }}</p>
            </div>
        </div>
    </PopupContainer>
</template>

<style scoped>
.card {
    color: rgba(255, 255, 255, 0.815);
}

.name {
    text-align: center;
}

.description {
    padding-left: 50px;
    padding-right: 50px;
    max-height: 400px;
    overflow-y: auto;
    white-space: pre-line;
    scrollbar-width: thin;
    scrollbar-color: rgba(255, 255, 255, 0.4) rgba(0, 0, 0, 0.2);
}

.description::-webkit-scrollbar {
    width: 8px;
}
</style>