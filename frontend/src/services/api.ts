import axios from 'axios'
import { useMessage } from '@/stores/messageStore'
import { isJSON } from '@/utils/helpers'

export const BASE_URL = import.meta.env.VITE_API_BASE

const apiClient = axios.create({
	baseURL: `https://${BASE_URL}`,
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
    const socket = new WebSocket(`wss://${BASE_URL}/ws?session_token=${token}`)

    socket.addEventListener("open", async () => {
        socket.send(message);
    });

    socket.addEventListener("message", (event) => {
        if (isJSON(event.data)) {
            const data = JSON.parse(event.data)
            if (data.error) {
                console.error("Server Error: ", data.error)
                messageStore.currentError = "Server error"
                messageStore.showError = true
                messageStore.sending = false
                messageStore.removeLastMessage()
                messageStore.resetStoreState()
                return;
            }
        }

        if (event.data === "__DONE__") { 
            messageStore.sending = false
            messageStore.finishLatestAIMessage()
            messageStore.resetStoreState()
            return;
        }
        messageStore.updateLatestAIMassage(event.data)
    });

    socket.addEventListener("error", (error) => {
        messageStore.removeLastMessage()
        messageStore.currentError = "Couldn't Connect to Websocket"
        messageStore.showError = true
        messageStore.sending = false
        messageStore.resetStoreState()
        console.error(`WebSocket error: ${error}`)
    });
}