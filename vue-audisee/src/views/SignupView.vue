<template>
  <!-- Section: Design Block -->
  <section class="background-radial-gradient overflow-hidden">
    <div class="container px-4 py-5 px-md-5 text-center text-lg-start my-5">
      <div class="row gx-lg-5 align-items-center mb-5">
        <div class="col-lg-6 mb-5 mb-lg-0" style="z-index: 10">
          <h1
            class="my-5 display-5 fw-bold ls-tight"
            style="color: hsl(218, 81%, 95%)"
          >
            Audisee <br />
            <span class="fs-2" style="color: hsl(218, 81%, 75%)"
              >당신의 취향을 찾아보세요</span
            >
          </h1>
        </div>

        <div class="col-lg-6 mb-5 mb-lg-0 position-relative">
          <div
            id="radius-shape-1"
            class="position-absolute rounded-circle shadow-5-strong"
          ></div>
          <div
            id="radius-shape-2"
            class="position-absolute shadow-5-strong"
          ></div>

          <div class="card bg-glass">
            <div class="card-body px-4 py-5 px-md-5">
              <form @submit.prevent="signUp">
                <!-- User input -->
                <div class="form-outline mb-4">
                  <h6 class="text-start">Username</h6>
                  <input
                    value="Username"
                    v-model="username"
                    type="text"
                    id="username"
                    class="form-control"
                  />
                </div>

                <!-- Password input -->
                <div class="form-outline mb-4">
                  <h6 class="text-start">Password</h6>
                  <input
                    value="Password"
                    v-model="password1"
                    type="password"
                    id="password1"
                    class="form-control"
                  />
                </div>
                <!-- Password input -->
                <div class="form-outline mb-4">
                  <h6 class="text-start">Check</h6>
                  <input
                    value="Check"
                    v-model="password2"
                    type="password"
                    id="password2"
                    class="form-control"
                  />
                </div>
                <!-- Checkbox -->
                <div class="form-check fs-6 d-flex justify-content-center mb-4">
                  <input
                    class="form-check-input me-2"
                    type="checkbox"
                    value=""
                    id="form2Example33"
                    checked
                  />
                  <label class="form-check-label" for="form2Example33">
                    개인정보 수집 및 이용에 관한 동의
                  </label>
                </div>

                <!-- Submit button -->
                <button type="submit" class="btn btn-primary btn-block mb-4">
                  Signup
                </button>
              </form>
              <div>
                <p class="mb-0 fw-normal fs-5">
                  이미 계정이 있다면?
                  <router-link
                    :to="{ name: 'LoginView' }"
                    class="fw-bold text-primary text-decoration-none"
                    >Log In</router-link
                  >
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
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
  },
};
</script>

<style>
.background-radial-gradient {
  background-color: hsl(218, 41%, 15%);
  background-image: radial-gradient(
      650px circle at 0% 0%,
      hsl(218, 41%, 35%) 15%,
      hsl(218, 41%, 30%) 35%,
      hsl(218, 41%, 20%) 75%,
      hsl(218, 41%, 19%) 80%,
      transparent 100%
    ),
    radial-gradient(
      1250px circle at 100% 100%,
      hsl(218, 41%, 45%) 15%,
      hsl(218, 41%, 30%) 35%,
      hsl(218, 41%, 20%) 75%,
      hsl(218, 41%, 19%) 80%,
      transparent 100%
    );
}

#radius-shape-1 {
  height: 220px;
  width: 220px;
  top: -60px;
  left: -130px;
  background: radial-gradient(#44006b, #ad1fff);
  overflow: hidden;
}

#radius-shape-2 {
  border-radius: 38% 62% 63% 37% / 70% 33% 67% 30%;
  bottom: -60px;
  right: -110px;
  width: 300px;
  height: 300px;
  background: radial-gradient(#44006b, #ad1fff);
  overflow: hidden;
}

.bg-glass {
  background-color: hsla(0, 0%, 100%, 0.9) !important;
  backdrop-filter: saturate(200%) blur(25px);
}
</style>
