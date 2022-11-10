import { defineStore } from 'pinia';
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
      posts:{
        count: 0,
        previous: null,
        next:null,
        results : [],
      } as API.ArticleData,
      categories:{} as API.CategoryData
    };
  },

  actions: {
    async getPostsAction(getNextPage=false) {

      let pageUrl = null;
      if (getNextPage){
        pageUrl = this.posts.next;
      }

      const response = await getArticles(pageUrl)
          .then((response) => {
            this.posts =  {
              ...this.posts,
              next: response.data.next,
              previous: response.data.previous,
              results: [
                ...this.posts.results,
                ...response.data.results
              ],
            }
          })
          .catch((err) => {
            console.log(err);
          })
      return response;
    },

    getPostAction(id:number){
      const articles = this.postsapp.css
      const result = articles.find(article => article.id == id);
      return result;
    },

    async getCategoriesAction() {
      const response = await getCategories()
          .then((response) => {
            this.categories =  response.data
          })
          .catch((err) => {
            console.log(err);
          })
          return response;
    } 

  },
});
