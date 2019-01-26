
<template>

	<div class="HostLog">
	  <pre>{{ log }}</pre>
	</div>

</template>


<script type="text/javascript" charset="utf-8">

	export default {
		name: "HostLog",
		props: ['log'],
	}

</script>

<style>
	pre {
		text-align: left;
	}
</style>
