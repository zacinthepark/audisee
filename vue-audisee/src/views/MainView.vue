<template>
  <div class="text-white">
    <div class="d-flex">
      <b-container>
        <b-card-img class="rounded float-end" :src="`${poster_path}`" alt="#" />
      </b-container>
      <b-container>
        <br />
        <div class="mb-5 text-start">
          <h3>{{ title }}</h3>
          <h6 class="opacity-50">{{ release_date }}</h6>
          <br />
          <h6>{{ genre }}</h6>
          <h6>★ {{ vote_average }}</h6>
        </div>
      </b-container>
    </div>

    <MainAVue />
    <MainBVue />
    <MainCVue />
  </div>
</template>

<!-- title, genre, overview, release_date, poster_path, popularity, vote_count, vote_average -->

<script>
import MainAVue from "@/components/MainA.vue";
import MainBVue from "@/components/MainB.vue";
import MainCVue from "@/components/MainC.vue";

export default {
  name: "MainView",
  components: {
    MainAVue,
    MainBVue,
    MainCVue,
  },
  data() {
    return {
      title: "블랙팬서",
      genre: "큐티 섹시",
      overview: "어쩌구저쩌구 박진우 바보",
      release_date: "2014.02.14",
      poster_path: "https://newsimg.sedaily.com/2018/01/18/1RUH59AFMV_1.jpg",
      popularity: 121212121,
      vote_count: 2324351,
      vote_average: 4.5,
    };
  },
};
</script>

<style></style>
