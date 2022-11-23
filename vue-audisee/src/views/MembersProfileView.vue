<template>
  <div class="text-white">
    <NavBarVue />

    <h1 class="fw-bold">{{ memberName }}의 프로필</h1>
    <h3 class="p-3 mt-5 mb-2 text-start">
      총 {{ memberMoviesLength }}개의 영화를 좋아해요
    </h3>
    <div class="row row-cols-1 row-cols-md-6 g-4 fs-6">
      <MemberProfileLike
        v-for="(movie, index) in memberMovies"
        :key="`member-movie-${index}`"
        :member-movie="movie"
      />
    </div>
    <h3 class="p-3 mt-5 mb-2 text-start">
      총 {{ memberTracksLength }}개의 음악이 마음에 들어요
    </h3>
    <div class="row row-cols-1 row-cols-md-6 g-4 fs-6">
      <MemberProfilePlaylist
        v-for="(track, index) in memberTracks"
        :key="`member-track-${index}`"
        :member-track="track"
      />
    </div>
  </div>
</template>

<script>
import MemberProfileLike from "@/components/MemberProfileLike.vue"
import MemberProfilePlaylist from "@/components/MemberProfilePlaylist.vue"
import NavBarVue from "@/components/NavBar.vue"

export default {
  name: "MembersProfileView",
  components: {
    MemberProfileLike,
    MemberProfilePlaylist,
    NavBarVue,
  },
  computed: {
    memberName() {
      return this.$store.state.memberName
    },
    memberMovies() {
      return this.$store.state.memberMovies
    },
    memberTracks() {
      return this.$store.state.memberTracks
    },
    memberMoviesLength() {
      return this.$store.getters.memberMovieCount
    },
    memberTracksLength() {
      return this.$store.getters.memberTrackCount
    },
  },
  updated() {
    // this.$store.dispatch("getMyMovies");
    // this.$store.dispatch("getMyTracks");
  },
}
</script>

<style></style>
