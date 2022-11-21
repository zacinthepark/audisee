<template>
  <div>
    <h1>ProfileView</h1>
    <h1>ProfileLike</h1>
    <ProfileLikeVue v-for="movie in myMovies" :key="movie.id" :my-movie="movie"/>
    <ProfilePlaylistVue />
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
    }
  },
  created() {
    this.$store.dispatch('getMyMovies');
  },
};
</script>

<style></style>
