import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    hosts: []
  },
  mutations: {
    add_host(state, host_name) {
      for (let host of state.hosts) {
        if (host.name == host_name) {
          return
        }
        
      }
      state.hosts.push({"name": host_name, "logs": []}) 
    }
  },
  getters: {
    host_names: (state, getters) => {
      var names = [];

      for (let host of state.hosts) {
        names.push(host.name) 
      }

      return names
    },
  },
  actions: {

  }
})
