<template>
  <section class="hero is-info is-full-height">
    <div class="hero-head">
      <nav class="navbar">
        <div class="container">
          <div class="navbar-brand">
            <a class="navbar-item is-size-1 has-text-white">Twitter</a>
            <span class="navbar-burger burger" data-target="navbarMenuHeroA">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </div>
        </div>
      </nav>
    </div>
    <!-- Hero content: will be in the middle -->
    <div class="hero-body">
      <slot />
    </div>
  </section>
</template>

<script>
// @ is an alias to /src

export default {
  name: "loginsignup",
  components: {}
};
</script>

<style scoped>
section {
  min-height: 100%;
}
</style>
