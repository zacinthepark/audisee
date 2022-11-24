<template>
  <div>
    <div
      class="card h-100 bg-transparent border-transparent"
      style="width: 12rem"
    >
      <img
        class="rounded card-img-top"
        :src="`https://image.tmdb.org/t/p/original${myMovie.poster_path}`"
        alt="#"
      />

      <div class="card-body">
        <span class="fs-5">{{ myMovie.title }}</span>
        <button
          type="button"
          class="btn btn-outline-none fs-5 fw-bold btn-lg"
          style="color: red"
          @click="deleteMyMovie"
        >
          x
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfileLike",
  props: {
    myMovie: Object,
  },
  methods: {
    deleteMyMovie() {
      const movie_id = this.myMovie.id;
      this.$store.dispatch("deleteMyMovie", movie_id);
    },
  },
};
</script>

<style></style>
