<template>
  <div class="notfound">
    <v-layout justify-center>
      <img :src="imgSrc" alt="" />
    </v-layout>
    <v-layout justify-center>
      <v-btn @click="back">
        <v-icon>mdi-arrow-left</v-icon>
        Back
      </v-btn>
    </v-layout>
  </div>
</template>

<script>
export default {
  name: "NotFound",
  data: () => ({
    imgSrc: require("../assets/images/404.png"),
  }),
  methods: {
    back() {
      this.$router.go(-1);
    },
  },
};
</script>

<style lang="scss" scoped>
.notfound {
  margin: auto;
}
</style>
