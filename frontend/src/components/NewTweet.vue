<template>
  <div class="box">
    <label class="label">New Tweet</label>
    <textarea class="textarea" v-model="newTweet"></textarea>
    <button class="button is-info submit-tweet" @click="submitTweet()">
      Tweet
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "NewTweet",
  data() {
    return {
      newTweet: ""
    };
  },
  methods: {
    submitTweet() {
      axios.defaults.headers = {
        Authorization: "Token " + this.token
      };
      axios
        .post("http://127.0.0.1:8000/api/tweets/create/", {
          tweet_text: this.newTweet,
          author: 1
        })
        .then(res => {
          this.newTweet = "";
          this.$store.dispatch("getTweets");
          return res;
        })
        .catch(error => {
          return error;
        });
    }
  },
  computed: {
    User() {
      return this.$store.state.user;
    },
    token() {
      return this.$store.state.authToken;
    }
  }
};
</script>

<style scoped>
.submit-tweet {
  display: float;
  margin-top: 10px;
}
</style>
