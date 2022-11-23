<template>
  <div
    class="card h-100 bg-transparent border-transparent"
    style="width: 18rem"
  >
    <img class="rounded card-img-top" :src="music.cover_path" alt="#" />

    <div class="card-body">
      <span>{{ music.track_name }}</span>
      <button
        type="button"
        class="btn btn-outline-none fs-5 fw-bold btn-lg"
        style="color: red"
        @click="addToMyTrack"
      >
        ❤
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import "swiper/dist/css/swiper.css";
// import { SwiperSlide } from "vue-awesome-swiper";

const API_URL = "http://127.0.0.1:8000";

export default {
  name: "MainAItem",
  // movie 프롭 받아놓음
  components: {
    // SwiperSlide,
  },
  props: {
    movie: Object,
    music: Object,
  },
  methods: {
    addToMyTrack() {
      const track_genre = this.music.track_genre;
      const track_name = this.music.track_name;
      const artist_name = this.music.artist_name;
      const album_name = this.music.album_name;
      const cover_path = this.music.cover_path;
      const preview_url = this.music.preview_url;
      axios({
        method: "post",
        url: `${API_URL}/playlist/tracks/`,
        data: {
          track_genre: track_genre,
          track_name: track_name,
          artist_name: artist_name,
          album_name: album_name,
          cover_path: cover_path,
          preview_url: preview_url,
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
};
</script>

<style></style>
