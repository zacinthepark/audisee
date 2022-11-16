<template>
  <div>
    <h1>PlaylistView</h1>
    <PlaylistItemVue />
  </div>
</template>

<script>
import PlaylistItemVue from "@/components/PlaylistItem.vue";

export default {
  name: "PlaylistView",
  components: {
    PlaylistItemVue,
  },
};
</script>

<style></style>
