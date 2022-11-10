<template>
    <div class="container mx-auto flex flex-wrap py-6">
        <!-- Posts Section -->
        <section class="w-full md:w-2/3 flex flex-col items-center px-3">
            <div v-for="post in postsStore.posts.results" :key="post.id">
                <ArticlePost  :article="post" />
            </div>
            
            

            <!-- Pagination -->
            <div class="flex items-center py-8">
                <button v-if="postsStore.posts.next !== null"
                 @click="loadNextPage"
                 class="p-4 bg-blue-800 hover:bg-blue-600 font-semibold text-white text-sm flex items-center justify-center">
                    Load more
                </button>
            </div>

        </section>

       <SideBar/>
    </div>
</template>

<script setup lang="ts">

import SideBar from "src/components/SideBar.vue"
import ArticlePost from "src/components/ArticlePost.vue"
import { usePostsStore } from "src/stores/posts";
import { onBeforeMount } from "vue";

const postsStore = usePostsStore();



onBeforeMount(async () => {
    postsStore.getPostsAction(false);
})

const loadNextPage = () => {
    if(postsStore.posts.next !== null){
        postsStore.getPostsAction(true);
    }
    
}

</script>
