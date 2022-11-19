<template>
  <div>
    <h1>RecommendView</h1>
    <p>{{ movie.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'RecommendItem',
  props: {
    movie: Object,
  }
};
</script>

<style></style>
