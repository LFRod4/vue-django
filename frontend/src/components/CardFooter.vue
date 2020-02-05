<template>
  <div class="card">
    <footer class="card-footer">
      <div
        class="card-footer-item has-background-info has-text-white"
        v-if="ifFollowing(userId)"
        @click="unfollow(userId)"
      >Following</div>
      <div class="card-footer-item" v-else @click="followUser(userId)">Follow</div>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";
export default {
  name: "cardFooter",
  props: ["userId"],
  data() {
    return {
      follower_ids: []
    };
  },
  created() {
    this.follower_ids = this.$store.state.follower_ids;
  },
  methods: {
    followUser(userId) {
      axios.defaults.headers = {
        "Content-Type": "application/json"
      };
      axios
        .post("http://127.0.0.1:8000/api/tweets/follow/", {
          follower_id: this.user.id,
          followed_id: userId
        })
        .then(response => {
          this.$store.dispatch("updateFollowerId", userId);
          this.follower_ids.push(userId);
          return response;
        })
        .catch(error => {
          return error;
        });
    },
    ifFollowing(id) {
      if (this.follower_ids.includes(id)) {
        return true;
      } else {
        return false;
      }
    },
    unfollow(unfollowId) {
      axios.defaults.headers = {
        "Content-Type": "application/json"
      };
      axios
        .post("http://127.0.0.1:8000/api/tweets/delete/", {
          follower_id: this.user.id,
          followed_id: unfollowId
        })
        .then(response => {
          var index = this.follower_ids.indexOf(unfollowId);
          this.follower_ids.splice(index, 1);
          this.$store.dispatch("removeFollowerId", unfollowId);
          return response;
        })
        .catch(error => {
          return error;
        });
    }
  },
  computed: {
    ...mapState(["user"])
  }
};
</script>

<style lang="scss" scoped></style>
