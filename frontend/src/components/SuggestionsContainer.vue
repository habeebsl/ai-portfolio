<script setup>

</script>

<template>
    <div class="prompt-suggestions">
        <slot></slot>
    </div>
</template>

<style scoped>
.prompt-suggestions {
    max-width: 1000px;
    margin: 0 auto 16px auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 12px;
}
</style>
