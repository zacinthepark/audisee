<template>
  <div>
    <h1>HomeView</h1>
    <h1>오늘은 어떤 영화를 시청하셨나요</h1>
    <h2>V</h2>
    <router-link :to="{ name: 'SearchView' }">SearchView</router-link>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style></style>
