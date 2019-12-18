<template>
  <div>
    <div class="columns">
      <div class="column is-one-third">
        <HomeSideNav></HomeSideNav>
      </div>
      <div class="column">
        <NewTweet></NewTweet>
        <div class="tweet-box">
          <Tweet></Tweet>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import LayoutDefault from "@/layouts/LayoutDefault.vue";
import HomeSideNav from "@/components/HomeSideNav.vue";
import Tweet from "@/components/Tweet.vue";
import NewTweet from "@/components/NewTweet.vue";

export default {
  name: "home",
  created() {
    this.$emit("update:layout", LayoutDefault);
  },
  components: {
    HomeSideNav,
    Tweet,
    NewTweet
  },
  computed: {
    getToken() {
      return this.$store.state.auth_token;
    }
  }
};
</script>

<style scoped>
.tweet-box {
  height: 50vh;
  overflow: scroll;
}
</style>
