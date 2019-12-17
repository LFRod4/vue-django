<template>
  <section class="hero is-info is-full-height">
    <!-- Hero head: will stick at the top -->
    <TheHeader></TheHeader>
    <!-- Hero content: will be in the middle -->
    <div class="hero-body">
      <slot />
    </div>

    <!-- Hero footer: will stick at the bottom -->
    <TheFooter></TheFooter>
  </section>
</template>

<script>
// @ is an alias to /src
import TheHeader from "@/components/TheHeader.vue";
import TheFooter from "@/components/TheFooter.vue";

export default {
  name: "home",
  components: {
    TheHeader,
    TheFooter
  }
};
</script>

<style scoped>
section {
  min-height: 100%;
}
</style>
