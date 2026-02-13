import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SubjectView from '@/views/SubjectView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import Test from '@/views/Test.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    }, 
    {
      path: '/subject/:title',
      name: 'subject',
      component: SubjectView,
    },
    {
      path: '/test',
      name: 'test',
      component: Test,
    },
    {
      path: '/:catchAll(.*)',
      name: 'not-found',
      component: NotFoundView
    }
  ],
})

export default router
