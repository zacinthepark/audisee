<template>
  <!-- Background image -->
  <div class="container" style="height: 70vh">
    <div class="d-flex justify-content-center align-items-center h-100">
      <div class="text-white">
        <h1 class="mb-3 fw-normal">오늘은 어떤 영화를 시청하셨나요</h1>
        <br />
        <!-- 라우터 링크 하얀색으로 바꾸기 -->
        <router-link :to="{ name: 'SearchView' }">
          <b-iconstack animation="cylon-vertical" rotate="90">
            <b-icon stacked icon="chevron-right" shift-h="-4"></b-icon>
            <b-icon stacked icon="chevron-right" shift-h="0"></b-icon>
            <b-icon stacked icon="chevron-right" shift-h="4"></b-icon>
          </b-iconstack>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style></style>
