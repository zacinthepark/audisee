<template>
  <!-- Background image -->
  <div
    class="p-5 text-center bg-image"
    style="
      /* 여기에 영화 사진 같은거 넣으면 좋을 거 같다
      하지만 그거하는 거 뭐 다 좋은데 배경 다크 투명도 넣어야댐 */
      background-image: url('https://mdbcdn.b-cdn.net/img/new/slides/041.webp');
      height: 500px;
    "
  >
    <router-link
      :to="{ name: 'LoginView' }"
      class="d-grid gap-2 d-md-flex justify-content-md-end text-decoration-none"
    >
      <button class="btn btn-outline-light" type="button">Login</button>
    </router-link>
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
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>

<style></style>
