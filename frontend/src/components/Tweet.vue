<template>
  <div class="box">
    <article class="media">
      <div class="media-left">
        <figure class="image is-64x64">
          <img src="https://bulma.io/images/placeholders/128x128.png" />
        </figure>
      </div>
      <div class="media-content">
        <div class="content">
          <div>
            <div v-if="tweets.first_name">
              <div>{{ tweets.first_name + " @" + tweets.username }}</div>
            </div>
            <div v-else>
              <div>{{ user.first_name + " @" + user.username }}</div>
            </div>
            <div class="tweet-text">{{ tweets.tweet_text }}</div>
            <br />
            <strong>{{ tweets.created_on }}</strong>
          </div>
        </div>
        <nav class="level is-mobile">
          <div class="level-left">
            <a class="level-item" aria-label="reply">
              <span class="icon is-small">
                <i class="fas fa-reply has-text-info"></i>
              </span>
            </a>
            <a class="level-item" aria-label="retweet">
              <span class="icon is-small">
                <i class="fas fa-retweet has-text-info"></i>
              </span>
            </a>
            <a class="level-item" aria-label="like">
              <span class="icon is-small">
                <i class="fas fa-heart has-text-info"></i>
              </span>
            </a>
            <span class="is-size-7 has-text-weight-semibold"></span>
          </div>
        </nav>
      </div>
    </article>
  </div>
</template>

<script>
export default {
  name: "Tweet",
  props: ["tweets"],
  data() {
    return {
      tweet: "",
      withTransition: true
    };
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    currentRouteName() {
      return this.$route.name;
    }
  }
};
</script>

<style scoped>
.tweet-text {
  margin: 5px 0 0 0;
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
