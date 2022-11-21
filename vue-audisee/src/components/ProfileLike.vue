<template>
  <div>
    <div class="card bg-transparent border-transparent" style="width: 18rem">
      <img
        class="rounded card-img-top"
        :src="`https://image.tmdb.org/t/p/original${myMovie.poster_path}`"
        alt="#"
      />

      <div class="card-body">
        <span>{{ myMovie.title }}</span>
        <button
          type="button"
          class="btn btn-outline-none fs-4 fw-bold btn-lg"
          style="color: red"
        >
          ❤
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
};
</script>

<style></style>
