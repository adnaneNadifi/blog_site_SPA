import { defineStore } from 'pinia';
import { ref } from "vue";
import {getArticles , getCategories} from 'src/services/articles/api'
import { api } from 'src/boot/axios';
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
      Article:{} as API.Article,
      categories:[] as API.CategoryData
    };
  },

  actions: {
    async getPostsAction() {
      const response = await getArticles()
          .then((response) => {
            this.posts =  response.data
          })
          .catch((err) => {
            console.log(err);
          })
      return response;
    },
    getPostAction(id:number){
      
    
      const articles = this.posts
      const result = articles.find(article => article.id == id);
      this.Article = result;
      console.log(this.Article);
    },
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
