import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap'

import GAuth from 'vue-google-oauth2'

Vue.use(GAuth, {
  clientId: '220236547468-49pis7nd758b0rg1rrldmn38jjtl74f7.apps.googleusercontent.com',
  // scope: 'profile email',
  // prompt: 'select_account'
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
