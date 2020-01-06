<template>
  <div>
    <div class="img-container">
      <img src="@/assets/images/home.jpg" class />
    </div>
    <div class="columns hero-body">
      <div class="column is-one-fifth">
        <UserCard></UserCard>
      </div>
      <div class="column right-column" v-if="tweetList.length > 0">
        <Tweet class="tweet" v-for="tweets in tweetList" :key="tweets.id" :tweets="tweets"></Tweet>
      </div>
      <div v-else>
        <div class="column righ-column">
          You aren't following anyone. Check out the
          <span>discover</span> tab to find cool people
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

export default {
  name: "home",
  components: {
    UserCard,
    Tweet
  },
  created() {
    this.$emit("update:layout", LayoutDefault);
    this.$store.dispatch("getFollowers");
  },
  computed: {
    tweetList() {
      return this.$store.state.followersTweetList;
    }
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
  height: 70vh;
  overflow: scroll;
}

.tweet {
  padding-bottom: 10px;
}
</style>
