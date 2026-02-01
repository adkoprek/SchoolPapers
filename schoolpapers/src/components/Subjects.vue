<script setup lang="ts">
import { watch, onMounted } from 'vue';
import { RouterLink } from 'vue-router';

const props = defineProps({
    subjects: {
        type: Array<{ subject: string; logo: string }>,
        required: true
    }
});
</script>

<template>
    <main class="flex-1">
        <div class="flex max-w-4/5 mx-auto px-6 justify-center">
            <div class="grid flex-wrap gap-8 w-fit grid-cols-4">
                <RouterLink :to="`/subject/${subject.subject.toLocaleLowerCase()}`" v-for="subject in subjects" :key="subject.subject"
                    class="group flex items-center gap-8
                        bg-white rounded-3xl p-8
                        border border-gray-100
                        shadow-sm
                        hover:shadow-xl
                        transition-all duration-300
                        cursor-pointer min-w-85">
                    <div class="flex items-center justify-center
                            min-w-24 min-h-24 rounded-2xl
                            bg-gray-100 group-hover:bg-gray-200
                            transition-colors">

                        <img :src="subject.logo"
                            class="w-14 h-14 object-contain"
                            alt="logo"/>
                    </div>

                    <p class="text-2xl font-semibold text-gray-800">
                    {{ subject.subject }}
                    </p>
                </RouterLink>
            </div>
        </div>
    </main>
</template>