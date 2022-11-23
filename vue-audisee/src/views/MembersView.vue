<template>
  <div>
    <NavBarVue />

    <h1>MembersView</h1>
    <MembersItemVue />
  </div>
</template>

<script>
import MembersItemVue from "@/components/MembersItem.vue";
import NavBarVue from "@/components/NavBar.vue";

export default {
  name: "MembersView",
  components: {
    MembersItemVue,
    NavBarVue,
  },
};
</script>

<style></style>
