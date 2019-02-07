<template>

  <div id="log-pane">

	<v-container grid-list-md text-xs-center>
		<v-layout row wrap>
		  <v-flex xs12>

			<div id="host-header-block">
			  <div id="host-header">{{host}}</div>
			</div>


		  </v-flex>

		  <v-flex xs12>

			<div class="loading" v-if="loading">
			  Loading ...
			</div>

			<div id="LogMain">
			  <HostLog
			  v-for="log in logs"
			  v-bind:key="log.id"
			  v-bind:log="log.command"
			  ></HostLog>
			</div>
		  
		  </v-flex>

	  </v-layout>
  </v-container>

  </div>

</template>


<script type="text/javascript" charset="utf-8">
import HostLog from './HostLog.vue'

    export default {
        name: "LogMain",
        components: {
            HostLog
        },
        created() {
          this.fetch_log()
        },
        watch: {
          '$route': 'fetch_log'
        },
        data: function() {
          return {
            logs: [],
            host: null,
            loading: true,
            next_id: 1,
            log_str: ""
          }
        },
        methods: {
          fetch_log() {
            this.host = this.$route.params.name
            this.$socket.emit('pull_log', this.host)
          }
        },
        sockets: {
          pull_log: function(data) {
            this.loading = true;
            this.logs = [];

            for (let line in data.log) {
              this.logs.push({ id: this.next_id++, command: data.log[line]})
            }

            this.loading = false
          },

          append_command: function(command) {
			 this.logs.push({ id: this.next_id++, command: command})
          }
        }

    }

</script>


<style scoped>

  #host-header {
    float: left;
    font-size: 32px; 
  }


</style>
