<template>
  <div>
    {{ review.username }}님 :
    {{ review.content }}
    <!-- <form @submit.prevent="postReview">
      <input type="text" v-model="content">
    </form> -->
  </div>
</template>

<script>
export default {
  name: "MainCReview",
  data() {
    return {
      content: null,
    };
  },
  methods: {
    // postReview() {
    //   const content = this.content
    //   if (!content) {
    //     alert('Empty Review!')
    //   } else {
    //     this.$store.dispatch("postReview", content)
    //   }
    // },
  },
  props: {
    review: Object,
  },
};
</script>

<style></style>
