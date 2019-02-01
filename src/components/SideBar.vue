<template>
  <v-navigation-drawer
  class="nav"
    :mini-variant.sync="mini"
    v-model="drawer"
    hide-overlay
    stateless
  >
    <v-toolbar flat class="transparent">
      <v-list class="pa-0">
        <v-list-tile avatar>
          <v-list-tile-avatar>
              <v-icon>laptop</v-icon>
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>Terminal Agents</v-list-tile-title>
          </v-list-tile-content>

          <v-list-tile-action>
            <v-btn
              icon
              @click.stop="mini = !mini"
            >
              <v-icon>chevron_left</v-icon>
            </v-btn>
          </v-list-tile-action>
        </v-list-tile>
      </v-list>
    </v-toolbar>

    <v-list class="pt-0" dense>
      <v-divider></v-divider>

      <v-list-tile
        v-for="(host, index) in hosts"
        :key="index"
        @click="make_active(host)"
      >

        <v-list-tile-action>
          <v-icon>mood</v-icon>
        </v-list-tile-action>

        <v-list-tile-content>
          <v-list-tile-title>
            {{ host }}
          </v-list-tile-title>
        </v-list-tile-content>

      </v-list-tile>

    </v-list>
  </v-navigation-drawer>
</template>

<script>
  import {mapGetters} from 'vuex';

  export default {
  name: "SideBar",
    data () {
      return {
        drawer: true,
        mini: true,
        right: null
      }
    },
    computed: {
      hosts() {
        return this.$store.getters.host_names
      }
    },
    created() {
      this.$socket.emit('log_hosts');
    },
    sockets: {
      recv_log_hosts: function(hosts) {
        for (let host of hosts) {
          this.$store.commit('add_host', host);
        }
      },
      command_added: function(data) {
        if (!this.$store.getters.host_names.includes(data.name)) {
          this.$store.commit('add_host', data.name);             
        }
      },
    },
    methods: {
      make_active(host_name) {
        this.$router.replace({ name: 'log_view', params: { name: host_name } })
      }
    }
  }
</script>


<style>

  a {
    color: inherit;
    text-decoration: inherit;
  }

</style>
