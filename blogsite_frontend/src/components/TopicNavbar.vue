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
                    <router-link  :to="{name:'addCategory'}">
                        <button class="uppercase text-gray-800 hover:text-black  p-4">
                            Add category
                        </button>
                        
                    </router-link>
                    <router-link  :to="{name:'allCategories'}">
                        <button class="uppercase text-gray-800 hover:text-black  p-4">
                            All categories
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
