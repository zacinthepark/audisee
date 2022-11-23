<template>
  <div class="text-white">
    <NavBarVue />
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
          <button
            type="button"
            class="btn btn-outline-none fs-4 fw-bold btn-lg"
            style="color: red"
            @click="addToMyMovie"
          >
            ❤
          </button>
        </div>
      </b-container>
    </div>

    <div>
      <b-tabs class="fs-6 m-5" pills card>
        <b-tab class="fs-6" title="추천음악" active
          ><MainAVue :movie="movie"
        /></b-tab>
        <b-tab class="fs-6" title="상세정보" lazy>
          <MainCVue :movie="movie"
        /></b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<!-- title, genre, overview, release_date, poster_path, popularity, vote_count, vote_average -->

<script>
import MainAVue from "@/components/MainA.vue";
import MainCVue from "@/components/MainC.vue";
import axios from "axios";
import NavBarVue from "@/components/NavBar.vue";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainView",
  components: {
    MainAVue,
    MainCVue,
    NavBarVue,
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
          this.movieTitle = movie.title;
          break;
        }
      }
    },
    addToMyMovie() {
      const title = this.movie.title;
      const poster_path = this.movie.poster_path;
      axios({
        method: "post",
        url: `${API_URL}/playlist/movies/`,
        data: {
          title: title,
          poster_path: poster_path,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.getMovieById(this.$route.params.id);
    this.$store.dispatch("getMusicRecommendation");
  },
};
</script>

<style></style>
