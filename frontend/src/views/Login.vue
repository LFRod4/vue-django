<template>
  <div class="login box">
    <Login></Login>
    <SignUp v-if="loggedIn"></SignUp>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginSignUpVue from "../layouts/LoginSignUp.vue";
import Login from "@/components/Login.vue";
import SignUp from "@/components/SignUp.vue";
import router from "../router/index.js";

export default {
  name: "home",
  created() {
    this.$emit("update:layout", LoginSignUpVue);
  },
  data() {
    return {
      loggedIn: false
    };
  },
  components: {
    Login,
    SignUp
  },
  mounted() {
    if (this.$store.state.authToken) {
      window.alert("test");
      router.push({ path: "/myprofile" });
    }
  }
};
</script>

<style>
.login {
  max-width: 30%;
  margin: 0 auto;
}
</style>
