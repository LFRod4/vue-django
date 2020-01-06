<template>
  <div class="login box">
    <LoginForm v-if="!this.$store.state.signUp"></LoginForm>
    <SignUp v-if="this.$store.state.signUp"></SignUp>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginSignUpVue from "../layouts/LoginSignUp.vue";
import LoginForm from "@/components/LoginForm.vue";
import SignUp from "@/components/SignUp.vue";
import router from "../router/index.js";

export default {
  name: "home",
  created() {
    this.$emit("update:layout", LoginSignUpVue);
  },
  data() {
    return {
      signUp: false
    };
  },
  components: {
    LoginForm,
    SignUp
  },
  mounted() {
    if (this.$store.state.authToken) {
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
