<template>
  <div>
    <NavBarVue />
    <div class="container">
      <MembersItemVue
        v-for="(user, index) in users"
        :key="`user-${index}`"
        :user="user"
      />
    </div>
  </div>
</template>

<script>
import MembersItemVue from "@/components/MembersItem.vue";
import NavBarVue from "@/components/NavBar.vue";
import axios from "axios";

export default {
  name: "MembersView",
  components: {
    MembersItemVue,
    NavBarVue,
  },
  data() {
    return {
      users: [],
    };
  },
  created() {
    axios({
      method: "get",
      url: "http://127.0.0.1:8000/users/",
    })
      .then((response) => {
        // console.log(response)
        this.users = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style></style>
