<template>

<h1 class="text-5xl font-bold mt-10 mb-6">{{category.title}}</h1>
    <section class="w-full gap-4 lg:grid grid-cols-3 items-center px-3">


        <article v-for="article in category.posts" :key="article.id"
         class="flex flex-col shadow my-4">
        <!-- Article Image -->
        <a href="#" class="hover:opacity-75">
            <img src="https://source.unsplash.com/collection/1346951/1000x500?sig=1">
        </a>
        <div class="bg-white flex flex-col justify-start p-6">
            <a href="#" class="text-blue-700 text-sm font-bold uppercase pb-4">{{category.title}} </a>
            <a href="#" class="text-3xl font-bold hover:text-gray-700 pb-4">{{article.title}}</a>
            <a href="#" class="pb-6">{{article.content.substring(0,100)}}</a>
            <a href="#" class="uppercase text-gray-800 hover:text-black">Continue Reading </a>
        </div>
        </article>

     
    </section>
</template>
<script setup lang="ts">
import { getCategoryWithArticles } from 'src/services/articles/api';
import { onBeforeMount, ref } from 'vue';
import { onBeforeRouteUpdate, useRoute } from "vue-router";

const route = useRoute();

const category = ref({} as API.CategoryWithArticles)

async function loadCategory(id:number) {
    await getCategoryWithArticles(id).then((res)=>{
        category.value = res.data;
    })
}


onBeforeMount(async () => {
    const categoryId = parseInt(route.params.id as string);
    loadCategory(categoryId)
})


onBeforeRouteUpdate(async (to, from)=>{
    const categoryId = parseInt(to.params.id as string);
    loadCategory(categoryId)
})

</script>