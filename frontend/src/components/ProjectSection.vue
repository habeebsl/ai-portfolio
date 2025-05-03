<script setup>
import ProjectCard from './ProjectCard.vue';

const descriptions = {
    translator: `
    This is my latest project, offering multilingual real-time transcription of audio data, as well as real-time translation into multiple languages. Additionally, users can play back the translated text in a natural and intuitive human-like voice.

    It leverages:

    - OpenAI's Whisper-1 model for audio transcription
    - OpenAI's TTS-1 model for generating speech from translated text
    - GPT-4o Mini for verifying transcribed text
    - DeepL for text translation
    `,

    keypoint: `
    Keypoint is a web app that extracts and highlights the most critical information from a text. It identifies key sentences, paragraphs, and terms, and provides Wikipedia-based tooltips for important words, allowing users to access more information instantly. The app also includes a redirect link to the relevant Wikipedia page for further exploration.  

    This project leverages Google’s Gemini-1.5-Pro model for its cutting-edge NLP capabilities. I also used PostgreSQL for session-based storage.  

    I created Keypoint as a productivity tool for students, researchers, and professionals who need to quickly extract insights from dense texts. Its utility lies in helping users absorb information efficiently without reading through the entire document.  

    - Challenges: Determining which parts of the text to highlight required extensive trial and error to balance contextual accuracy and user expectations.  
    - Outcome: This tool is particularly useful for researchers managing large volumes of information.  
    `
}
</script>

<template>
    <div class="container">
        <ProjectCard 
            class="fade-in"
            projectName="KeyPoint"
            description="Highlights the key contents of documents"
            link="https://keypoint-coral.vercel.app/"
            githubLink="https://github.com/habeebsl/keypoint"
            videoLink="https://drive.google.com/file/d/1qWoG1yyhYIEKWkIdAHjFYKooixFEyzP4/preview"
            thumbnail="/images/keypoint_thubnail2.png"
            :fullDescription="descriptions.keypoint"
        />
        <ProjectCard 
            class="fade-in"
            projectName="AI Translator"
            description="Enables real-time, multilingual translation"
            link="https://ai-translator-beryl.vercel.app/"
            githubLink="https://github.com/habeebsl/ai-translator"
            videoLink="https://www.loom.com/embed/ab7bb5645b234762b2abd23d1cb12c6b?sid=cb4f657c-6d51-44c7-848f-3e21ea212d5e"
            thumbnail="/images/translator.png"
            :fullDescription="descriptions.translator"
        />
    </div>
</template>

<style scoped>
.container {
    display: flex;
    justify-content: flex-start;
    gap: 40px;
    height: auto;
}

@media (max-width: 768px) {
    .container {
        flex-direction: column;
    }
}
</style>