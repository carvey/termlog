
import VueRouter from 'vue-router'
import LogMain from '../src/components/LogMain.vue'

const routes = [
  {
    path: '/log/:name',
    name: 'log_view',
    component: LogMain,
    props: true
  }  
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router;
