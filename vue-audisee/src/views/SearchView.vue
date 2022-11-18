<template>
  <div class="container text-white">
    <div>
      <!-- 오빠야가 주는 장르 분위기 넣기 -->
      <h3>음산한 깜찍한 커여운</h3>
      <br />
      <h3>음산한 깜찍한 커여운 어쩌구</h3>
      <br />
      <h3>음산한 깜찍한 커여운</h3>
      <br />
    </div>
    <div class="mt-3 inputs">
      <i class="fa fa-search"></i>
      <input type="text" class="form-control" placeholder="Search Tasks..." />
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchView",
  data() {
    return {
      // 장르 넣기
      atmosphere: [
        "귀여운",
        "음산한",
        "깜찍한",
        "보리차",
        "광동밀",
        "국산보",
        "어린밀",
        "영양정",
        "서초구",
        "액상차",
      ],
      text: "",
    };
  },
};
</script>

<style></style>
