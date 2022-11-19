<template>
  <div class="col" @click="moveMain">
    <img
      class="m-2"
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
      alt="#"
      style="width: 200px; height: 300px"
    />
    <h6 class="p-2">{{ movie.title }}</h6>
  </div>
</template>

<script>
export default {
  name: "RecommendItem",
  props: {
    movie: Object,
  },

  methods: {
    moveMain() {
      this.$router.push({
        name: "MainView",
        parmas: { movie_id: this.movie.id },
      });
    },
  },
};
</script>

<style></style>
