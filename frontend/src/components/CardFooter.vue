<template>
  <div class="card">
    <footer class="card-footer">
      <div
        class="card-footer-item has-background-info has-text-white"
        v-if="ifFollowing(userId)"
      >Following</div>
      <div class="card-footer-item" v-else @click="followUser()">Follow</div>
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
    return {};
  },
  methods: {
    followUser(following_id) {
      axios
        .post("http://127.0.0.1:8000/auth/users/", {
          follower_id: this.user.id,
          following_id: following_id
        })
        .then(response => {
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
    }
  },
  computed: {
    ...mapState(["follower_ids", "user"])
  }
};
</script>

<style lang="scss" scoped></style>
