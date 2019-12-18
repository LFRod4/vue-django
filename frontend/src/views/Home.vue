<template>
  <div class>
    <h1>Home</h1>
  </div>
</template>

<script>
// @ is an alias to /src
import LayoutDefault from "@/layouts/LayoutDefault.vue";

export default {
  name: "home",
  created() {
    this.$emit("update:layout", LayoutDefault);
  },
  components: {}
};
</script>
