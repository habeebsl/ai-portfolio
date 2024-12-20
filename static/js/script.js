document.addEventListener("DOMContentLoaded", () => {
    const messageInput = document.getElementById("message-input")
    const messageCont = document.getElementsByClassName("message-container")
    const submitBtn = document.getElementById("submit-btn")
    const content = document.getElementById("content")
    const submitSvg = 
    `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M22 2L11 13M22 2L15 22L11 13M11 13L2 9L22 2"/>
    </svg>`

    console.log(messageCont)
    requestAnimationFrame(() => {
        if (messageCont.length) {
            window.scrollTo(0, document.body.scrollHeight);
        } else {
            window.scrollTo(0, 0);    
        }
    });
   

    submitBtn.addEventListener("click", sendMessage)

    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            if (submitBtn.disabled !== true) {
                sendMessage()
            } 
        }
    })

    // Helper function: Reset send button
    function resetSendButton() {
        submitBtn.disabled = false;
        submitBtn.innerHTML = submitSvg;
        requestAnimationFrame(() => {
            window.scrollTo(0, document.body.scrollHeight);
        });
    }

    // Helper function: Create message elements
    function createMessageElement(role, message) {
        const messageContainer = document.createElement('div');
        messageContainer.classList.add('message-container');
        if (role === "You") {
            messageContainer.classList.add('user-message');
        }
        const avatar = document.createElement('div');
        avatar.classList.add('avatar');
        avatar.textContent = role;
        messageContainer.appendChild(avatar);

        const messageContent = document.createElement('div');
        messageContent.classList.add('message-content');

        const paragraph = document.createElement('p');
        paragraph.innerHTML = message;

        messageContent.appendChild(paragraph);
        messageContainer.appendChild(messageContent);
    
        return messageContainer;
    }
    
    async function sendMessage() {
        message = messageInput.value.trim()
        
        if (!message){
            messageInput.value = "";
            return;
        }
        console.log(message)
        content.appendChild(createMessageElement("You", message))
        requestAnimationFrame(() => {
            window.scrollTo(0, document.body.scrollHeight);
        });
        messageInput.value = ""
        submitBtn.disabled = true
        submitBtn.innerHTML = 
        `<div class="typing-indicator">
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        </div>`

        const response = await fetch("/send_message", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        })

        const data = await response.json()
        console.log(data)
        submitBtn.innerHTML = submitSvg
 
        content.appendChild(createMessageElement("AI", data.message))
        resetSendButton()


    }
})