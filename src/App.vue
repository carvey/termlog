<template>
  <div id="app">

	<v-container grid-list-md text-xs-center>

		<div id="sidebar">
			<SideBar></SideBar>
		</div>

		<div id="content">
			<LogMain msg="Welcome to Your Vue.js App"/>
		</div>

	</v-container>

  </div>
</template>

<script>
import LogMain from './components/LogMain.vue'
import SideBar from './components/SideBar.vue'

export default {
  name: 'app',
  components: {
	SideBar,
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
  margin: auto;
  padding: 10px;
}

#sidebar {
  float:left;
  height: 100%;
    z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  overflow-x: hidden; /* Disable horizontal scroll */
  position:fixed;
  padding-top: 65px;
}

#content {

}
</style>
