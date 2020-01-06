<template>
  <div>
    <div class="field">
      <label class="label">First Name</label>
      <div class="control">
        <input class="input" type="text" placeholder="First Name" v-model="firstName" value />
      </div>
    </div>
    <div class="field">
      <label class="label">Last Name</label>
      <div class="control">
        <input class="input" type="text" placeholder="Last Name" v-model="lastName" value />
      </div>
    </div>
    <div class="field">
      <label class="label">Username</label>
      <div class="control has-icons-left has-icons-right">
        <input class="input" type="text" placeholder="Username" v-model="username" value />
        <span class="icon is-small is-left">
          <i class="fas fa-user"></i>
        </span>
        <span class="icon is-small is-right">
          <i class="fas fa-check"></i>
        </span>
      </div>
    </div>
    <div class="field">
      <label class="label">Email</label>
      <div class="control has-icons-left has-icons-right">
        <input class="input" type="email" placeholder="Email" v-model="email" value />
        <span class="icon is-small is-left">
          <i class="fas fa-envelope"></i>
        </span>
      </div>
      <p class="help is-danger" v-if="errors">This email is invalid</p>
    </div>
    <div class="field">
      <label class="label">About Me</label>
      <div class="control has-icons-left has-icons-right">
        <input class="input" type="text" placeholder="AboutMe" v-model="aboutMe" value />
        <span class="icon is-small is-left">
          <i class="fas fa-envelope"></i>
        </span>
      </div>
      <p class="help is-danger" v-if="errors">This email is invalid</p>
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
    <div class="field">
      <label class="label">Re-Password</label>
      <p class="control has-icons-left">
        <input class="input" type="password" placeholder="Password" v-model="rePassword" />
        <span class="icon is-small is-left">
          <i class="fas fa-lock"></i>
        </span>
      </p>
    </div>
    <div class="is-size-7 has-text-link has-text-weight-semibold" @click="loginSignUp()">Login</div>
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
      firstName: "",
      lastName: "",
      username: "",
      email: "",
      aboutMe: "",
      password: "",
      rePassword: "",
      errors: ""
    };
  },
  methods: {
    submit() {
      var payload = {
        firstName: this.firstName,
        lastName: this.lastName,
        username: this.username,
        email: this.email,
        password: this.password
      };
      if (this.password === this.rePassword && this.password) {
        this.$store.dispatch("createNewUser", payload);
      }
    },
    loginSignUp() {
      this.$store.dispatch("loginSignUp", false);
    }
  }
};
</script>

<style scoped>
.login {
  padding-bottom: 10px;
}
</style>
