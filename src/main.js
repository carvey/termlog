import Vue from 'vue'
import App from './App.vue'
import store from './store'
import VueSocketIO from 'vue-socket.io'

Vue.config.productionTip = false
Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://localhost:5000',
}))


new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
