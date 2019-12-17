<template>
  <div>
    <div class="field">
      <label class="label">Username</label>
      <div class="control has-icons-left has-icons-right">
        <input
          class="input is-success"
          type="text"
          placeholder="Username"
          value=""
        />
        <span class="icon is-small is-left">
          <i class="fas fa-user"></i>
        </span>
        <span class="icon is-small is-right">
          <i class="fas fa-check"></i>
        </span>
      </div>
      <p class="help is-success">This username is available</p>
    </div>

    <div class="field">
      <label class="label">Email</label>
      <div class="control has-icons-left has-icons-right">
        <input
          class="input is-danger"
          type="email"
          placeholder="Email"
          value=""
        />
        <span class="icon is-small is-left">
          <i class="fas fa-envelope"></i>
        </span>
        <span class="icon is-small is-right">
          <i class="fas fa-exclamation-triangle"></i>
        </span>
      </div>
      <p class="help is-danger">This email is invalid</p>
    </div>

    <div class="field">
      <label class="label">Password</label>
      <p class="control has-icons-left">
        <input class="input" type="password" placeholder="Password" />
        <span class="icon is-small is-left">
          <i class="fas fa-lock"></i>
        </span>
      </p>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link">Submit</button>
      </div>
      <div class="control">
        <button class="button is-link is-light">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped></style>
