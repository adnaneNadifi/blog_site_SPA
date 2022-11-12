<template>

  <q-layout  view="lHh Lpr lFf">
    <topic-navbar></topic-navbar>
    <q-page-container class="flex justify-center">
      <router-view />
    </q-page-container>
    <MainFooter/>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { EssentialLinkProps } from 'components/EssentialLink.vue';

import MainNavbar from "src/components/MainNavbar.vue";
import TopicNavbar from "src/components/TopicNavbar.vue";
import MainFooter from "src/components/MainFooter.vue";
import { usePostsStore } from "src/stores/posts";
import { onBeforeMount, onMounted} from "vue";

const essentialLinks: EssentialLinkProps[] = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev'
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev'
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev'
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev'
  }
];

const leftDrawerOpen = ref(false);
const isLoading = ref(true);

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}

const postsStore = usePostsStore()



</script>
