<template>
  <div>
    <div class="card bg-transparent border-transparent" style="width: 18rem">
      <img class="rounded card-img-top" :src="myTrack.cover_path" alt="#" />

      <div class="card-body">
        <span>{{ myTrack.track_name }}</span>
        <button
          type="button"
          class="btn btn-outline-none fs-4 fw-bold btn-lg"
          style="color: red"
        >
          ❤
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfilePlaylist",
  props: {
    myTrack: Object,
  },
  components: {},
};
</script>

<style></style>
