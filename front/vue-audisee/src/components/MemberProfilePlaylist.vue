<template>
  <div>
    <div
      class="card h-100 bg-transparent border-transparent"
      style="width: 12rem"
    >
      <img class="rounded card-img-top" :src="memberTrack.cover_path" alt="#" />

      <div class="card-body">
        <span class="fs-5">{{ memberTrack.track_name }}</span>
        <!-- <button
          type="button"
          class="btn btn-outline-none fs-5 fw-bold btn-lg"
          style="color: red"
        >
          x
        </button> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MemberProfilePlaylist",
  props: {
    memberTrack: Object,
  },
}
</script>

<style></style>
