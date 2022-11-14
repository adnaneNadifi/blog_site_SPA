<template>
  <div class="w-full bg-white flex flex-col justify-start p-6 mb-4 shadow">
    <h3 class="text-2xl mb-4">Add Comment</h3>
    <q-form @submit="submitComment" class="q-gutter-md">
      <div>
        <q-input
          v-model="comment"
          type="text"
          class="mb-3"
          label="Type comment"
        />
        <q-btn
          class="float-right"
          label="Submit"
          type="submit"
          color="primary"
        />
      </div>
    </q-form>
  </div>
</template>
<script setup lang="ts">
import {   ref } from 'vue';
import { addComment } from 'src/services/articles/api';

const post_id = defineProps(['post_id'])
const comment = ref<string>('')


function submitComment() {
  const commentData:API.CommentForm = {
    post:post_id.post_id,
    comment:comment.value
  }
  addComment(commentData)
  // comment.value.comment = '';
}


</script>
