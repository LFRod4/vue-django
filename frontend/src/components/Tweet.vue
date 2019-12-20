<template>
  <div>
    <transition-group name="tweets" tag="div">
      <div class="box" v-for="tweets in tweetList" :key="tweets.id">
        <article class="media">
          <div class="media-left">
            <figure class="image is-64x64">
              <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image" />
            </figure>
          </div>
          <div class="media-content">
            <div class="content">
              <p>
                <strong>{{ tweets[1] }}</strong>
                <br />
                {{ tweets[3] }}
              </p>
            </div>
            <nav class="level is-mobile">
              <div class="level-left">
                <a class="level-item" aria-label="reply">
                  <span class="icon is-small">
                    <i class="fas fa-reply has-text-info" aria-hidden="true"></i>
                  </span>
                </a>
                <a class="level-item" aria-label="retweet">
                  <span class="icon is-small">
                    <i class="fas fa-retweet has-text-info" aria-hidden="true"></i>
                  </span>
                </a>
                <a class="level-item" aria-label="like">
                  <span class="icon is-small">
                    <i class="fas fa-heart has-text-info" aria-hidden="true"></i>
                  </span>
                </a>
                <span class="is-size-7 has-text-weight-semibold"></span>
              </div>
            </nav>
          </div>
        </article>
      </div>
    </transition-group>
  </div>
</template>

<script>
export default {
  name: "Tweet",
  data() {
    return {
      tweet: ""
    };
  },
  computed: {
    user() {
      return this.$store.state.user;
    },
    tweetList() {
      return this.$store.state.tweetList;
    }
  }
};
</script>

<style scoped>
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
