<script setup lang="ts">
import Subjects from "@/components/Subjects.vue";
import Footer from "@/components/Footer.vue";


const subjects: Array<{ subject: string; logo: string }> = [
    {subject: "Physik",     logo: "/logos/physik.svg" },
    {subject: "Biologie",   logo: "/logos/biologie.svg" },
    {subject: "Chemie",     logo: "/logos/chemie.svg" },
    {subject: "Geographie", logo: "/logos/geographie.svg" },
    {subject: "Geschichte", logo: "/logos/geschichte.svg" },
    {subject: "Wirtschaft", logo: "/logos/wirtschaft.svg" },
]; 
</script>

<template>
    <div class="min-h-screen flex flex-col bg-gray-50">
        <header class="py-16 text-center">
            <h1 class="text-5xl md:text-7xl font-extrabold tracking-tight text-gray-800">
                School Papers
            </h1>
        </header>

        <Subjects :subjects="subjects" />
        <Footer />
    </div>
</template>