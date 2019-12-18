<template>
  <component :is="layout">
    <router-view :layout.sync="layout" />
  </component>
</template>

<script>
export default {
  data() {
    return {
      layout: "div",
      posts: []
    };
  }
};
</script>

<style>
.tweet-box {
  height: 50vh;
  overflow: scroll;
}
</style>
