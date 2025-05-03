<script setup>
const emit = defineEmits(['close'])
</script>

<template>
  <div
    class="video-overlay"
    @click.self="() => emit('close')"
  >
    <div class="video-container">
      <button class="close-button" @click="() => emit('close')">
        <span class="close-icon">×</span>
      </button>
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.video-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.video-container {
  position: relative;
  width: 60%;
  max-width: 960px;
  aspect-ratio: 16/9;
  background: rgb(18, 18, 18);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 16px;
}

.close-button {
  position: absolute;
  top: -40px;
  right: -40px;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 1001;
}

.close-icon {
  font-size: 32px;
  color: white;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  transition: all 0.3s ease;
}

.close-icon:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: scale(1.1);
}
</style>