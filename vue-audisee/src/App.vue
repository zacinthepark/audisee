<template>
  <div id="app">
    <!-- NavBar 자체를 로그인 되면 보이게 추후 수정 -->
    <NavBar />
    <div class="m-5 p-5">
      <router-view />
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
};
</script>

<style>
@font-face {
  font-family: "LineSeed";
  src: url("./assets/fonts/LINESeedKR-Bd.ttf") format("woff");
  font-weight: 700;
  font-style: normal;
}
@font-face {
  font-family: "LineSeed";
  src: url("./assets/fonts/LINESeedKR-Rg.ttf") format("woff");
  font-weight: 400;
  font-style: normal;
}
@font-face {
  font-family: "LineSeed";
  src: url("./assets/fonts/LINESeedKR-Th.ttf") format("woff");
  font-weight: 100;
  font-style: normal;
}

#app {
  text-align: center;
  font-size: 50px;
  font-family: font_thin;
}
</style>
