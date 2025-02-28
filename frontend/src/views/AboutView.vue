<script setup>
import portrait from '@/assets/images/portrait1.jpeg'
</script>

<template>
    <div class="about-page">
        <div class="about-content">
            <h1>About <span class="gradient-text">Me</span></h1>
            
            <div class="about-grid">
                <div class="about-text">
                    <p>Hi, I'm Habeeb Salami, a passionate software developer that is dedicated to developing breakthrough AI solutions and apps. I thrive on coding challenges and enjoy transforming ideas into tangible products. Beyond the screen, I enjoy researching upcoming technologies, contributing to open-source projects, and sharing expertise with other developers.</p>
                    <p>Since starting my tech journey in 2022, I’ve been privileged to work on exciting projects that push boundaries and solve real-world problems. I'm a firm believer in continuous learning and embracing the dynamic nature of technology to drive meaningful change.</p>
                    <p>When I’m not immersed in code, I enjoy reading, playing chess, and shooting hoops on the basketball court. I’m always eager to connect with like-minded individuals and explore opportunities for collaboration.</p>
                </div>
                
                <div class="about-image-container">
                    <div class="glow-effect"></div>
                    <img :src="portrait" alt="Habeeb Salami" class="about-image">
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
body {
    overflow-y: hidden;
}

.about-page {
    max-width: 1000px;
    margin: 0px auto;
    margin-top: 70px;
    padding: 0 24px;
}

.about-content h1 {
    font-size: 48px;
    font-weight: 600;
    margin-bottom: 0;
}

.about-grid {
    display: grid;
    grid-template-columns: 3fr 2fr;
    gap: 60px;
    align-items: start;
}

.about-text p {
    font-size: 16px;
    line-height: 1.8;
    color: var(--text-secondary);
    margin-bottom: 24px;
}

.about-image-container {
    position: relative;
}

.about-image {
    width: 90%;
    border-radius: 24px;
    position: relative;
    z-index: 2;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.glow-effect {
    position: absolute;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    filter: blur(100px);
    opacity: 0.12;
    z-index: 1;
}

@media (max-width: 768px) {
    body {
        overflow-y: auto;
    }
    
    .about-page {
        margin: 0px auto;
        margin-bottom: 40px;
    }

    .about-content h1 {
        font-size: 36px;
    }

    .about-grid {
        grid-template-columns: 1fr;
        gap: 30px;
    }

    .about-text p {
        font-size: 15px;
    }
}
</style>