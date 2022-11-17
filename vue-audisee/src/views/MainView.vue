<template>
  <!-- <div>
    <h1>MainView</h1>
    <h1>블랙팬서</h1>
    <MainAVue />
    <MainBVue />
    <MainCVue />
  </div> -->

  <b-container>
    <div class="mb-5">
      <p class="fs-3 text-white">블랙팬서</p>
    </div>
    <MainAVue />
    <MainBVue />
    <MainCVue />
  </b-container>
</template>

<script>
import MainAVue from "@/components/MainA.vue";
import MainBVue from "@/components/MainB.vue";
import MainCVue from "@/components/MainC.vue";

export default {
  name: "MainView",
  components: {
    MainAVue,
    MainBVue,
    MainCVue,
  },
};
</script>

<style></style>
