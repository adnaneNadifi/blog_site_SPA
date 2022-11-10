<template>
<!-- Topic Nav -->
<nav class="w-full py-4 border-t border-b bg-gray-100" x-data="{ open: false }">
        <div >
            <div class="w-full container mx-auto flex flex-col sm:flex-row items-center justify-center text-sm font-bold uppercase mt-0 px-6 py-2">
                <router-link  :to="{name:'home'}">
                        <button class="uppercase text-gray-800 hover:text-black  p-4">
                            Home
                        </button>
                        
                    </router-link>

                    <router-link  v-for="categorie in postsStore.categories.results" :key="categorie.id" :to="{name:'category',params:{id:categorie.id}}">
                        <button class="uppercase text-gray-800 hover:text-black  p-4">
                            {{categorie.title}}
                        </button>
                        
                    </router-link>
                
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
