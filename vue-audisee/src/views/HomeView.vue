<!-- Background image -->
<template>
  <!-- Background image -->
  <div class="bg-image shadow-2-strong">
    <div>
      <div
        class="container d-flex align-items-center justify-content-center text-center h-100"
      >
        <div class="text-white">
          <h1 class="mb-3">방금 영화를 시청하셨나요?</h1>
          <br />
          <router-link
            :to="{ name: 'SearchView' }"
            class="btn btn-outline-light btn-lg m-2"
            role="button"
            >START Audisee</router-link
          >
        </div>
      </div>
    </div>
  </div>
  <!-- Background image -->
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style>
/* Height for devices larger than 576px */
@media (min-width: 992px) {
  #intro {
    margin-top: -58.59px;
  }
}

.navbar .nav-link {
  color: #fff !important;
}
</style>
