import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/',name:"home", component: () => import('pages/IndexPage.vue') },
      { path: '/article/:id',name:'article', component: () => import('pages/ArticlePage.vue') },
      { path: '/category/:id',name:'category', component: () => import('pages/CategoriesIndexPage.vue') },
    ],
  },
 
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
