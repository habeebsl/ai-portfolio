import { defineStore } from 'pinia'
import { marked } from 'marked'


interface Message {
    role: string;
    content: string | Promise<string>;
    showCursor?: boolean 
}

export const useMessage = defineStore('message', {
    state: () => ({
        currentUserMessage: null,
        currentError: '',
        showError: false,
        sending: false,
        sendMessage: false,
        conversations: [] as Message[],
        promptSuggestions: [] as String[],
        newMessageCount: 0,
        accumulatedMessage: ''
    }),

    actions: {
        updateLatestAIMassage(message: string) {
            this.accumulatedMessage += message
            if (this.conversations.length > 0) {
                this.conversations[this.conversations.length-1] = {
                    role: "assistant", 
                    content: marked.parse(this.accumulatedMessage),
                    showCursor: true
                }
            }
        },

        finishLatestAIMessage() {
            if (this.conversations.length > 0) {
                this.conversations[this.conversations.length - 1].showCursor = false;
            }
        },

        appendMessage(role: string, message: string, showCursor: boolean = false) {
            this.conversations.push({ 
                role: role, 
                content: message, 
                showCursor: showCursor
            })
        },

        resetStoreState() {
            this.currentUserMessage = null
            this.sendMessage = false
            this.accumulatedMessage = ''
        },

        removeLastMessage() {
            this.conversations.pop()
        }
    }
})