import Vue from 'vue'
import Router from 'vue-router'

import Login from './views/Login.vue';
import Schedules from './views/Schedules.vue';
import Create from './views/Create.vue';
import Calendar from './views/Calendar.vue';

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/schedules',
      name: 'schedules',
      component: Schedules
    },
    {
      path: '/create',
      name: 'create',
      component: Create
    },
    {
      path: '/calendar/:id',
      name: 'calendar',
      component: Calendar
    }
  ]
})
