<template>
  <div class="w-full bg-white flex flex-col justify-start p-6 shadow">
    <h3 class="text-2xl mb-4">Comment section</h3>
    <q-list bordered separator>
      <q-item v-for="(comment, index) in comments" :key="index">
        <q-item-section>{{ comment.comment }}</q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  comments: API.Comment[];
}>();
</script>
