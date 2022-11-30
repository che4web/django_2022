import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/article',
    name: 'article',
    component: () => import(/* webpackChunkName: "about" */ '../views/ArticleTable.vue')
  },
  {
      path: '/article/:id',
    name: 'article-detail',
    component: () => import(/* webpackChunkName: "about" */ '../views/ArticleDetail.vue')
  },

  {
      path: '/journal/:id',
    name: 'journal-detail',
    component: () => import(/* webpackChunkName: "about" */ '../views/JournalDetail.vue')
  },

  {
      path: '/article-my',
    name: 'article-my',
    component: () => import(/* webpackChunkName: "about" */ '../views/ArticleMy.vue')
  },

  {
      path: '/article-form',
    name: 'article-form',
    component: () => import(/* webpackChunkName: "about" */ '../views/ArticleForm.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
