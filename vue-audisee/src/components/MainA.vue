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
        <div class="d-inline ps-2">{{ nowDate }}</div>
      </div>
    </div>
    <div class="col">
      <MainAItemList />
    </div>
  </div>
</template>

<script>
import MainAItemList from "@/components/MainAItemList";
// import "swiper/dist/css/swiper.css";
// import { Swiper, directive } from "vue-awesome-swiper";

export default {
  name: "MainA",
  components: {
    MainAItemList,
    // Swiper,
  },
  // directives: {
  //   swiper: directive,
  // },
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
      // swiperOption: {
      //   slidesPerView: 6,
      //   spaceBetween: 5,
      //   slidesPerGroup: 5,
      //   loopFillGroupWithBlank: true,
      //   pagination: {
      //     el: ".swiper-pagination",
      //     clickable: true,
      //   },
      //   navigation: {
      //     nextEl: ".swiper-button-next",
      //     prevEl: ".swiper-button-prev",
      //   },
      // },
      timer: null,
      nowDate: "",
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
  },
};
</script>

<style></style>
