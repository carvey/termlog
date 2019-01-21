
<template>

	<div id="HostLog">
  	  <p>Here some host logs:</p>
  	  <div>{{ log }}</div>
	</div>

</template>


<script type="text/javascript" charset="utf-8">

	export default {
		name: "HostLog",
		props: ['log'],
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
