<template>
  <div>
    <div class="field">
      <label class="label">Email</label>
      <div class="control has-icons-left has-icons-right">
        <input class="input" type="text" placeholder="Email" value v-model="email" />
        <span class="icon is-small is-left">
          <i class="fas fa-user"></i>
        </span>
      </div>
    </div>

    <div class="field">
      <label class="label">Password</label>
      <p class="control has-icons-left">
        <input class="input" type="password" placeholder="Password" v-model="password" />
        <span class="icon is-small is-left">
          <i class="fas fa-lock"></i>
        </span>
      </p>
    </div>
    <div class="sign-up is-size-7 has-text-weight-semibold has-text-link" @click="signUp()">Sign Up</div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" @click="submit()">Submit</button>
      </div>
      <div class="control">
        <button class="button is-link is-light">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: "",
      password: "",
      email: ""
    };
  },
  methods: {
    submit() {
      var loginInfo = {
        email: this.email,
        password: this.password
      };
      this.$store.dispatch("logIn", loginInfo);
    },
    signUp() {
      this.$store.dispatch("loginSignUp", true);
    }
  }
};
</script>

<style scoped>
.sign-up {
  padding-bottom: 10px;
}
</style>
