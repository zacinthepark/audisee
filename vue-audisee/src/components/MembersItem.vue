<template>
  <div>
    <h1>MembersItem</h1>
    <button @click="goMemberProfile">{{ user.id }}</button>
    {{ user.username }}
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
      return this.user.id
    },
    userName() {
      return this.user.username
    },
  },
  methods: {
    // test() {
    //   console.log(this.userId)
    // },
    goMemberProfile() {
      // console.log(this.userId)
      // console.log(this.userName)
      this.$store.commit("GET_MEMBER_NAME", this.userName)
      this.$store.dispatch("getMemberTracks", this.userId)
      this.$store.dispatch("getMemberMovies", this.userId)
      this.$router.push({ name: "MembersProfileView" })
    },
  },
}
</script>

<style></style>
