<script setup lang="ts">
import Footer from "@/components/Footer.vue";
import subjects from "@/assets/subjects.json";
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import router from "@/router";

type subjectsKeys = keyof typeof subjects;

const route = useRoute();

const title = ref(route.params.title as string);
const logo = ref<string>("");
const items = ref<Array<string>>([]);

onMounted(() => setContent());
watch(() => route.params.title, () => setContent());

async function setContent() {
    const newParam = route.params.title as string;

    if (!(newParam in subjects)) {
        router.replace('/not-found');
        return;
    }
    const subjectData = subjects[newParam as subjectsKeys];
    title.value = subjectData.title;
    logo.value = subjectData.logo;
    items.value = subjectData.items;
}
</script>

<template>
  <div class="flex flex-col min-h-screen relative">
    <header class="relative">
      <button @click="$router.back()" 
            class="absolute top-4 left-4 flex items-center gap-2 text-gray-700 hover:text-gray-900
               bg-gray-100 hover:bg-gray-200 px-3 py-1.5 rounded-lg font-medium
               shadow-sm hover:shadow transition-all duration-200 z-10">
        <span class="text-lg">←</span>
        <span>Back</span>
      </button>

      <div class="flex justify-center items-center gap-6 pt-24 pb-5 sm:py-12">
        <img :src="logo" class="sm:w-28 sm:h-28 w-15 h-15 object-contain" />
        <h1 class="sm:text-5xl text-4xl font-semibold text-gray-800">
          {{ title }}
        </h1>
      </div>
    </header>

    <main class="flex-1">
      <div class="max-w-6xl mx-auto px-6 mt-15">
        <div class="grid place-items-center grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <button
            v-for="item in items"
            :key="item"
            class="group w-full max-w-sm flex items-center justify-between
                   px-6 py-4 rounded-2xl border border-gray-200
                   bg-[#fdfdfd] hover:shadow-md transition-all duration-200"
          >
            <span class="text-lg font-semibold text-gray-800 text-center flex-1">
              {{ item }}
            </span>
            <span class="ml-3 text-white group-hover:text-gray-700 group-hover:translate-x-1 transition">
              →
            </span>
          </button>
        </div>
      </div>
    </main>

    <Footer />
  </div>
</template>