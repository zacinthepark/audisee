<template>
  <div class="text-white">
    <NavBarVue />

    <h1 class="pb-5">음산한 영화 추천 {{ mood }}</h1>
    <div class="row row-cols-1 row-cols-md-5 g-4">
      <RecommendItem v-for="(movie, index) in movies" :key="`recommend-${index}`" :movie="movie" />
    </div>
  </div>
</template>

<script>
import RecommendItem from "@/components/RecommendItem.vue";
import NavBarVue from "@/components/NavBar.vue";

export default {
  name: "RecommendView",
  components: {
    RecommendItem,
    NavBarVue,
  },
  computed: {
    movies() {
      return this.$store.state.recommendedMovies;
    },
    mood() {
      return this.$store.state.recommendedMood;
    },
  },
  created() {
    console.log(this.mood) // null --> ????????????
    this.$store.dispatch("getMovies")
  },
}
</script>

<style></style>
