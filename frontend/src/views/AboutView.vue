<script setup>
import { onMounted, ref } from 'vue';
import Typed from 'typed.js';
import portrait from '@/assets/images/portrait1.jpeg'
import SkillsSection from '@/components/SkillsSection.vue';
import ProjectSection from '@/components/ProjectSection.vue';
import TimelineSection from '@/components/TimelineSection.vue';
import VideoDisplay from '@/components/VideoDisplay.vue';
import InfoDisplay from '@/components/InfoDisplay.vue'

const typedElement = ref(null);

const experiences = [
  {
    title: "Software Engineer Intern",
    company: "Comini Learning",
    duration: "2025 - Present",
    description:
      "Building Interesting games to make learning more interactive and fun for children",
  },
  {
    title: "Python Instructor",
    company: "Google Developer Student Club",
    duration: "2022 - 2023",
    description:
      "Trained over 20 students in Python programming, enabling them to launch careers in web development.",
  },
];

const education = [
  {
    title: "Bachelor of Science in Computer Science",
    subtitle: "Igbinedion University, Nigeria",
    duration: "2021 - 2026",
    description: "Notable coursework includes Data Structures, Algorithms, Database Systems, and Software Engineering. Maintained a 4.5 GPA.",
  }
];

onMounted(() => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.fade-in').forEach((el) => {
        observer.observe(el);
    });
});

onMounted(() => {
  const typed = new Typed(typedElement.value, {
    strings: ['Fullstack Developer.', 'Python Expert.', 'Backend Developer'],
    typeSpeed: 80,
    backSpeed: 40,
    startDelay: 500,
    backDelay: 1500,
    loop: true,
    showCursor: true,
    cursorChar: '|',
    smartBackspace: true,
    fadeOut: false,
  });

  return () => typed.destroy();
});
</script>

<template>
    <div class="about-page">
        <div class="about-content">
            <h1>I'm a <span class="gradient-text" ref="typedElement"></span></h1>
            
            <div class="about-grid">
                <div class="about-text">
                    <p>Hi, I'm Habeeb. I'm a problem solver, someone who genuinely enjoys solving complex problems and building cool stuff. Currently I'm doing so with web technologies but Web development is overrated, where I want to go is Robotics. I want to build robots and problem solving prosthetics that can better human lives and help people with unsolved health problems. It's really ambitious I know.</p>
                    <p>That being said, I will continue growing my skills until I can make that incredible transition. I've also taken a liking to AI, most of my projects are centered around it, nowadays. I even made it a part of my brand, because I know the potential AI has and that excites me. I'm even planning on going into AI/ML, which will eventually help me solve problems in robotics.</p>
                    <p>I'm looking to work with people who'll help me grow and in turn I will put in the best work imaginable. I'm independent but I love a good team. I mostly work remotely but I'm open to other options if they're feasible. And that's me</p>
                </div>
                
                <div class="about-image-container">
                    <div class="glow-effect"></div>
                    <img :src="portrait" alt="Habeeb Salami" class="about-image">
                </div>
            </div>
        </div>
        <div>
            <div class="title">Skills</div>
            <SkillsSection />
        </div>
        <div>
            <div class="title">Projects</div>
            <ProjectSection />
        </div>
        <div>
            <div class="title">Experience</div>
            <TimelineSection 
                :items="experiences"
            />
        </div>
        <div>
            <div class="title">Education</div>
            <TimelineSection 
                :items="education"
            />
        </div>
    </div>
    <VideoDisplay />
    <InfoDisplay />
</template>

<style scoped>
.about-page {
    display: flex;
    flex-direction: column;
    gap: 64px;
    max-width: 1000px;
    margin: 0px auto;
    margin-top: 70px;
    padding: 0 24px;
    margin-bottom: 100px;
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

.title {
    margin-bottom: 24px;
    font-weight: 600;        
}

@media (max-width: 768px) {
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