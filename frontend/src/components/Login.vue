<template>
  <div>
    <div class="field">
      <label class="label">Email</label>
      <div class="control has-icons-left has-icons-right">
        <input
          class="input"
          type="text"
          placeholder="Email"
          value=""
          v-model="email"
        />
        <span class="icon is-small is-left">
          <i class="fas fa-user"></i>
        </span>
      </div>
      <p class="help is-success" v-if="TEST">This username is available</p>
    </div>

    <div class="field">
      <label class="label">Password</label>
      <p class="control has-icons-left">
        <input
          class="input"
          type="password"
          placeholder="Password"
          v-model="password"
        />
        <span class="icon is-small is-left">
          <i class="fas fa-lock"></i>
        </span>
      </p>
    </div>

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
      TEST: false,
      email: "test"
    };
  },
  methods: {
    submit() {
      var loginInfo = {
        email: this.email,
        password: this.password
      };
      this.$store.dispatch("logIn", loginInfo);
    }
  }
};
</script>

<style lang="scss" scoped></style>
