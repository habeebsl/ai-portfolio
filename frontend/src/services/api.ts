import axios from 'axios'
import { useMessage } from '@/stores/messageStore'

export const BASE_URL = import.meta.env.VITE_API_BASE

const apiClient = axios.create({
	baseURL: `http://${BASE_URL}`,
	headers: {
		'Content-Type': 'application/json'
	},
    withCredentials: true
})


export const apiService = {
    createSessionId() {
        return apiClient.get("/session/new")
    },

    getSessionId() {
        return apiClient.get("/session/validate")
    },

    getSessionData() {
        return apiClient.get("/session/data") 
    }
}

export const connectWebsocket = async (token: string, message: string) => {
    const messageStore = useMessage()
    const socket = new WebSocket(`ws://${BASE_URL}/ws?session_token=${token}`)

    socket.addEventListener("open", async () => {
        messageStore.sending = true
        socket.send(message);
    });

    socket.addEventListener("message", (event) => {
        if (event.data === "__DONE__") { 
            socket.close();
            return;
        }
        messageStore.updateLatestAIMassage(event.data)
    });

    socket.addEventListener("close", (event) => {
        if (event.code === 1011 && event.reason === "Redis connection unavailable") {
            messageStore.currentError = "Server error: Redis connection unavailable"
            messageStore.showError = true
            messageStore.sending = false
            messageStore.resetStoreState()
        }
        messageStore.finishLatestAIMessage()
        messageStore.sending = false
        messageStore.resetStoreState()
    })

    socket.addEventListener("error", (error) => {
        messageStore.removeLastMessage()
        messageStore.currentError = "WebSocket error"
        messageStore.showError = true
        messageStore.sending = false
        messageStore.resetStoreState()
        console.error(`WebSocket error: ${error}`)
    });
}