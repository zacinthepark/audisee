<template>
  <div>
    <NavBarVue />

    <h1>PlaylistView</h1>
    <PlaylistItemVue />
  </div>
</template>

<script>
import PlaylistItemVue from "@/components/PlaylistItem.vue";
import NavBarVue from "@/components/NavBar.vue";

export default {
  name: "PlaylistView",
  components: {
    PlaylistItemVue,
    NavBarVue,
  },
};
</script>

<style></style>
