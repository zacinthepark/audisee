<template>
  <div class="text-white">
    <router-link
      :to="{ name: 'LoginView' }"
      class="d-grid gap-2 d-md-flex justify-content-md-end text-decoration-none"
    >
      <button class="btn btn-outline-light" type="button">Login</button>
    </router-link>
    <div class="card bg-transparent border-secondary">
      <h3 class="card-header">
        <b-navbar-brand href="Home" class="text-white tw-bold"
          >AudiSee</b-navbar-brand
        >
      </h3>
      <div class="card-body">
        <h4 class="card-subtitle my-1">Audisee에 가입하세요</h4>
        <form @submit.prevent="signUp">
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
            <label for="password1" class="col-sm-2 col-form-label"
              >비밀번호
            </label>
            <div>
              <input
                type="password"
                class="form-control"
                id="password1"
                v-model="password1"
              />
            </div>
          </div>
          <div class="m-3 row card-text fs-5">
            <h6 for="password2" class="col-sm-2 col-form-label">
              비밀번호 확인
            </h6>
            <div>
              <input
                type="password"
                class="form-control"
                id="password2"
                v-model="password2"
              />
            </div>
          </div>
          <button type="submit" value="SignIn" class="btn btn-outline-light">
            Signup
          </button>
          <label for="username">아이디: </label>
          <input type="text" id="username" v-model="username" /><br />

          <label for="password1">비밀번호: </label>
          <input type="text" id="password1" v-model="password1" /><br />

          <label for="password2">비밀번호 확인: </label>
          <input type="text" id="password2" v-model="password2" /><br />

          <input type="submit" value="회원가입" />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignupView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signUp() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      };
      this.$store.dispatch("signUp", payload);
      this.$router.push({ name: "HomeView" });
    },
    // goHome() {
    //   this.$router.push({ name: "HomeView" });
    // },
  },
};
</script>

<style></style>
