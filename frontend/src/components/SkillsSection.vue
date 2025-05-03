<script setup>
import SkillCard from './SkillCard.vue';
import HTML from './skills/HTML.vue';
import CSS from './skills/CSS.vue';
import Javascript from './skills/Javascript.vue';
import Typescript from './skills/Typescript.vue';
import Python from './skills/Python.vue';
import Node from './skills/Node.vue';
import Vue from './skills/Vue.vue';
import React from './skills/React.vue';
import Pinia from './skills/Pinia.vue';
import Vite from './skills/Vite.vue';
import Tailwind from './skills/Tailwind.vue';
import Flask from './skills/Flask.vue';
import Django from './skills/Django.vue';
import Fastapi from './skills/Fastapi.vue';
import Postman from './skills/Postman.vue';
import Redis from './skills/Redis.vue';
import Postgres from './skills/Postgres.vue';
import MySQL from './skills/MySQL.vue';
import Docker from './skills/Docker.vue';
import AWS from './skills/AWS.vue';
import Langchain from './skills/Langchain.vue';
import Firebase from './skills/Firebase.vue';
import Supabase from './skills/Supabase.vue';
</script>

<template>
    <div class="skills-container">
        <div class="skills-wrapper">
            <SkillCard class="fade-in">
                <HTML className="skill-svg" />
                HTML
            </SkillCard>
            <SkillCard class="fade-in">
                <CSS className="skill-svg" />
                CSS
            </SkillCard>
            <SkillCard class="fade-in">
                <Javascript className="skill-svg" />
                Javascript
            </SkillCard>
            <SkillCard class="fade-in">
                <Typescript className="skill-svg" />
                Typescript
            </SkillCard>
            <SkillCard class="fade-in">
                <Python className="skill-svg" />
                Python
            </SkillCard>
            <SkillCard class="fade-in">
                <Node className="skill-svg" />
                Node.js
            </SkillCard>
            <SkillCard class="fade-in">
                <Vue className="skill-svg" />
                Vue
            </SkillCard>
            <SkillCard class="fade-in">
                <React className="skill-svg" />
                React
            </SkillCard>
            <SkillCard class="fade-in">
                <Pinia className="skill-svg" />
                Pinia
            </SkillCard>
            <SkillCard class="fade-in">
                <Vite className="skill-svg" />
                Vite
            </SkillCard>
            <SkillCard class="fade-in">
                <Tailwind className="skill-svg" />
                Tailwind
            </SkillCard>
            <SkillCard class="fade-in">
                <Flask className="skill-svg" />
                Flask
            </SkillCard>
            <SkillCard class="fade-in">
                <Django className="skill-svg" />
                Django
            </SkillCard>
            <SkillCard class="fade-in">
                <Fastapi className="skill-svg" />
                FastApi
            </SkillCard>
            <SkillCard class="fade-in">
                <Postman className="skill-svg" />
                Postman
            </SkillCard>
            <SkillCard class="fade-in">
                <Redis className="skill-svg" />
                Redis
            </SkillCard>
            <SkillCard class="fade-in">
                <Postgres className="skill-svg" />
                Postgres
            </SkillCard>
            <SkillCard class="fade-in">
                <MySQL className="skill-svg" />
                MySQL
            </SkillCard>
            <SkillCard class="fade-in">
                <Docker className="skill-svg" />
                Docker
            </SkillCard>
            <SkillCard class="fade-in">
                <AWS className="skill-svg" />
                AWS
            </SkillCard>
            <SkillCard class="fade-in">
                <Langchain className="skill-svg" />
                Langchain
            </SkillCard>
            <SkillCard class="fade-in">
                <Firebase className="skill-svg" />
                Firebase
            </SkillCard>
            <SkillCard class="fade-in">
                <Supabase className="skill-svg" />
                Supabase
            </SkillCard>
        </div>
    </div>
</template>

<style scoped>
.skills-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    width: 100%;
}

.skills-wrapper {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.skill-svg {
    width: 30px;
    height: 30px;
}
</style>