<template>
  <div>
    <b-navbar toggleable="lg" type="dark" class="mb-3 container-fluid">
      <b-navbar-brand href="Home" class="text-white tw-bold m-5"
        ><img
          src="../assets/audisee.png"
          alt="#"
          class="me-1"
          style="width: 25px"
        />
        AUDISEE</b-navbar-brand
      >
      <b-collapse id="nav-collapse" class="fs-5 d-flex ml-auto" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item href="Search">Search</b-nav-item>
          <b-nav-item href="Members">Members</b-nav-item>
          <b-nav-item href="Profile">Profile</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  methods: {
    goProfile() {
      this.$router.push({ name: "ProfileView" });
    },
  },
};
</script>

<style>
a {
  text-decoration: none;
  color: white;
}
</style>
