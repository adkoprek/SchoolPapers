<script setup lang="ts">
import Subjects from "@/components/Subjects.vue";
import Footer from "@/components/Footer.vue";
import physikLogo from "@/assets/physik.svg";
import biologieLogo from "@/assets/biologie.svg";
import chemieLogo from "@/assets/chemie.svg";
import geographieLogo from "@/assets/geographie.svg";
import geschichteLogo from "@/assets/geschichte.svg";
import wirtschaftLogo from "@/assets/wirtschaft.svg";

const subjects: Array<{ subject: string; logo: string }> = [
    {subject: "Physik",     logo: physikLogo    },
    {subject: "Biologie",   logo: biologieLogo  },
    {subject: "Chemie",     logo: chemieLogo    },
    {subject: "Geographie", logo: geographieLogo},
    {subject: "Geschichte", logo: geschichteLogo},
    {subject: "Wirtschaft", logo: wirtschaftLogo},
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