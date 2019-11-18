import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap'

import GAuth from 'vue-google-oauth2'

Vue.use(GAuth, {
  clientId: '220236547468-tej6t7kvg133npvqp80s60mrl7gtaofi.apps.googleusercontent.com',
  access_type: 'offline',

  scope: 'https://www.googleapis.com/auth/calendar',
  prompt: 'consent'
})

import router from './router'
import store from './store'

Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
