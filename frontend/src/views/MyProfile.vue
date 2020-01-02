<template>
  <div class="hero-body">
    <div class="columns">
      <div class="column is-one-third">
        <HomeSideNav></HomeSideNav>
      </div>
      <div class="column">
        <NewTweet></NewTweet>
        <div class="tweet-box">
          <transition-group name="tweets">
            <Tweet class="tweet" v-for="tweets in tweetList" :key="tweets.id" :tweets="tweets"></Tweet>
          </transition-group>
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
    },
    tweetList() {
      return this.$store.state.userTweetList;
    }
  }
};
</script>

<style>
.tweet {
  padding-bottom: 15px;
}

.tweets-enter-active {
  animation: add-tweet 1s;
}

.tweets-leave-active {
  position: absolute;
  animation: add-tweet 1s reverse;
}

.tweets-move {
  transition: transform 1s;
}
@keyframes add-tweet {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 0.5;
  }
  100% {
    opacity: 1;
  }
}
</style>
