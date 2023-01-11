<template>
  <div class="text-white">
    <NavBarVue />

    <h1 class="fw-bold">MY PROFILE</h1>
    <h3 class="p-3 mt-5 mb-2 text-start">
      LIKED {{ myMoviesLengthData }} MOVIES
    </h3>
    <div class="row row-cols-1 row-cols-md-6 g-4 fs-6">
      <ProfileLikeVue
        v-for="movie in myMoviesData"
        :key="movie.id"
        :my-movie="movie"
      />
    </div>
    <h3 class="p-3 mt-5 mb-2 text-start">
      LIKED {{ myTracksLengthData }} TRACKS
    </h3>
    <div class="row row-cols-1 row-cols-md-6 g-4 fs-6">
      <ProfilePlaylistVue
        v-for="track in myTracksData"
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
  data() {
    return {
      myMoviesData: [],
      myTracksData: [],
      myMoviesLengthData: null,
      myTracksLengthData: null,
    }
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
  watch: {
    myMovies(val) {
      this.myMoviesData = val
      this.updateData()
    },
    myTracks(val) {
      this.myTracksData = val
      this.updateData()
    },
    myMoviesLength(val) {
      this.myMoviesLengthData = val
    },
    myTracksLength(val) {
      this.myTracksLengthData = val
    },
  },
  methods: {
    updateData() {
      this.myMoviesData = this.myMovies
      this.myTracksData = this.myTracks
      this.myMoviesLengthData = this.myMoviesLength
      this.myTracksLengthData = this.myTracksLength
    },
  },
  created() {
    this.$store.dispatch("getMyMovies");
    this.$store.dispatch("getMyTracks");
    this.updateData();
  },
  // updated() {
  //   this.$store.dispatch("getMyMovies");
  //   this.$store.dispatch("getMyTracks");
  // },
};
</script>

<style></style>
