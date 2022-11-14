<template>
  <div class="w-full bg-white flex flex-col justify-start p-6 mb-4 shadow">
    <h3 class="text-2xl mb-4">Add Comment</h3>
    <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-md">
      <div>
        <q-input v-model="text" type="text" class="mb-3" label="Type comment" />
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
<script setup lang="ts"></script>
