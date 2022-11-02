import { defineStore } from 'pinia';
import { ref } from "vue";
import  axios  from "axios";
export const usePostsStore = defineStore('posts', () => {
  const posts = ref([])
  
  function getPostsData() {
    axios
      .get('http://localhost:8000/api/blog_posts/')
      .then((response) => {
        posts.value = response.data
        console.log(posts.value);
        
      })
      .catch((err) => {
        console.log(err);
        
      })
  } 
  
  return { posts ,getPostsData}
})
