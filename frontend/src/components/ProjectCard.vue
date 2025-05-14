<script setup>
import ButtonContainer from "./ButtonContainer.vue";
import { useProject } from "@/stores/projectStore";

const props = defineProps({
  projectName: String,
  description: String,
  fullDescription: String,
  link: String,
  githubLink: String,
  videoLink: String,
  thumbnail: String,
  showLink: {
    type: String,
    default: true
  }
});

const projectStore = useProject();

const handleVideoButtonClick = (event) => {
  event.stopPropagation();
  projectStore.VideoUrl = props.videoLink;
  projectStore.showVideo = true;
};

const handleInfoClick = (event) => {
    event.stopPropagation();
    projectStore.projectName = props.projectName
    projectStore.infoData = props.fullDescription
    projectStore.showInfo = true;
}

const handleLinkButtonClick = (event) => {
  event.stopPropagation();
  window.open(props.link, "_blank");
};

const handleGithubButtonClick = (event) => {
  event.stopPropagation();
  window.open(props.githubLink, "_blank");
};
</script>

<template>
  <div class="project-card" @click="handleLinkButtonClick">
    <div class="project-image-container">
      <img :src="thumbnail" alt="" class="project-image" />
    </div>
    <div class="action-area">
      <div class="content">
        <h1 class="project-title">{{ projectName }}</h1>
        <p class="project-description">
          {{ description }}
        </p>
      </div>
      <div class="action-buttons">
        <ButtonContainer @click="handleInfoClick">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3">
                <path fill="url(#buttonGradient)" d="M440-280h80v-240h-80v240Zm40-320q17 0 28.5-11.5T520-640q0-17-11.5-28.5T480-680q-17 0-28.5 11.5T440-640q0 17 11.5 28.5T480-600Zm0 520q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z"/>
            </svg>
          </ButtonContainer>
        <div class="right-buttons">
          <ButtonContainer @click="handleVideoButtonClick">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                height="24px"
                viewBox="0 -960 960 960"
                width="24px"
            >
                <defs>
                <linearGradient
                    id="buttonGradient"
                    x1="0%"
                    y1="0%"
                    x2="100%"
                    y2="100%"
                >
                    <stop offset="0%" stop-color="var(--primary)" />
                    <stop offset="100%" stop-color="var(--secondary)" />
                </linearGradient>
                </defs>
                <path
                    fill="url(#buttonGradient)"
                    d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h480q33 0 56.5 23.5T720-720v180l160-160v440L720-420v180q0 33-23.5 56.5T640-160H160Z"
                />
            </svg>
          </ButtonContainer>
          <ButtonContainer @click="handleGithubButtonClick">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
              <path fill="url(#buttonGradient)" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
            </svg>
          </ButtonContainer>
          <ButtonContainer v-if="showLink" @click="handleLinkButtonClick">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                height="24px"
                viewBox="0 -960 960 960"
                width="24px"
            >
                <path
                    fill="url(#buttonGradient)"
                    d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h280v80H200v560h560v-280h80v280q0 33-23.5 56.5T760-120H200Zm188-212-56-56 372-372H560v-80h280v280h-80v-144L388-332Z"
                />
            </svg>
          </ButtonContainer>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.project-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 20px;
  height: 300px;
  width: 300px;
  color: var(--text);
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.project-image-container {
  flex: 1;
  position: relative;
  overflow: hidden;
}

.project-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  transition: transform 0.3s ease;
}

.action-area {
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.content {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.project-title {
  margin: 0;
  font-size: 1.2rem;
}

.project-description {
  margin: 0;
  font-size: 0.875rem;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.4;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.right-buttons {
  display: flex;
  gap: 5px;
  align-self: flex-end;
}

.action-buttons {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.project-card:hover .project-image {
  transform: scale(1.1);
}
</style>
