<template>
  <div class="row justify-content-start">
    <div class="col-3 bg-red text-start">
      <br />
      <br />
      <h6 class="fw-light">나를 위한 새로운 발견</h6>
      <br />
      <h3 class="fw-normal">{{ movie.title }}</h3>
      <h3 class="fw-normal">추천 음악</h3>
      <br />
      <div class="opacity-75">
        <div class="d-inline pe-2">총 40 곡</div>
        |
        <div class="d-inline ps-2">2022.11.16</div>
      </div>
    </div>
    <div class="col">
      <Swiper class="swiper" :options="swiperOption">
        <MainAItem
          :movie="movie"
          v-for="music in musics"
          :key="music.id"
          :music="music"
        />
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </Swiper>
    </div>
  </div>
</template>

<script>
import MainAItem from "@/components/MainAItem";
// import "swiper/dist/css/swiper.css";
import { Swiper, directive } from "vue-awesome-swiper";

export default {
  name: "MainA",
  components: {
    MainAItem,
    Swiper,
  },
  directives: {
    swiper: directive,
  },
  props: {
    movie: Object,
  },
  computed: {
    musics() {
      return this.$store.state.musics;
    },
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 6,
        spaceBetween: 5,
        slidesPerGroup: 5,
        loopFillGroupWithBlank: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true,
        },
        navigation: {
          nextEl: ".swiper-button-next",
          prevEl: ".swiper-button-prev",
        },
      },
    };
  },
};
</script>

<style></style>
