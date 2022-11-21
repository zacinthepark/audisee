<template>
  <div>
    <h6>{{ myTrack.track_name }}</h6>
  </div>
</template>

<script>
export default {
  name: "ProfilePlaylist",
  props: {
    myTrack: Object,
  }
};
</script>

<style></style>
