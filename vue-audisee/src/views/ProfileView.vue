<template>
  <div>
    <h1>ProfileView</h1>
    <h1>ProfileMovies</h1>
    <ProfileLikeVue v-for="movie in myMovies" :key="movie.id" :my-movie="movie"/>
    <h1>ProfileTracks</h1>
    <ProfilePlaylistVue v-for="track in myTracks" :key="track.id" :my-track="track"/>
  </div>
</template>

<script>
import ProfileLikeVue from "@/components/ProfileLike.vue";
import ProfilePlaylistVue from "@/components/ProfilePlaylist.vue";

export default {
  name: "ProfileView",
  components: {
    ProfileLikeVue,
    ProfilePlaylistVue,
  },
  computed: {
    myMovies() {
      return this.$store.state.myMovies;
    },
    myTracks() {
      return this.$store.state.myTracks;
    },
  },
  created() {
    this.$store.dispatch('getMyMovies');
    this.$store.dispatch('getMyTracks');
  },
};
</script>

<style></style>
