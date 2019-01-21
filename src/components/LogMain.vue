<template>

    <div id="LogMain">
      <p>Big log template</p>
      <input type="text" />
      <button @click="emitClick">emit</button>
      <HostLog log="test log"></hostLog>
    </div>

</template>


<script type="text/javascript" charset="utf-8">
import HostLog from './HostLog.vue'

    export default {
        name: "LogMain",
        components: {
            HostLog
        },
        sockets: {
            connect: function() {
                this.$socket.emit('log_hosts');
            },
            log_hosts: function(data) {
                console.log(data);
            },
            recv_charles_log: function(data) {
                console.log("Received!");
                console.log(data);
            }
        },
        methods: {
            emitClick () {
                this.$socket.emit('get_charles_log', 'test');
            }
        }
    }

/*
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    // verify our websocket connection is established
    socket.on('connect', function() {
        console.log('Websocket connected!');
    });
    // message handler for the 'join_room' channel
    socket.on('join_room', function(msg) {
        console.log(msg);
    });
    // createGame onclick - emit a message on the 'create' channel to 
    // create a new game with default parameters
    function createGame() {
      console.log('Creating game...');
      socket.emit('create', {size: 'normal', teams: 2, dictionary: 'Simple'});
    }
*/
</script>
