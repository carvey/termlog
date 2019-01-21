<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <LogMain msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import LogMain from './components/LogMain.vue'

export default {
  name: 'app',
  components: {
    LogMain
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
