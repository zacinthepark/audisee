<template>
  <div>
    <h1>RecommendView</h1>
    <h1>비슷한 영화 추천</h1>
    <RecommendItemVue />
  </div>
</template>

<script>
import RecommendItemVue from "@/components/RecommendItem.vue";

export default {
  name: "RecommendView",
  components: {
    RecommendItemVue,
  },
};
</script>

<style></style>
