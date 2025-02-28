<script setup>
defineProps({
    link: String,
    title: String,
    linkText: String
})
</script>

<template>
    <a :href="link" class="contact-card" target="_blank">
        <div class="card-icon">
            <slot></slot>
        </div>
        <h3>{{ title }}</h3>
        <p>{{ linkText }}</p>
    </a>
</template>

<style>
.contact-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    text-decoration: none;
    color: var(--text);
    transition: all 0.3s ease;
}

.contact-card:hover {
    transform: translateY(-5px);
    background: rgba(255, 255, 255, 0.05);
    border-color: rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.2);
}

.card-icon {
    width: 60px;
    height: 60px;
    margin: 0 auto 20px;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.card-icon svg {
    stroke: white;
}

.contact-card h3 {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
}

.contact-card p {
    color: var(--text-secondary);
    font-size: 15px;
}

@media (max-width: 768px) {
    .contact-card {
        padding: 24px;
    }
}
</style>