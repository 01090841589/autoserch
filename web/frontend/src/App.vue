<template>
  <v-app id="inspire" class="viewport">
    <v-content>
      <transition name="fade">
        <router-view :key="$route.fullPath"></router-view>
      </transition>
    </v-content>

    <BottomNav class="bottom-nav" />
    <!-- <v-footer app color="blue-grey" class="white--text">
      <span>SSAFY</span>
      <v-spacer />
      <span>&copy; 2020</span>
    </v-footer>-->
  </v-app>
</template>

<script>
import BottomNav from "./components/BottomNav";
// import { mdiArrowLeftThick, mdiCrosshairsGps } from "@mdi/js";
// import {
//   mdiCalendarTextOutline,
//   mdiAccountCircle,
//   mdiHelp,
//   mdiLockOpenVariant,
//   mdiLock,
// } from "@mdi/js";
export default {
  name: "App",
  props: {
    source: String,
  },

  components: {
    BottomNav,
  },
  created() {
    this.isLogin = sessionStorage.getItem("token");
  },
  // data: () => ({
  //   search_overlay: null,
  //   drawer: null,
  //   overlay: null,
  //   selected: "이름",
  //   selected_items: ["이름", "제조사"],
  //   left: false,
  //   keyword: "",
  //   updater: 0,
  //   isLogin: false,
  //   leftArrowIcon: mdiArrowLeftThick,
  //   gpsIcon: mdiCrosshairsGps,
  //   loginRoutePath: "/login",
  //   myPageRoutePath: "/MyPage",
  // }),
  //   methods: {
  //     setSelected(value) {
  //       this.selected = value;
  //       console.log(this.selected);
  //     },
  //     search(keyword) {
  //       const data = { keyword: keyword, filter: this.selected };

  //       // console.log(this.$route);
  //       console.log("fullpath:", this.$router.currentRoute.path);
  //       console.log("data, query:", data, this.$route.query.keyword);
  //       if (this.$router.currentRoute.path == `/search` && this.$route.query.keyword == data.keyword) {
  //         console.log("refreash");
  //         this.$router.go(0);
  //       } else {
  //         console.log("push to search");
  //         this.$router.push({
  //           path: "/search",
  //           query: { keyword: data.keyword, filter: data.filter },
  //         });
  //       }
  //     },
  //     homeBtn() {
  //       // console.log(this.$router.currentRoute.path);
  //       if (this.$router.currentRoute.path === "/") {
  //         this.$router.go(0);
  //       } else {
  //         this.$router.push("/");
  //       }
  //     },
  //     moveLoginPage() {
  //       this.overlay = false;
  //       this.$router.push(this.loginRoutePath);
  //     },
  //     moveMyPage() {
  //       this.overlay = false;
  //       this.$router.push(this.myPageRoutePath);
  //     },
  //     logOut() {
  //       this.overlay = false;
  //       sessionStorage.clear();
  //       this.updater++;
  //     },
  //     moveSignUp() {
  //       this.overlay = false;
  //       this.$router.push("/signup");
  //     },
  //   },
  //   watch: {
  //     checklogin: function() {
  //       console.log("LOGIN CHECK:", this.isLogin);
  //     },
  //   },
};
</script>

<style lang="scss" scoped>
@media (min-width: 1367px) {
  .bottom-nav {
    display: none;
  }
}
@media (max-width: 1366px) {
  .left-drawer {
    display: none;
  }
}

.filter {
  border: 1px solid black;
}

@import url("https://fonts.googleapis.com/css?family=Black+Han+Sans|Do+Hyeon|Jua|Nanum+Gothic|Sunflower:300");
#effect {
  font-family: "Do Hyeon", sans-serif;
}

// #effect {
//   text-transform: uppercase;
//   font-size: 36px;
//   color: white;
//   text-decoration: none;
//   position: relative;
// }
// [class^="link-"] {
//   display: inline-block;
// }
// .toolbarSize {
//   width: 30px;
// }
// .link-7 #effect:before {
//   content: "";
//   border-bottom: solid 1px white;
//   position: absolute;
//   bottom: 0;
//   left: 30%;
//   width: 0;
//   -webkit-transform: scale(0);
//   -moz-transform: scale(0);
//   -ms-transform: scale(0);
//   -o-transform: scale(0);
//   transform: scale(0);
// }
// .link-7 #effect:hover:before {
//   border-bottom: solid thin white;
//   width: 40%;
//   -webkit-animation: heartbeat-x 1.7s infinite ease-in;
//   animation: heartbeat-x 1.7s infinite ease-in;
// }

// .link-7 #effect:hover {
//   -webkit-animation: heartbeat 1.7s infinite ease-in;
//   animation: heartbeat 1.7s infinite ease-in;
// }

// @-webkit-keyframes heartbeat {
//   0% {
//     -webkit-transform: scale(1);
//   }
//   10% {
//     -webkit-transform: scale(1.1);
//   }
//   20% {
//     -webkit-transform: scale(1);
//   }
//   30% {
//     -webkit-transform: scale(1.1);
//   }
//   40% {
//     -webkit-transform: scale(1);
//   }
// }

// @-webkit-keyframes heartbeat-x {
//   0% {
//     -webkit-transform: scaleX(0);
//   }
//   10% {
//     -webkit-transform: scaleX(1);
//   }
//   20% {
//     -webkit-transform: scaleX(0);
//   }
//   30% {
//     -webkit-transform: scaleX(1);
//   }
//   40% {
//     -webkit-transform: scaleX(0);
//   }
// }

// @keyframes heartbeat {
//   0% {
//     transform: scale(1);
//   }
//   10% {
//     transform: scale(1.1);
//   }
//   20% {
//     transform: scale(1);
//   }
//   30% {
//     transform: scale(1.1);
//   }
//   40% {
//     transform: scale(1);
//   }
// }

// @keyframes heartbeat-x {
//   0% {
//     transform: scaleX(0);
//   }
//   10% {
//     transform: scaleX(1);
//   }
//   20% {
//     transform: scaleX(0);
//   }
//   30% {
//     transform: scaleX(1);
//   }
//   40% {
//     transform: scaleX(0);
//   }
// }
</style>
