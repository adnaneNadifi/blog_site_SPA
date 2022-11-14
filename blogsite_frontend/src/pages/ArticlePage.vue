<template>
  <div class="container mx-auto flex flex-wrap py-6">
    <!-- Posts Section -->

    <section class="w-full md:w-2/3 flex flex-col items-center px-3">
      <article class="flex flex-col shadow my-4">
        <!-- Article Image -->
        <a href="#" class="hover:opacity-75">
          <img
            src="https://source.unsplash.com/collection/1346951/1000x500?sig=1"
          />
        </a>
        <div class="bg-white flex flex-col justify-start p-6">
          <!-- category -->
          <a
            v-for="category in article.display_categories"
            :key="category.id"
            class="text-blue-700 text-sm font-bold uppercase pb-4"
            >{{ category.title }}</a
          >
          <!-- title -->
          <a href="#" class="text-3xl font-bold hover:text-gray-700 pb-4">{{
            article.title
          }}</a>
          <!-- content -->
          <p>{{ article.content }}</p>
        </div>
      </article>
      <AddCommentForm />
      <CommentSection :comments="article.comments" />
    </section>

    <SideBar />
  </div>
</template>
<script setup lang="ts">
import SideBar from 'src/components/SideBar.vue';
import CommentSection from 'src/components/CommentSection.vue';
import AddCommentForm from 'src/components/AddCommentFom.vue';
import { usePostsStore } from 'src/stores/posts';
import { useRoute } from 'vue-router';
import { ref, onBeforeMount } from 'vue';
import { getArticle } from 'src/services/articles/api';

const route = useRoute();
const article = ref({} as API.Article);

onBeforeMount(async () => {
  const id = parseInt(route.params.id as string);
  await getArticle(id).then((res) => {
    article.value = res.data;
  });
});
</script>
