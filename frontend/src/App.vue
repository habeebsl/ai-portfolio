<script setup>
import { onMounted, ref } from 'vue';
import { RouterView } from 'vue-router'
import NavBar from '@/components/NavBar.vue';
import LoadingScreen from './components/LoadingScreen.vue';
import { useMessage } from './stores/messageStore';
import { apiService } from './services/api';

const messageStore = useMessage()
const isLoading = ref(false)
const progress = ref(0)

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
  <LoadingScreen v-if="isLoading" :progress="progress" />
  <div v-else>
      <NavBar v-if="messageStore.conversations.length > 0" />
      <RouterView />
  </div>
</template>

<style scoped>
</style>
