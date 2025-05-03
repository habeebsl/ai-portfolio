<template>
    <button class="action-button">
        <slot></slot>
    </button>
</template>

<style>
.action-button {
  padding: 4px;
  padding-top: 2px;
  padding-bottom: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.action-button:hover {
  transform: scale(1.1);
  background: linear-gradient(
    to bottom right,
    var(--primary),
    var(--secondary)
  );
}

.action-button:hover svg path {
  fill: #000000;
}
</style>