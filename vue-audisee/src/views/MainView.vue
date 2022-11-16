<template>
  <div>
    <h1>MainView</h1>
    <h1>블랙팬서</h1>
    <router-link :to="{ name: '' }"></router-link>
    <router-link :to="{ name: '' }"></router-link>
    <router-link :to="{ name: '' }"></router-link>
  </div>
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
