<script setup>
import ContactCard from '@/components/ContactCard.vue';
</script>

<template>
    <div class="contact-page">
        <div class="contact-header">
            <h1>Let's <span class="gradient-text">Connect</span></h1>
            <p class="subtitle">I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision.</p>
        </div>
        <div class="contact-grid">
            <ContactCard
                link="mailto:habeebsalami09@email.com"
                title="Email"
                linkText="habeebsalami09@email.com"
            >
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                    <polyline points="22,6 12,13 2,6"/>
                </svg>
            </ContactCard>
            <ContactCard
                link="https://www.linkedin.com/in/habeeb-salami-688870290"
                title="LinkedIn"
                linkText="linkedin.com/in/habeeb-salami-688870290"
            >
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>
                    <rect x="2" y="9" width="4" height="12"/>
                    <circle cx="4" cy="4" r="2"/>
                </svg>
            </ContactCard>
            <ContactCard
                link="https://github.com/habeebsl"
                title="GitHub"
                linkText="github.com/habeebsl"
            >
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
                </svg>
            </ContactCard>
            <ContactCard
                link="https://x.com/habeebslm"
                title="X (Twitter)"
                linkText="@habeebslm"
            >
                <svg width="24" height="24" viewBox="0 0 1200 1227" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M714.163 519.284L1160.89 0H1055.03L667.137 450.887L357.328 0H0L468.492 681.821L0 1226.37H105.866L515.491 750.218L842.672 1226.37H1200L714.137 519.284H714.163ZM569.165 687.828L521.697 619.934L144.011 79.6944H306.615L611.412 515.685L658.88 583.579L1055.08 1150.3H892.476L569.165 687.854V687.828Z" fill="white"/>
                </svg>
            </ContactCard>
        </div>
    </div>
</template>

<style scoped>
.contact-page {
    max-width: 1000px;
    margin: 0px auto;
    margin-top: 70px;
    margin-bottom: 38px;
    padding: 0 24px;
}

.contact-header {
    text-align: center;
    margin-bottom: 60px;
}

.contact-header h1 {
    font-size: 48px;
    font-weight: 600;
    margin-bottom: 20px;
}

.subtitle {
    color: var(--text-secondary);
    font-size: 18px;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
}

.contact-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 24px;
    margin-top: 40px;
}

@media (max-width: 768px) {
    .contact-page {
        margin: 19px auto;
    }

    .contact-header h1 {
        font-size: 36px;
    }

    .subtitle {
        font-size: 16px;
    }

    .contact-grid {
        gap: 16px;
    }
}
</style>