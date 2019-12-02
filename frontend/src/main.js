import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap'
import Google from './google'


import router from './router'
import store from './store'

Vue.use(BootstrapVue)

Vue.prototype.$google = new Google();

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
