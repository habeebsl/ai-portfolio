<script setup>
</script>

<template>
    <div class="btn-container">
        <slot></slot>
    </div>
</template>


<style scoped>
.btn-container {
    display: flex;
    padding: 7px 15px;
    align-items: center;
    background-color: rgba(128, 128, 128, 0.2);
    gap: 6px;
    font-size: 12px;
    font-weight: 500;
    border-radius: 6px;
    transition: all 0.1s ease-in;
}

.btn-container:hover {
    transform: scale(1.1);
}
</style>