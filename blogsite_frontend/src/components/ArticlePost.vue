<template>
  <article class="flex flex-col shadow my-4">
                <a href="#" class="hover:opacity-75">
                    <img src="https://source.unsplash.com/collection/1346951/1000x500?sig=1">
                </a>
                <p>id : {{article.id}}</p>
                <div class="bg-white flex flex-col justify-start p-6">
                    <div class="flex-col pb-3">
                        <a v-for="category in  article.categories" :key="category.id" href="#" class="text-blue-700 text-sm font-bold uppercase pr-4">{{category.title}}</a>
                    </div>
                    
                    <a href="#" class="text-3xl font-bold hover:text-gray-700 pb-4">{{article.title}}</a>
                    <router-link @click="store.getPostAction(article.id)" :to="{name:'article',params:{id:article.id}}">to article page</router-link>
                    <a href="#" class="mb-2 line-clamp-2">{{article.content}}</a>
                    
                    <a href="#" class="uppercase text-gray-800 hover:text-black">Continue Reading <i class="fas fa-arrow-right"></i></a>
                </div>
            </article>
</template>
<script setup>
import { usePostsStore } from "src/stores/posts";
const store = usePostsStore()

const post = defineProps({
    article: Object,
})


</script>