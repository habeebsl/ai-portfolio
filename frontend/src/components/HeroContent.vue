<script setup>
import HeroButtons from '@/components/HeroButtons.vue';
import { useMessage } from '@/stores/messageStore';

const promptEquivalent = {
    skills: "What are your skills?", 
    projects: "Can you provide an overview of your past projects and contributions?", 
    experiences: "Tell me about your work history and roles",
};

const messageStore = useMessage()

const handleClick = (event) => {    
    if (event.target.tagName === 'SPAN') {
        const key = event.target.innerText.toLowerCase();
        if (promptEquivalent[key]) {
            messageStore.currentUserMessage = promptEquivalent[key]
            messageStore.sendMessage = true
        }
    }
};
</script>

<template>
    <div class="hero-content">
        <div class="name-heading">Hey, I'm <span class="gradient-text">Habeeb Salami</span></div>
        <div class="role">Software Engineer | AI Solutions Developer</div>
        <h1>Experience my journey through <span class="gradient-text">interactive AI</span></h1>
        <p class="hero-text" @click="handleClick">
            Ask anything about my <span>skills</span>, <span>projects</span>, and <span>experiences</span>—or check out the <span><router-link to="/about" class="subtle-link">about page</router-link></span> for the TL;DR version
        </p>
        <HeroButtons />
    </div>
</template>

<style scoped>
.hero-content {
    position: relative;
    z-index: 2;
}

.name-heading {
    font-size: 24px;
    font-weight: 500;
    margin-top: 10px;
    margin-bottom: 8px;
}

.role {
    color: var(--primary-light);
    font-size: 18px;
    margin-bottom: 20px;
    font-weight: 500;
}

.hero-content h1 {
    font-size: 40px;
    line-height: 1.2;
    margin-bottom: 16px;
    font-weight: 600;
}

.hero-text {
    font-size: 16px;
    color: var(--text-secondary);
    line-height: 1.6;
    max-width: 400px;
}

.hero-text span {
    color: transparent;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    background-clip: text;
    font-weight: 600;
    position: relative;
    cursor: pointer;
    display: inline-block;
    transition: color 0.3s ease, background 0.3s ease;
}

.hero-text span::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -2px;
    width: 0;
    height: 2px;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary));
    transition: width 0.3s ease;
}

.hero-text span:hover::after {
    width: 100%;
}

.hero-text span:hover {
    background: linear-gradient(135deg, var(--primary-light), var(--accent));
    -webkit-background-clip: text;
    background-clip: text;
}

.subtle-link {
    text-decoration: none;
    color: transparent;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text;
    background-clip: text;
    font-weight: 600;
    position: relative;
    cursor: pointer;
    display: inline-block;
    transition: color 0.3s ease, background 0.3s ease;
}

.subtle-link span::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: -2px;
    width: 0;
    height: 2px;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary));
    transition: width 0.3s ease;
}

.subtle-link span:hover::after {
    width: 100%;
}

.subtle-link span:hover {
    background: linear-gradient(135deg, var(--primary-light), var(--accent));
    -webkit-background-clip: text;
    background-clip: text;
}

@media (max-width: 768px) {
    .name-heading {
        font-size: 20px;
    }
    
    .role {
        font-size: 16px;
    }

    .hero-content h1 {
        font-size: 32px;
    }
}

</style>