<template>
  <div @click="goMainView(movie.id)" class="col">
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
    goMainView(id) {
      this.$router.push({ name: "MainView", params: { id } });
    },
  },
};
</script>

<style></style>
