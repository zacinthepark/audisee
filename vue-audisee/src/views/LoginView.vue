<template>
  <div class="text-white">
    <router-link
      :to="{ name: 'SignupView' }"
      class="d-grid gap-2 d-md-flex justify-content-md-end text-decoration-none"
    >
      <button class="btn btn-outline-light" type="button">Signup</button>
    </router-link>
    <div class="d-flex align-items-center justify-content-center">
      <div class="text-start">
        <h1>Login</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
};
</script>

<style></style>
