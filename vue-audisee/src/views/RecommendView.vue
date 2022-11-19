<template>
  <div>
    <h1>RecommendView</h1>
    <h1>비슷한 영화 추천</h1>
    <RecommendItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
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
      return this.$store.state.movies
    },
  },
  created() {
      this.$store.dispatch('getMovies')
  },
};
</script>

<style></style>
