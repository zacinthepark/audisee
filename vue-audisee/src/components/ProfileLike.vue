<template>
  <div>
    <h6>{{ myMovie.title }}</h6>
  </div>
</template>

<script>
export default {
  name: "ProfileLike",
  props: {
    myMovie: Object,
  }
};
</script>

<style></style>
