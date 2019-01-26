import Vue from 'vue'
import App from './App.vue'
import NavBar from './components/NavBar.vue'
import store from './store'
import VueSocketIO from 'vue-socket.io'
import Vuetify from 'vuetify'

import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader
import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader

Vue.config.productionTip = false
Vue.use(new VueSocketIO({
    debug: true,
    connection: 'http://localhost:5000',
}))

Vue.use(Vuetify)

new Vue({
  store,
  render: h => h(NavBar)
}).$mount('#NavBar')

new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
