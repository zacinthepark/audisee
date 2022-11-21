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
        <form @submit.prevent="logIn">
          <label for="username">아이디: </label>
          <input type="text" id="username" v-model="username" /><br />

          <label for="password">비밀번호: </label>
          <input type="text" id="password" v-model="password" /><br />

          <input @click="goHome" type="submit" value="로그인" />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    logIn() {
      const username = this.username;
      const password = this.password;
      const payload = {
        username: username,
        password: password,
      };
      this.$store.dispatch("logIn", payload);
    },
    goHome() {
      this.$router.push({ name: "HomeView" });
    },
  },
};
</script>

<style></style>
