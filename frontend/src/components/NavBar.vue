<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
  <nav class="navbar">
    <div class="navbar-content">
      <div class="navbar-logo">Habeeb Salami</div>
      <div class="navbar-links">
        <RouterLink 
          to="/" 
          class="nav-item" 
          active-class="active"
          exact
        >
          Home
        </RouterLink>
        <RouterLink 
          to="/about" 
          class="nav-item" 
          active-class="active"
        >
          About
        </RouterLink>
        <RouterLink 
          to="/contact" 
          class="nav-item" 
          active-class="active"
        >
          Contact
        </RouterLink>
        <a 
          href="https://drive.usercontent.google.com/u/0/uc?id=1gbS64L1dpQm67Xz6yZoaK6Yy9SfCpK18&export=download" 
          class="nav-item" 
          download
        >
          Get Resume
        </a>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 40px;
    background: var(--background);
    padding: 8px 0;
    z-index: 1000;
    border-bottom: none;
}

.navbar::after {
    content: '';
    position: absolute;
    bottom: -10px;
    left: 0;
    width: 100%;
    height: 20px;
    background: linear-gradient(to bottom, var(--background), transparent);
    pointer-events: none;
}

.navbar-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 24px;
}

.navbar-logo {
    font-size: 18px;
    font-weight: 700;
    color: var(--primary-light);
    background: linear-gradient(135deg, var(--primary-light), var(--secondary));
    -webkit-background-clip: text;
    background-clip: text;
    text-transform: uppercase;
}

/* Navbar Links */
.navbar-links {
    display: flex;
    gap: 16px;
}

.nav-item {
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 12px;
    color: var(--text-secondary);
    position: relative;
    transition: color 0.3s ease;
    text-transform: uppercase;
}

.nav-item:hover,
.nav-item.active {
    color: transparent;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary));
    -webkit-background-clip: text;
    background-clip: text;
}

.nav-item::after {
    content: '';
    position: absolute;
    left: 0;
    bottom: 0;
    width: 0;
    height: 2px;
    background: linear-gradient(135deg, var(--primary-light), var(--secondary));
    transition: width 0.3s ease;
}

.nav-item:hover::after,
.nav-item.active::after {
    width: 100%;
}

@media (max-width: 768px) {
    .navbar-content {
        padding: 0 16px;
    }

    .navbar-logo {
        display: none;
    }

    .navbar-links {
        width: 100%;
        justify-content: space-around;
        gap: 0;
    }

    .nav-item {
        font-size: 12px;
        padding: 6px 12px;
    }
}
</style>