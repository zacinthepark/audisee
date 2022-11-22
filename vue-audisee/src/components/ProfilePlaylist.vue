<template>
  <div>
    <div class="card bg-transparent border-transparent" style="width: 12rem">
      <img class="rounded card-img-top" :src="myTrack.cover_path" alt="#" />

      <div class="card-body">
        <span class="fs-5">{{ myTrack.track_name }}</span>
        <button
          type="button"
          class="btn btn-outline-none fs-5 fw-bold btn-lg"
          style="color: red"
        >
          x
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
  methods: {
    deleteMyTrack() {
      const track_id = this.myTrack.id
      this.$store.dispatch('deleteMyTrack', track_id)
    }
  },
};
</script>

<style></style>
