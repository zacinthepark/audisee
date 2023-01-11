<template>
  <div class="text-white d-inline-flex m-5 border border-2 rounded">
    <div>
      <div @click="goMemberProfile" class="m-3 p-3">
        <b-icon icon="person-fill" scale="2"></b-icon>
      </div>
      <span class="fs-4">{{ user.username }} 님</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "MembersItemVue",
  props: {
    user: Object,
  },
  computed: {
    userId() {
      return this.user.id;
    },
    userName() {
      return this.user.username;
    },
  },
  methods: {
    // test() {
    //   console.log(this.userId)
    // },
    goMemberProfile() {
      // console.log(this.userId)
      // console.log(this.userName)
      this.$store.commit("GET_MEMBER_NAME", this.userName);
      this.$store.dispatch("getMemberTracks", this.userId);
      this.$store.dispatch("getMemberMovies", this.userId);
      this.$router.push({ name: "MembersProfileView" });
    },
  },
};
</script>

<style></style>
