<template>
  <v-bottom-navigation dark shift fixed grow>
    <v-btn v-if="isLogin">
      <span>Log out</span>
      <v-icon>mdi-logout-variant</v-icon>
    </v-btn>

    <v-btn v-else to="/login">
      <span>Log in</span>
      <v-icon>mdi-login-variant</v-icon>
    </v-btn>

    <v-btn to="/">
      <span>Home</span>
      <v-icon>mdi-home</v-icon>
    </v-btn>

    <v-btn to="/MyPage">
      <span>MyPage</span>
      <v-icon>mdi-account</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>

<script>
export default {
  name: "BottomNav",
  data: () => ({
    isLogin: false,
  }),
};
</script>

<style lang="scss" scoped>
.phone-viewport {
  z-index: 1;
  width: 100%;
  height: auto;
  display: inline-flex;
  align-items: flex-end;
  overflow: hidden;
  border-top: 0.01rem solid rgba(#000, 0.26);
  background: rgba(#ffffff, 1);
  md-icon {
    color: #009ff4;
  }
}
.md-bottom-bar.md-type-fixed .md-bottom-bar-item {
  max-width: none;
  min-width: 0 !important;
}
</style>
