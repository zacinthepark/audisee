<template>
  <div>
    <MainAItem
      :movie="movie"
      v-for="music in musics"
      :key="music.id"
      :music="music"
    />
  </div>
</template>

<script>
import MainAItem from "@/components/MainAItem.vue";

export default {
  name: "MainAItemList",
  components: {
    MainAItem,
  },
};
</script>

<style></style>
