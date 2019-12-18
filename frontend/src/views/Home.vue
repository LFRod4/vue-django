<template>
  <div>
    <div class="img-container">
      <img src="@/assets/images/home.jpg" class />
    </div>
    <div class="columns hero-body">
      <div class="column is-one-fifth">
        <HomeSideNav></HomeSideNav>
      </div>
      <div class="column right-column">
        <NewTweet></NewTweet>
        <Tweet></Tweet>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import LayoutDefault from "@/layouts/LayoutDefault.vue";
import NewTweet from "@/components/NewTweet.vue";
import HomeSideNav from "@/components/HomeSideNav.vue";
import Tweet from "@/components/Tweet.vue";

export default {
  name: "home",
  components: {
    NewTweet,
    HomeSideNav,
    Tweet
  },
  created() {
    this.$emit("update:layout", LayoutDefault);
  }
};
</script>

<style scoped>
.img-container {
  width: 100%;
  height: 100%;
}
.img-container img {
  width: 100%;
  height: 45vh;
  object-fit: cover;
}

.profile-img {
  padding-left: 25%;
}

.right-column {
  height: 100vh;
  overflow: scroll;
}
</style>
