<template>
  <div>
    <h1>ProfileView</h1>
    <ProfileLikeVue />
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
};
</script>

<style></style>
