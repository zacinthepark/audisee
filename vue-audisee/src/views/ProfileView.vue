<template>
  <div class="text-white">
    <NavBarVue />

    <h1 class="fw-bold">나 의 프로필</h1>
    <h3 class="p-3 mt-5 mb-2 text-start">
      총 {{ myMoviesLength }}개의 영화를 좋아해요
    </h3>
    <div class="row row-cols-1 row-cols-md-6 g-4 fs-6">
      <ProfileLikeVue
        v-for="movie in myMovies"
        :key="movie.id"
        :my-movie="movie"
      />
    </div>
    <h3 class="p-3 mt-5 mb-2 text-start">
      총 {{ myTracksLength }}개의 음악이 마음에 들어요
    </h3>
    <div class="row row-cols-1 row-cols-md-6 g-4 fs-6">
      <ProfilePlaylistVue
        v-for="track in myTracks"
        :key="track.id"
        :my-track="track"
      />
    </div>
  </div>
</template>

<script>
import ProfileLikeVue from "@/components/ProfileLike.vue";
import ProfilePlaylistVue from "@/components/ProfilePlaylist.vue";
import NavBarVue from "@/components/NavBar.vue";

export default {
  name: "ProfileView",
  components: {
    ProfileLikeVue,
    ProfilePlaylistVue,
    NavBarVue,
  },
  computed: {
    myMovies() {
      return this.$store.state.myMovies;
    },
    myTracks() {
      return this.$store.state.myTracks;
    },
    myMoviesLength() {
      return this.$store.getters.myMovieCount;
    },
    myTracksLength() {
      return this.$store.getters.myTrackCount;
    },
  },
  created() {
    this.$store.dispatch("getMyMovies");
    this.$store.dispatch("getMyTracks");
  },
  updated() {
    // this.$store.dispatch("getMyMovies");
    // this.$store.dispatch("getMyTracks");
  },
};
</script>

<style></style>
