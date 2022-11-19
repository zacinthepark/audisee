<template>
  <div class="row">
    <div class="col-4 bg-red text-start">
      <br />
      <br />
      <h6 class="fw-light">나를 위한 새로운 발견</h6>
      <br />
      <h3 class="fw-normal">{{ movieTitle }}</h3>
      <h3 class="fw-normal">추천 음악</h3>
      <br />
      <div class="opacity-75">
        <div class="d-inline pe-2">총 40 곡</div>
        |
        <div class="d-inline ps-2">2022.11.16</div>
      </div>
    </div>
    <div class="col">
      <MainAItem />
    </div>
  </div>
</template>

<script>
import MainAItem from "@/components/MainAItem";

export default {
  name: "MainA",
  components: {
    MainAItem,
  },
  props: {
    movieTitle: String,
  },
};
</script>

<style></style>
