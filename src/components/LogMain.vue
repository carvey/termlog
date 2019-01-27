<template>

    <div id="LogMain">
      <HostLog
      v-for="log in logs"
      v-bind:key="log.id"
      v-bind:command="log.command"
      v-bind:log="log.command"
      ></HostLog>
    </div>

</template>


<script type="text/javascript" charset="utf-8">
import HostLog from './HostLog.vue'

    export default {
        name: "LogMain",
        components: {
            HostLog
        },
        data: function() {
          return {
            logs: [],
            nextIndex: 1
          }
        },
    }

/*
    sockets: {
        recv_charles_log: function(data) {
      this.logs.push({id: this.nextIndex++, command: data.log});
        }
    },
*/

</script>
