import { defineStore } from 'pinia';
import { ref } from "vue";
import {getArticles , getCategories} from 'src/services/articles/api'
/* export const usePostsStore = defineStore('posts', () => {
  const posts = ref([])
  
  function getPostsData() {
    getArticles()
        .then((response) => {
          posts.value = response.data
          console.log(posts.value);
          
        })
        .catch((err) => {
          console.log(err);
          
        })
  } 
  
  return { posts ,getPostsData}
}) */

export const usePostsStore = defineStore('posts', {
  state: () => {
    return {
      posts:[] as API.ArticleData,
      categories:[] as API.CategoryData
      
    };
  },
  actions: {
    getPostsAction() {
      getArticles()
          .then((response) => {
            this.posts =  response.data
          })
          .catch((err) => {
            console.log(err);
          })
    } ,

    getCategoriesAction() {
      getCategories()
          .then((response) => {
            this.categories =  response.data
          })
          .catch((err) => {
            console.log(err);
          })
    } 
  },
});
