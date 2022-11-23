<template>
  <div>
    <!-- As a link -->
    <b-navbar variant="faded" type="light">
      <div class="container-fluid">
        <b-navbar-brand href="Home" class="text-white tw-bold"
          >AudiSee</b-navbar-brand
        >
        <router-link :to="{ name: 'ProfileView' }">
          <b-skeleton-icon
            icon="person-fill"
            :icon-props="{ fontScale: 1, variant: 'light' }"
          ></b-skeleton-icon>
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
