<template>
     
    <div class="container mx-auto flex flex-wrap py-6">
        <!-- Posts Section -->
        <section class="w-full md:w-2/3 flex flex-col items-center px-3">

            <article class="flex flex-col shadow my-4">
                <!-- Article Image -->
                <a href="#" class="hover:opacity-75">
                    <img src="https://source.unsplash.com/collection/1346951/1000x500?sig=1">
                </a>
                <div class="bg-white flex flex-col justify-start p-6">
                    <!-- category -->
                    {{article.categoris}}
                    <a v-for="category in article.category" :key="category.id" class="text-blue-700 text-sm font-bold uppercase pb-4">{{category.title}}</a>
                    <!-- title -->
                    <a href="#" class="text-3xl font-bold hover:text-gray-700 pb-4">{{article.title}}</a>
                    <!-- content -->
                    <p>{{article.content}}</p>
                </div>
            </article>
            

            <!-- Pagination -->
            <div class="flex items-center py-8">
                <a href="#" class="h-10 w-10 bg-blue-800 hover:bg-blue-600 font-semibold text-white text-sm flex items-center justify-center">1</a>
                <a href="#" class="h-10 w-10 font-semibold text-gray-800 hover:bg-blue-600 hover:text-white text-sm flex items-center justify-center">2</a>
                <a href="#" class="h-10 w-10 font-semibold text-gray-800 hover:text-gray-900 text-sm flex items-center justify-center ml-3">Next <i class="fas fa-arrow-right ml-2"></i></a>
            </div>

        </section>

       <SideBar/>
    </div>
</template>
<script setup>
import SideBar from "src/components/SideBar.vue";
import { usePostsStore } from "src/stores/posts";
import { onMounted } from "vue";

const store = usePostsStore()
const article = store.Article
console.log('inside article');
console.log(article);

</script>