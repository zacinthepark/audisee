<template>
  <div class="text-white">
    <div class="d-flex">
      <b-container class="me-5">
        <b-card-img
          style="width: 300px"
          class="rounded float-end"
          :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
          alt="#"
        />
      </b-container>
      <b-container>
        <div class="mb-5 text-start col-6">
          <h3>{{ movie.title }}</h3>
          <h6 class="opacity-50">{{ movie.release_date }}</h6>
          <br />
          <h6>{{ movie.genre }}</h6>
          <h6>★ {{ movie.vote_average }}</h6>
          <br />
          <h6>{{ movie.overview }}</h6>
        </div>
      </b-container>
    </div>

    <div>
      <b-tabs class="fs-6 m-5" pills card>
        <b-tab class="fs-6" title="추천음악" active
          ><MainAVue :movie-title="movieTitle"
        /></b-tab>
        <b-tab class="fs-6" title="상세정보" lazy> <MainCVue /></b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<!-- title, genre, overview, release_date, poster_path, popularity, vote_count, vote_average -->

<script>
import MainAVue from "@/components/MainA.vue";
import MainCVue from "@/components/MainC.vue";

export default {
  name: "MainView",
  components: {
    MainAVue,
    MainCVue,
  },
  data() {
    return {
      movie: null,
    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
  },
  methods: {
    getMovieById(id) {
      for (const movie of this.movies) {
        if (movie.id === Number(id)) {
          this.movie = movie;
          break;
        }
      }
    },
  },
  created() {
    this.getMovieById(this.$route.params.id);
  },
};
</script>

<style></style>
