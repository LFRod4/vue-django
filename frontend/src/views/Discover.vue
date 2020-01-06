<template>
  <div>
    <div class="img-container">
      <img src="@/assets/images/home.jpg" />
    </div>
    <div class="columns hero-body">
      <div class="column is-one-fifth" v-for="profile in allProfiles" :key="profile.key">
        <UserCard :profile="profile"></UserCard>
        <CardFooter :userId="profile.id"></CardFooter>
      </div>
    </div>
  </div>
</template>

<script>
import LayoutDefault from "@/layouts/LayoutDefault.vue";
import UserCard from "@/components/UserCard.vue";
import CardFooter from "@/components/CardFooter.vue";

import axios from "axios";
import { mapState } from "vuex";

export default {
  name: "discover",
  components: {
    UserCard,
    CardFooter
  },
  data() {
    return {
      allProfiles: {}
    };
  },
  created() {
    this.$emit("update:layout", LayoutDefault);
  },
  mounted() {
    var profiles = [];
    axios
      .get("http://127.0.0.1:8000/api/tweets/userprofiles/")
      .then(response => {
        for (var x = 0; x < response.data.length; x++) {
          if (response.data[x][0] !== this.user.id) {
            var obj = {};
            obj["id"] = response.data[x][0];
            obj["first_name"] = response.data[x][1];
            obj["last_name"] = response.data[x][2];
            obj["about_me"] = response.data[x][3];
            obj["username"] = response.data[x][4];
            profiles.push(obj);
          }
          this.allProfiles = profiles;
        }
      })
      .catch(error => {
        return error;
      });
  },
  computed: {
    ...mapState(["user"])
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
  height: 30vh;
  object-fit: cover;
}
</style>
