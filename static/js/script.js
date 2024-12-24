document.addEventListener("DOMContentLoaded", () => {
    // DOM Elements
    const messageInput = document.getElementById("message-input");
    const messageCont = document.querySelectorAll(".message-container");
    const suggestions = document.querySelector('.prompt-suggestions');
    const submitBtn = document.getElementById("submit-btn");
    const suggestionBoxes = document.querySelectorAll('.suggestion-box');
    const content = document.getElementById("content");
    const heroSection = document.querySelector(".hero-section");

    // State Variables
    let isScrolledUp = false;
    let newMessageCount = 0;

    // UI Templates
    const submitSvg = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M22 2L11 13M22 2L15 22L11 13M11 13L2 9L22 2"/>
    </svg>`;

    // UI Components Setup
    const scrollButton = createScrollButton();
    const notification = createNotificationBanner();

    function createScrollButton() {
        const button = document.createElement('button');
        button.className = 'scroll-bottom-button';
        button.id = 'scroll-bottom-btn';
        button.style.display = 'none';
        button.innerHTML = `<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 5v14M5 12l7 7 7-7"/>
        </svg>`;
        document.body.appendChild(button);
        return button;
    }

    function createNotificationBanner() {
        const banner = document.createElement('div');
        banner.className = 'new-message-notification';
        banner.style.display = 'none';
        document.body.appendChild(banner);
        return banner;
    }

    // Message Handling
    async function sendMessage(prompt = null) {
        const message = prompt ?? messageInput.value.trim();
        if (!message) return;

        removeErrorMessage();
        if (!navigator.onLine) {
            handleError("It seems you're offline right now. Please check your internet connection and try again.");
            messageInput.value = message;
            return;
        }
        removeHeroSection();
        displayUserMessage(message);
        resetInput();
        setLoadingState();

        try {
            const response = await fetch("/send_message", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message })
            });

            if (!response.ok) throw new Error(`Server error: ${response.status}`);
            
            const data = await response.json();
            if (data.error) throw new Error(data.error);
            appendMessageAndScroll("AI", data.message)
        } catch (error) {
            const userMessages = document.querySelectorAll('.user-message');
            for (let i = userMessages.length - 1; i >= 0; i--) {
                if (userMessages[i].textContent === message) {
                    userMessages[i].remove();
                    break;
                }
            }
            console.log(`Error: ${error}`);
            messageInput.value = message;
            handleError(error);
        } finally {
            resetSendButton();
            checkScroll();
        }
    }

    function createMessageElement(role, message) {
        const messageContainer = document.createElement('div');
        messageContainer.classList.add('message-container');

        const avatar = document.createElement('div');
        avatar.classList.add('avatar');
        avatar.textContent = role;
        messageContainer.appendChild(avatar);

        const messageContent = document.createElement('div');
        messageContent.classList.add('message-content');

        const paragraph = document.createElement('p');
        if (role === "You") {
            messageContainer.classList.add('user-message');
            paragraph.textContent = message;
        } else {
            paragraph.innerHTML = message;
            if (isScrolledUp) showNotification();
        }

        messageContent.appendChild(paragraph);
        messageContainer.appendChild(messageContent);
        setTimeout(checkScroll, 100);
        return messageContainer;
    }

    // UI State Management
    function checkScroll() {
        if (content.querySelectorAll('.message-container').length < 2) {
            hideScrollButton();
            content.style.paddingBottom = '0'
            return;
        }
        content.style.paddingBottom = '150px'
        const distanceFromBottom = document.documentElement.scrollHeight - window.scrollY - window.innerHeight;
        isScrolledUp = distanceFromBottom > 100;
        
        if (distanceFromBottom < 10) {
            hideScrollButton();
            hideNotification();
        } else {
            showScrollButton();
        }
    }

    function showNotification() {
        newMessageCount++;
        notification.textContent = `${newMessageCount} new message${newMessageCount > 1 ? 's' : ''}`;
        notification.style.display = 'flex';
        setTimeout(() => notification.classList.add('visible'), 10);
    }

    function hideNotification() {
        notification.classList.remove('visible');
        setTimeout(() => {
            notification.style.display = 'none';
            newMessageCount = 0;
        }, 300);
    }

    // UI Helpers
    function initializeTextArea(textArea, maxHeight = 200) {
        const initialHeight = textArea.scrollHeight;

        function updateHeight() {
            textArea.style.height = 'auto';
            const newHeight = Math.max(
                initialHeight,
                Math.min(textArea.scrollHeight, maxHeight)
            );
            
            if (textArea.offsetHeight !== newHeight) {
                textArea.style.height = `${newHeight}px`;
            }
        }
    
        const throttledUpdate = throttle(updateHeight, 16);
        textArea.addEventListener('input', throttledUpdate);
        textArea.addEventListener('change', throttledUpdate);
        updateHeight();
    
        return () => {
            textArea.removeEventListener('input', throttledUpdate);
            textArea.removeEventListener('change', throttledUpdate);
        };
    }
    
    function throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    function displayUserMessage(message) {
        appendMessageAndScroll("You", message)
        if (suggestions) hideSuggestions();
    }

    function manageHeroSection() {
        if (isDeviceWidthNotLessThan(768) && heroSection) {
            console.log("setting overflow hidden")
            document.body.style.overflowY = 'hidden'
        } else {
            document.body.style.overflowY = 'auto'
        }
    }

    function isDeviceWidthNotLessThan(minWidth) {
        return window.matchMedia(`(min-width: ${minWidth}px)`).matches;
    }

    function resetInput() {
        messageInput.value = "";
        messageInput.style.height = 'auto';
    }

    function setLoadingState() {
        submitBtn.disabled = true;
        submitBtn.innerHTML = `<div class="typing-indicator">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        </div>`;
    }

    function resetSendButton() {
        submitBtn.disabled = false;
        submitBtn.innerHTML = submitSvg;
    }

    function handleError(error) {
        const scrollTop = document.documentElement.scrollTop
        const clientHeight =  document.documentElement.clientHeight
        const scrollHeight = document.documentElement.scrollHeight
        let errorElement = `<div class="error-message" id="error-message">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 15a1.5 1.5 0 1 1 1.5-1.5A1.5 1.5 0 0 1 12 17zm1-4h-2V7h2z"/>
        </svg>
        <span>${error}</span>
        </div>`;   
        if (scrollTop + clientHeight >= scrollHeight){
            content.innerHTML += errorElement;
            requestAnimationFrame(() => {
                window.scrollTo(0, document.body.scrollHeight)
            })
        } else {
            content.innerHTML += errorElement;
        }
        
    }

    function removeErrorMessage() {
        const errorMessage = document.getElementById("error-message");
        if (errorMessage) errorMessage.remove();
    }

    function hideSuggestions() {
        suggestions.style.display = 'none';
    }

    function removeHeroSection() {
        if (heroSection) {
            heroSection.remove()
            document.body.style.overflowY = 'auto';
        }
    }

    function showScrollButton() {
        scrollButton.style.display = 'flex';
        setTimeout(() => scrollButton.classList.add('visible'), 10);
    }

    function hideScrollButton() {
        scrollButton.classList.remove('visible');
        setTimeout(() => scrollButton.style.display = 'none', 300);
    }

    function appendMessageAndScroll(role, message) {
        const scrollTop = document.documentElement.scrollTop
        const clientHeight =  document.documentElement.clientHeight
        const scrollHeight = document.documentElement.scrollHeight
        if (scrollTop + clientHeight >= scrollHeight){
            content.appendChild(createMessageElement(role, message));
            requestAnimationFrame(() => {
                window.scrollTo(0, document.body.scrollHeight)
            })
        } else {
            content.appendChild(createMessageElement(role, message));
        }
    }

    // Event Listeners
    suggestionBoxes.forEach(box => {
        box.addEventListener("click", () => {
            sendMessage(box.querySelector('.suggestion-text').textContent);
        });
    });

    submitBtn.addEventListener("click", () => sendMessage());

    messageInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey && !submitBtn.disabled) {
            e.preventDefault();
            sendMessage();
        }
    });

    scrollButton.addEventListener("click", () => {
        window.scrollTo({
            top: document.documentElement.scrollHeight,
            behavior: 'smooth'
        });
    });

    notification.addEventListener('click', () => {
        window.scrollTo({
            top: document.documentElement.scrollHeight,
            behavior: 'smooth'
        });
        hideNotification();
    });

    window.addEventListener('scroll', checkScroll);
    window.addEventListener('resize', checkScroll);

    // Initialization
    manageHeroSection();
    initializeTextArea(messageInput);
    checkScroll();
});