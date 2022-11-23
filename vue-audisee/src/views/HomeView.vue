<!-- Background image -->
<template>
  <div>
    <div class="wrapper">
      <div class="content">
        <h2>AUDISEE</h2>
        <h2>AUDISEE</h2>
      </div>
    </div>
    <br />
    <div>
      <b-iconstack font-scale="2" animation="cylon" @click="goSearch">
        <b-icon
          stacked
          icon="caret-right-fill"
          shift-h="-8"
          style="color: #8ab1f2"
        ></b-icon>
        <b-icon
          stacked
          icon="caret-right-fill"
          shift-h="0"
          style="color: #8ab1f2"
        ></b-icon>
        <b-icon
          stacked
          icon="caret-right-fill"
          shift-h="8"
          style="color: #8ab1f2"
        ></b-icon>
      </b-iconstack>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
  methods: {
    goSearch() {
      this.$router.push({ name: "SearchView" });
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900");

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}

.wrapper {
  display: flex;
  /* background: #000; */
  min-height: 50vh;
  align-items: center;
  justify-content: center;
}

.content {
  position: relative;
}

.content h2 {
  color: #fff;
  font-size: 8em;
  position: absolute;
  transform: translate(-50%, -50%);
}

.content h2:nth-child(1) {
  color: transparent;
  -webkit-text-stroke: 2px #8ab1f2;
}

.content h2:nth-child(2) {
  color: #8ab1f2;
  animation: animate 4s ease-in-out infinite;
}

@keyframes animate {
  0%,
  100% {
    clip-path: polygon(
      0% 45%,
      16% 44%,
      33% 50%,
      54% 60%,
      70% 61%,
      84% 59%,
      100% 52%,
      100% 100%,
      0% 100%
    );
  }

  50% {
    clip-path: polygon(
      0% 60%,
      15% 65%,
      34% 66%,
      51% 62%,
      67% 50%,
      84% 45%,
      100% 46%,
      100% 100%,
      0% 100%
    );
  }
}
</style>
