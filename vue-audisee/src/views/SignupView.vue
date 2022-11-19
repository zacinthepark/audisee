<template>
  <div class="text-white">
    <router-link
      :to="{ name: 'LoginView' }"
      class="d-grid gap-2 d-md-flex justify-content-md-end text-decoration-none"
    >
      <button class="btn btn-outline-light" type="button">Login</button>
    </router-link>
    <div class="d-flex align-items-center justify-content-center">
      <div class="text-start">
        <h1>Signup</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignupView",
};
</script>

<style></style>
