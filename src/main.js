import Vue from 'vue'
import App from './App.vue'
import NavBar from './components/NavBar.vue'
import store from './store'
import VueSocketIO from 'vue-socket.io'
import Vuetify from 'vuetify'
import io from 'socket.io-client';

import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader
import 'material-design-icons-iconfont/dist/material-design-icons.css' // Ensure you are using css-loader

const socketInstance = io('http://localhost:5000', {
  transports: ['websocket'],
});

Vue.config.productionTip = false
Vue.use(new VueSocketIO({
    debug: true,
    connection: socketInstance,
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

