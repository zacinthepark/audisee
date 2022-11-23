<template>
  <div>
    <!-- As a link -->
    <b-navbar variant="faded" type="light">
      <div class="container-fluid">
        <b-navbar-brand href="Home" class="text-white tw-bold"
          >AUDISEE</b-navbar-brand
        >
        <b-icon
          font-scale="0.8"
          @click="goProfile"
          icon="person-circle"
        ></b-icon>
      </div>
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
