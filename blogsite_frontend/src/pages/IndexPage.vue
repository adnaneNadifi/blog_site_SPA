<template>
  <div class="container mx-auto flex flex-wrap py-6">
    <!-- Posts Section -->
    <section class="w-full md:w-2/3 flex flex-col items-center px-3">
      <!-- add article model -->
      <q-btn
        label="Add article"
        icon-right="add"
        color="primary"
        @click="addArticleModel = true"
      />
      <q-dialog v-model="addArticleModel" persistent>
        <q-card style="min-width: 350px">
          <q-card-section>
            <div class="text-h6">Add article</div>
          </q-card-section>
          <q-card-section class="q-pt-none">
            <q-form ref="addArticleForm" @reset="resetArticleForm">
              <q-input
                v-model="article.title"
                type="text"
                label="Add article title"
                :rules="[
                  (val) => (val && val.length > 0) || 'Please type something',
                ]"
              />
              <q-input
                v-model="article.content"
                type="textarea"
                label="Add article content"
              />
              <q-select
                v-model="article.categories"
                :options="allCategories"
                multiple
                emit-value
                map-options
                label="Choose category"
                filled
              />
              <div class="mt-2">
                <q-btn flat @click="validateArticleForm" label="Add Article" />
                <q-btn flat type="reset" label="reset" />
                <q-btn
                  flat
                  @click="addArticleModel = false"
                  label="cancel"
                  v-close-popup
                />
              </div>
            </q-form>
          </q-card-section>
        </q-card>
      </q-dialog>
      <div v-for="post in postsStore.posts.results" :key="post.id">
        <!-- articles -->
        <ArticlePost :article="post" />
      </div>

      <!-- Pagination -->
      <div class="flex items-center py-8">
        <button
          v-if="postsStore.posts.next !== null"
          @click="loadNextPage"
          class="p-4 bg-blue-800 hover:bg-blue-600 font-semibold text-white text-sm flex items-center justify-center"
        >
          Load more
        </button>
      </div>
    </section>

    <SideBar />
  </div>
</template>

<script setup lang="ts">
import SideBar from 'src/components/SideBar.vue';
import ArticlePost from 'src/components/ArticlePost.vue';
import { usePostsStore } from 'src/stores/posts';
import { onBeforeMount, ref } from 'vue';
import { getAllCategories, addArticle } from 'src/services/articles/api';

const postsStore = usePostsStore();
const addArticleModel = ref<boolean>(false);
const addArticleForm = ref(null);
const article = ref<API.ArticleForm>({
  title: '',
  content: '',
  categories: [],
});

const allCategories = ref<string[]>([]);

onBeforeMount(async () => {
  if (postsStore.first_time_load) {
    postsStore.getPostsAction(false);
  }
  getAllCategories().then((res) => {
    allCategories.value = res.data.map((cat) => {
      return {
        label: cat.title,
        value: cat.id,
      };
    });
    /* console.log(res.data);
      console.log(res.data.map((cat) => cat.title)); */
  });
});

const loadNextPage = () => {
    if(postsStore.posts.next !== null){
        postsStore.getPostsAction(true);
    }
    
}

function validateArticleForm() {
  addArticleForm.value.validate().then((success) => {
    if (success) {
      /* const static_data = {
        title: 'static title',
        content: 'static title',
        categories: [
          {
            title: 'food',
          },
        ],
      }; */
      addArticle(article.value).then((res) => {
        console.log(res);
      });
      /* console.log('static data');
      console.log(static_data); */
    } else {
      console.log('form error');
    }
  });
}

// to reset validations:
function resetArticleForm() {
  console.log('RESET');
  addArticleForm.value.resetValidation();
  article.value = {
    title: '',
    content: '',
    categories: [
      {
        title: '',
      },
    ],
  };
}
</script>
