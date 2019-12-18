<template>
  <div>
    <div class="box" v-for="tweet in tweetList" :key="tweet.id">
      <article class="media">
        <div class="media-left">
          <figure class="image is-64x64">
            <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image" />
          </figure>
        </div>
        <div class="media-content">
          <div class="content">
            <p>
              <strong>{{tweet["first_name"]}}</strong>
              <br />
              {{ tweet["tweet_text"] }}
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
              <span class="is-size-7 has-text-weight-semibold">
                {{
                tweet["created_on"]
                }}
              </span>
            </div>
          </nav>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  name: "Tweet",
  data() {
    return {
      tweet: "",
      allTweets: {}
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

<style scoped></style>
