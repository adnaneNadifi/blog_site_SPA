<template>
<!-- Topic Nav -->
<nav class="w-full py-4 border-t border-b bg-gray-100" x-data="{ open: false }">
        <div class="block sm:hidden">
            <a
                href="#"
                class="block md:hidden text-base font-bold uppercase text-center flex justify-center items-center"
            >
                Topics <i  class="fas ml-2"></i>
            </a>
        </div>
        <div >
            <div class="w-full container mx-auto flex flex-col sm:flex-row items-center justify-center text-sm font-bold uppercase mt-0 px-6 py-2">
                <div v-for="categorie in postsStore.categories" :key="categorie.id">
                    <a href="" class="hover:bg-gray-400 rounded py-2 px-4 mx-2 ">{{categorie.title}}</a>
                </div>
                
            </div>
        </div>
    </nav>
</template>

<script setup lang="ts">

import { usePostsStore } from "src/stores/posts";
import { onBeforeMount } from "vue";

const postsStore = usePostsStore()


onBeforeMount(() => {
    postsStore.getCategoriesAction();
})

</script>
