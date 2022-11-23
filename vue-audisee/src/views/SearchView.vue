<template>
  <div class="container text-white">
    <NavBarVue />
    <div>
      <!-- 오빠야가 주는 장르 분위기 넣기 -->
      <h3>adventure animation humanism</h3>
      <br />
      <h3>
        <span @click="goRecommend">thrillers</span> actions comedy romance
      </h3>
      <br />
      <h3>history music mysteries</h3>
      <br />
    </div>
    <b-form @submit.prevent="onSubmit">
      <b-form-input
        list="input-list"
        id="input-with-list"
        v-model="searchMovie"
        placeholder="검색어를 입력하세요"
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
      // 장르 넣기
      atmosphere: [
        "adventure",
        "animation",
        "humanism",
        "thrillers",
        "actions",
        "happy",
        "history",
        "music",
        "mysteries",
      ],
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
    goRecommend() {
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

<style></style>
