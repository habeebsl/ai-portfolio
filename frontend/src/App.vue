<script setup>
import { onMounted, ref, watch } from 'vue';
import { RouterView, useRoute } from 'vue-router'
import NavBar from '@/components/NavBar.vue';
import LoadingScreen from './components/LoadingScreen.vue';
import { useMessage } from './stores/messageStore';
import { apiService } from './services/api';

const messageStore = useMessage()
const isLoading = ref(false)
const progress = ref(0)
const route = useRoute()

// Handle scroll behavior based on route
watch(() => route.path, (newPath) => {
    // Only prevent scroll on home page (chat interface)
    if (newPath === '/') {
        document.body.classList.add('no-scroll')
    } else {
        document.body.classList.remove('no-scroll')
    }
}, { immediate: true })

onMounted(async () => {
    try {
        progress.value = 20
        isLoading.value = true
        const response = await apiService.getSessionData()
        progress.value = 50
        const data = response.data
        console.log(data)
        messageStore.promptSuggestions = data.prompts
        messageStore.conversations = data.conversations
    } catch (error) {
        console.error(error.message)
    } finally {
        progress.value = 100
        isLoading.value = false
    }
})
</script>

<template>
    <div class="app-root">
        <LoadingScreen v-if="isLoading" :progress="progress" />
        <div v-else class="app-content">
            <NavBar v-if="messageStore.conversations.length > 0 || route.path !== '/'" />
            <RouterView />
        </div>
    </div>
</template>

<style scoped>
.app-root {
    height: 100%;
    display: flex;
    flex-direction: column;
}

.app-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: auto; /* Allow scroll by default */
}

/* Only hide overflow for home route (chat interface) */
:global(body.no-scroll) .app-content {
    overflow: hidden;
}
</style>
