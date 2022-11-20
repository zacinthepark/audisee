<template>
  <div class="container text-white">
    <div>
      <!-- 오빠야가 주는 장르 분위기 넣기 -->
      <h3>음산한 깜찍한 커여운</h3>
      <br />
      <h3>음산한 깜찍한 커여운 어쩌구</h3>
      <br />
      <h3>음산한 깜찍한 커여운</h3>
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

export default {
  name: "SearchView",
  data() {
    return {
      // 장르 넣기
      atmosphere: [
        "귀여운",
        "음산한",
        "깜찍한",
        "보리차",
        "광동밀",
        "국산보",
        "어린밀",
        "영양정",
        "서초구",
        "액상차",
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
