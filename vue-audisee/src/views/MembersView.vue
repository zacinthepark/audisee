<template>
  <div>
    <NavBar />

    <h1>MembersView</h1>
    <MembersItemVue />
  </div>
</template>

<script>
import MembersItemVue from "@/components/MembersItem.vue";

export default {
  name: "MembersView",
  components: {
    MembersItemVue,
  },
};
</script>

<style></style>
