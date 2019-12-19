<template>
  <div class="hero-head">
    <nav class="navbar">
      <div class="container">
        <div class="navbar-brand">
          <a class="navbar-item is-size-1 has-text-white">Tw</a>
          <span class="navbar-burger burger" data-target="navbarMenuHeroA">
            <span></span>
            <span></span>
            <span></span>
          </span>
        </div>
        <div id="navbarMenuHeroA" class="navbar-menu">
          <div class="navbar-end">
            <router-link
              @click.native="activeTab = 'home'"
              to="/"
              class="navbar-item"
              :class="{ 'is-active' : activeTab === 'home'}"
            >Home</router-link>
            <router-link
              @click.native="activeTab = 'profile'"
              to="/myprofile"
              class="navbar-item"
              :class=" { 'is-active' : activeTab === 'profile'}"
            >My Profile</router-link>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "TheHeader",
  props: {
    msg: String
  },
  data() {
    return {
      activeTab: "profile"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
