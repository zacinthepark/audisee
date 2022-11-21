<template>
  <div class="p-5">
    <iframe
      :src="`http://www.youtube.com/embed/${this.video.id.videoId}`"
      frameborder="0"
      width="700"
      height="350"
    ></iframe>
    <h3>{{ movie.title }} 예고편</h3>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "https://www.googleapis.com/youtube/v3/search";
const API_KEY = "AIzaSyCI8t8M1ADPjcTTAuIOs3G2w-Nev9hXwRs";

export default {
  name: "MainC",
  data: function () {
    return {
      video: null,
    };
  },
  props: {
    movie: Object,
  },
  methods: {
    movieTrailer() {
      const params = {
        key: API_KEY,
        part: "snippet",
        type: "video",
        q: `${this.movie.title} trailer`,
      };

      axios({
        method: "get",
        url: API_URL,
        params: params,
      })
        .then((res) => {
          this.video = res.data.items[0];
          console.log(this.video.id.videoId);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.movieTrailer();
  },
  // computed: {
  //   videoUrl() {
  //     const videoId = this.video.id.videoId;
  //     return `http://www.youtube.com/embed/${videoId}`;
  //   },
  // },
};
</script>

<style></style>
