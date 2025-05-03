<script setup lang="ts">
import { onMounted } from 'vue';

interface TimelineItem {
  title: string;
  subtitle: string;
  company?: string;
  duration: string;
  description: string;
}

defineProps<{
  items: TimelineItem[];
}>();

onMounted(() => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.timeline-item').forEach((el) => {
        observer.observe(el);
    });
});
</script>

<template>
  <div class="timeline-container">
    <div class="timeline-line"></div>

    <div
      v-for="(item, index) in items"
      :key="index"
      class="timeline-item"
      :style="{ '--delay': `${index * 0.2}s` }"
    >
      <div class="timeline-dot"></div>

      <div class="timeline-content">
        <div class="timeline-header">
          <h3 class="timeline-title">{{ item.title }}</h3>
          <span class="timeline-duration">{{ item.duration }}</span>
        </div>
        <div class="timeline-subtitle">{{ item.subtitle || item.company }}</div>
        <p class="timeline-description">{{ item.description }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.timeline-container {
  position: relative;
  padding-left: 100px;
  display: flex;
  flex-direction: column;
  gap: 60px;
}

.timeline-line {
  position: absolute;
  left: 50px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(
    to bottom,
    transparent,
    var(--primary) 10%,
    var(--secondary) 90%,
    transparent
  );
}

.timeline-item {
  position: relative;
  opacity: 0;
  transform: translateX(-20px);
}

.timeline-item.visible {
  animation: slideIn 0.3s ease forwards;
  animation-delay: var(--delay);
}

@keyframes slideIn {
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.timeline-dot {
  position: absolute;
  left: -50px;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  border: 2px solid var(--background);
  z-index: 1;
}

.timeline-content {
  position: relative;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 20px;
  transition: transform 0.3s ease;
  margin-left: 0;
}

.timeline-content:hover {
  transform: translateY(-5px);
}

.timeline-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.timeline-title {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 600;
  background: linear-gradient(135deg, var(--primary), var(--secondary));
  -webkit-background-clip: text;
  color: transparent;
}

.timeline-duration {
  font-size: 0.9rem;
  color: var(--text-secondary);
}

.timeline-subtitle {
  font-size: 1rem;
  color: var(--text-secondary);
  margin-bottom: 12px;
}

.timeline-description {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--text-secondary);
  margin: 0;
}

@media (max-width: 768px) {
  .timeline-container {
    padding-left: 60px; 
  }

  .timeline-line {
    left: 30px;
  }

  .timeline-dot {
    left: -30px;
  }

  .timeline-content {
    margin-left: 0;
  }
}

@media (max-width: 480px) {
  .timeline-container {
    padding-left: 40px;
  }

  .timeline-line {
    left: 20px;
  }

  .timeline-dot {
    left: -20px;
  }
}
</style>
