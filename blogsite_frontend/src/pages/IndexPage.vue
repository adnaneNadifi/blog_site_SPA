<template>
    <MainNavbar/>
    <TopicNavbar/>
    <div class="container mx-auto flex flex-wrap py-6">
        <!-- Posts Section -->
        <section class="w-full md:w-2/3 flex flex-col items-center px-3">

            <div v-for="post in postsStore.posts" :key="post.id">
                <ArticlePost  :article="post" />
            </div>
            


            <!-- Pagination -->
            <div class="flex items-center py-8">
                <a href="#" class="h-10 w-10 bg-blue-800 hover:bg-blue-600 font-semibold text-white text-sm flex items-center justify-center">1</a>
                <a href="#" class="h-10 w-10 font-semibold text-gray-800 hover:bg-blue-600 hover:text-white text-sm flex items-center justify-center">2</a>
                <a href="#" class="h-10 w-10 font-semibold text-gray-800 hover:text-gray-900 text-sm flex items-center justify-center ml-3">Next <i class="fas fa-arrow-right ml-2"></i></a>
            </div>

        </section>

       <SideBar/>
    </div>
    <MainFooter/>
</template>

<script setup lang="ts">
import MainNavbar from "src/components/MainNavbar.vue";
import TopicNavbar from "src/components/TopicNavbar.vue";
import MainFooter from "src/components/MainFooter.vue";
import SideBar from "src/components/SideBar.vue"
import ArticlePost from "src/components/ArticlePost.vue"
import { usePostsStore } from "src/stores/posts";
import { onBeforeMount } from "vue";

const postsStore = usePostsStore()


onBeforeMount(() => {
    postsStore.getPostsAction();
})

</script>
