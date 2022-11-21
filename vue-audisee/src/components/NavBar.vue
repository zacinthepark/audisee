<template>
  <div>
    <!-- As a link -->
    <b-navbar variant="faded" type="light">
      <div class="container-fluid">
        <b-navbar-brand href="Home" class="text-white tw-bold"
          >AudiSee</b-navbar-brand
        >
        <router-link :to="{ name: 'ProfileView' }">
          <img
            src="https://mdbcdn.b-cdn.net/img/new/avatars/2.webp"
            class="rounded-circle shadow-4"
            style="width: 50px"
            alt="Avatar"
          />
        </router-link>
      </div>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style></style>
