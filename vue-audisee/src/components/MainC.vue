<template>
  <div class="p-5">
    <h3 class="fw-bold">{{ movie.title }} PREVIEW</h3>
    <hr />
    <div class="d-flex">
      <iframe
        class="me-5"
        :src="`http://www.youtube.com/embed/${this.video.id.videoId}`"
        frameborder="0"
        width="800"
        height="450"
      ></iframe>
      <div
        class="row border border-light border-2 rounded d-flex align-items-end"
      >
        <div class="p-4">
          <div class="text-start">
            <MainCReview
              v-for="(review, index) in reviews"
              :key="`review-${index}`"
              :review="review"
            />
          </div>
          <br />
          <form @submit.prevent="postReview">
            <input
              type="text"
              v-model="content"
              placeholder="리뷰를 작성해주세요"
            />
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MainCReview from "@/components/MainCReview.vue";

const API_URL = "https://www.googleapis.com/youtube/v3/search";
const API_KEY = "AIzaSyCI8t8M1ADPjcTTAuIOs3G2w-Nev9hXwRs";

export default {
  name: "MainC",
  components: {
    MainCReview,
  },
  data: function () {
    return {
      video: null,
      content: null,
    };
  },
  computed: {
    reviews() {
      return this.$store.state.movieReviews;
    },
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
          // console.log(this.video.id.videoId);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    postReview() {
      const content = this.content;
      if (!content) {
        alert("Empty Review!");
      } else {
        this.$store.dispatch("postReview", content);
      }
      this.content = null;
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
