<template>
  <div id="app">
    <NavBar />
    <p class="text-white">안녕하세요 인생이란 무엇인가</p>
    <router-view />
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
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

@font-face {
  font-family: "font_bold";
  src: url("./assets/fonts/LINESeedKR-Bd.ttf") format("woff2");
  font-weight: 100;
  font-style: normal;
}
@font-face {
  font-family: "font_regular";
  src: url("./assets/fonts/LINESeedKR-Rg.ttf") format("woff2");
  font-weight: 100;
  font-style: normal;
}
@font-face {
  font-family: "font_thin";
  src: url("./assets/fonts/LINESeedKR-Th.ttf") format("woff2");
  font-weight: 100;
  font-style: normal;
}

#app {
  text-align: center;
  font-size: 50px;
  font-family: font_thin;
}
</style>
