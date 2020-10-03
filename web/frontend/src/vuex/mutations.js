export default {
  checkLogin: function() {
    if (sessionStorage.getItem("token") != true) {
      this.$router.push("/login");
    }
  },
};
