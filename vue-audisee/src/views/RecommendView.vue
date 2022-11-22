<template>
  <div class="text-white">
    <h1 class="pb-5">음산한 영화 추천</h1>
    <div class="row row-cols-1 row-cols-md-5 g-4">
      <RecommendItem v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>
  </div>
</template>

<script>
import RecommendItem from "@/components/RecommendItem.vue";

export default {
  name: "RecommendView",
  components: {
    RecommendItem,
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
  },
  created() {
    this.$store.dispatch("getMovies");
  },
};
</script>

<style></style>
