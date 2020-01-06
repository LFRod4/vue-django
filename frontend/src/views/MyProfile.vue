<template>
  <div class="hero-body">
    <div class="columns">
      <div class="column is-one-third">
        <UserCard :profile="user"></UserCard>
      </div>
      <div class="column">
        <NewTweet></NewTweet>
        <div class="tweet-box">
          <transition-group name="tweets" v-if="userTweetList.length > 0">
            <Tweet class="tweet" v-for="tweets in userTweetList" :key="tweets.id" :tweets="tweets"></Tweet>
          </transition-group>
          <div v-else>
            <div class="box">
              <div class="first-tweet">Send Your First Tweet</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import LayoutDefault from "@/layouts/LayoutDefault.vue";
import UserCard from "@/components/UserCard.vue";
import Tweet from "@/components/Tweet.vue";
import NewTweet from "@/components/NewTweet.vue";
import { mapState } from "vuex";

export default {
  name: "home",
  created() {
    this.$emit("update:layout", LayoutDefault);
  },
  components: {
    UserCard,
    Tweet,
    NewTweet
  },
  computed: {
    ...mapState(["auth_token", "userTweetList", "user"])
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

.first-tweet {
  margin: 0 auto;
  font-size: 20px;
  font-weight: bold;
}
</style>
