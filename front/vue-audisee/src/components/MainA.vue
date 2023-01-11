<template>
  <div class="row justify-content-start">
    <div class="col-3 bg-red text-start">
      <br />
      <br />
      <span class="fw-light pe-3">나를 위한 새로운 발견 </span>
      <span>
        <button
          type="button"
          class="btn btn-outline-primary"
          @click="updateRecommendations"
        >
          <b-icon icon="arrow-counterclockwise"></b-icon>
        </button>
      </span>
      <br />
      <h3 class="fw-normal">{{ movie.title }}</h3>
      <h3 class="fw-normal">추천 음악</h3>
      <br />
      <div class="opacity-75">
        <div class="d-inline pe-2">총 50 곡</div>
        |
        <div class="d-inline ps-2">{{ nowDate }}</div>
      </div>
    </div>
    <div class="col-9">
      <VueSlickCarousel v-bind="settings">
        <MainAItem
          :movie="movie"
          v-for="(music, index) in musics"
          :key="`music-${index}`"
          :music="music"
        />
      </VueSlickCarousel>
    </div>
  </div>
</template>

<script>
import MainAItem from "@/components/MainAItem";
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
// optional style for arrows & dots
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";

export default {
  name: "MainA",
  components: {
    MainAItem,
    VueSlickCarousel,
  },
  props: {
    movie: Object,
  },
  computed: {
    musics() {
      return this.$store.state.recommendedMusics;
    },
  },
  data() {
    return {
      timer: null,
      nowDate: "",
      settings: {
        infinite: true,
        slidesToShow: 4,
        speed: 500,
        rows: 2,
        slidesPerRow: 1,
      },
    };
  },
  mounted() {
    this.timer = setInterval(() => {
      this.setNowTimes();
    }, 1000);
  },
  methods: {
    setNowTimes() {
      let myDate = new Date();
      let yy = String(myDate.getFullYear());
      let mm = myDate.getMonth() + 1;
      let dd = String(
        myDate.getDate() < 10 ? "0" + myDate.getDate() : myDate.getDate()
      );
      this.nowDate = yy + "-" + mm + "-" + dd;
    },
    updateRecommendations() {
      this.$store.dispatch("getMusicRecommendation");
    },
  },
};
</script>

<style></style>
