<template>
  <div class="text-white">
    <router-link
      :to="{ name: 'SignupView' }"
      class="d-grid gap-2 d-md-flex justify-content-md-end text-decoration-none"
    >
      <button class="btn btn-outline-light" type="button">Signup</button>
    </router-link>
    <div class="card bg-transparent border-secondary">
      <h3 class="card-header">
        <b-navbar-brand href="Home" class="text-white tw-bold"
          >AudiSee</b-navbar-brand
        >
      </h3>
      <div class="card-body">
        <h4 class="card-subtitle my-1">Audisee에 로그인하세요</h4>
        <form @submit.prevent="logIn">
          <div class="m-3 row card-text fs-5">
            <label for="username" class="col-sm-2 col-form-label"
              >아이디
            </label>
            <div>
              <input
                type="text"
                class="form-control"
                id="username"
                v-model="username"
              />
            </div>
          </div>
          <div class="m-3 row card-text fs-5">
            <label for="password" class="col-sm-2 col-form-label"
              >비밀번호
            </label>
            <div>
              <input
                type="password"
                class="form-control"
                id="password"
                v-model="password"
              /><br />
            </div>
          </div>
          <button @click="goHome" type="submit" value="LogIn" class="btn btn-outline-light">
            Login
          </button>

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
