<template>
  <div class="container text-white">
    <NavBarVue />
    <div>
      <h3>
        <span class="m-3" id="one" @click="getMovieRecommendOne"
          >adventure</span
        >
        <span class="m-3" id="two" @click="getMovieRecommendTwo"
          >animation</span
        >
        <span class="m-3" id="three" @click="getMovieRecommendThree"
          >humanism</span
        >
      </h3>
      <br />
      <h3>
        <span class="m-3" id="four" @click="getMovieRecommendFour"
          >thrillers</span
        >
        <span class="m-3" id="five" @click="getMovieRecommendFive"
          >actions</span
        >
        <span class="m-3" id="six" @click="getMovieRecommendSix">comedy</span>
        <span class="m-3" id="seven" @click="getMovieRecommendSeven"
          >romance</span
        >
      </h3>
      <br />
      <h3>
        <span class="m-3" id="eight" @click="getMovieRecommendEight"
          >history</span
        >
        <span class="m-3" id="nine" @click="getMovieRecommendNine">music</span>
        <span class="m-3" id="ten" @click="getMovieRecommendTen"
          >mysteries</span
        >
      </h3>
      <br />
    </div>
    <b-form @submit.prevent="onSubmit">
      <b-form-input
        list="input-list"
        id="input-with-list"
        v-model="searchMovie"
        placeholder="Which movie are you looking for?"
        trim
      ></b-form-input>
      <b-form-datalist id="input-list" v-if="searchMovie">
        <option v-for="(movie, index) in movies" :key="index">
          {{ movie.title }}
        </option>
      </b-form-datalist>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
import NavBarVue from "@/components/NavBar.vue";

export default {
  name: "SearchView",
  components: {
    NavBarVue,
  },
  data() {
    return {
      mood: null,
      text: "",
      searchMovie: "",
      movies: [],
    };
  },
  methods: {
    onSubmit() {
      const movie = _.find(
        this.movies,
        (movie) => movie.title === this.searchMovie
      );
      if (!movie) return;
      this.$router.push({
        name: "MainView",
        params: { id: movie.id },
      });
      this.searchMovie = "";
    },
    getMovieRecommendOne() {
      const mood = document.getElementById("one").innerText;
      this.$store.dispatch("getMovieRecommendOne", mood);
      this.$router.push({ name: "RecommendView" });
    },
    getMovieRecommendTwo() {
      const mood = document.getElementById("two").innerText;
      this.$store.dispatch("getMovieRecommendTwo", mood);
      this.$router.push({ name: "RecommendView" });
    },
    getMovieRecommendThree() {
      const mood = document.getElementById("three").innerText;
      this.$store.dispatch("getMovieRecommendThree", mood);
      this.$router.push({ name: "RecommendView" });
    },
    getMovieRecommendFour() {
      const mood = document.getElementById("four").innerText;
      this.$store.dispatch("getMovieRecommendFour", mood);
      this.$router.push({ name: "RecommendView" });
    },
    getMovieRecommendFive() {
      const mood = document.getElementById("five").innerText;
      this.$store.dispatch("getMovieRecommendFive", mood);
      this.$router.push({ name: "RecommendView" });
    },
    getMovieRecommendSix() {
      const mood = document.getElementById("six").innerText;
      this.$store.dispatch("getMovieRecommendSix", mood);
      this.$router.push({ name: "RecommendView" });
    },
    getMovieRecommendSeven() {
      const mood = document.getElementById("seven").innerText;
      this.$store.dispatch("getMovieRecommendSeven", mood);
      this.$router.push({ name: "RecommendView" });
    },
    getMovieRecommendEight() {
      const mood = document.getElementById("eight").innerText;
      this.$store.dispatch("getMovieRecommendEight", mood);
      this.$router.push({ name: "RecommendView" });
    },
    getMovieRecommendNine() {
      const mood = document.getElementById("nine").innerText;
      this.$store.dispatch("getMovieRecommendNine", mood);
      this.$router.push({ name: "RecommendView" });
    },
    getMovieRecommendTen() {
      const mood = document.getElementById("ten").innerText;
      this.$store.dispatch("getMovieRecommendTen", mood);
      this.$router.push({ name: "RecommendView" });
    },
  },
  created() {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/v1/movies/",
    })
      .then((res) => {
        this.movies = Object.freeze(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  },
};
</script>

<style>
span {
  margin: 20px auto;
}
</style>
