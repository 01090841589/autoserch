<template>
  <div>
    <v-app-bar app fluid>
      <v-app-bar-nav-icon @click.stop="overlay = !overlay" />

      <v-toolbar-title @click="homeBtn" style="cursor:pointer;" id="title">AutoSearch</v-toolbar-title>

      <v-spacer />
      <!-- 모바일 버전 -->
      <v-card elevation="0" color="transparent" class="d-flex d-sm-none" width="1px">
        <v-card-actions>
          <v-spacer />
          <v-btn text large @click="search_overlay = !search_overlay">
            <v-icon>mdi-magnify</v-icon>
          </v-btn>

          <v-dialog v-model="search_overlay" width="500" height="50%">
            <v-card>
              <v-card-title class="headline grey lighten-2" primary-title>Search</v-card-title>
              <v-divider></v-divider>
              <v-card-text>
                <v-layout row class="justify-center">
                  <v-flex xs6>
                    <v-select
                      :value="$store.myValue"
                      @input="setSelected"
                      :items="selected_items"
                      label="select type"
                      color="black"
                    ></v-select>
                  </v-flex>
                  <v-flex xs12>
                    <v-text-field
                      flat
                      solo-inverted
                      hide-details
                      label="키워드를 입력해 주세요."
                      v-model="keyword"
                      @keyup.enter="
                        search(keyword), (search_overlay = !search_overlay)
                      "
                    ></v-text-field>
                  </v-flex>
                  <v-flex row wrap xs6 class="pl-3 pt-6 justify-center text-center">
                    <v-btn
                      @click="
                        search(keyword), (search_overlay = !search_overlay)
                      "
                      text
                      large
                    >
                      <v-icon>mdi-magnify</v-icon>Search right now!
                    </v-btn>
                  </v-flex>
                </v-layout>
              </v-card-text>
            </v-card>
          </v-dialog>
        </v-card-actions>
      </v-card>
      <!-- 검색 바(md 이상) -->
      <v-card elevation="0" color="transparent" class="hidden-xs-only" width="50vw">
        <v-card-actions>
          <v-row class="mt-3 mx-0">
            <v-col cols="2" class="pt-6 px-0">
              <v-select
                :value="$store.myValue"
                @input="setSelected"
                :items="selected_items"
                label="select"
                color="black"
              ></v-select>
            </v-col>
            <v-col cols="6" class="px-0">
              <v-text-field
                flat
                solo-inverted
                hide-details
                label="Search"
                v-model="keyword"
                @keyup.enter="search(keyword)"
              ></v-text-field>
            </v-col>
            <v-col cols="2" class="px-0">
              <v-btn @click="search(keyword)" text large>
                <v-icon>mdi-magnify</v-icon>
              </v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>
      <v-spacer />
    </v-app-bar>

    <v-overlay :value="overlay" opacity="0.8">
      <v-navigation-drawer absolute color="transparent" style="position:fixed;">
        <v-layout>
          <v-flex>
            <v-toolbar width="100%" absolute dense color="transparent" style="position:fixed;">
              <v-card color="white" light elevation="0">
                <v-icon
                  @click.stop="overlay = !overlay"
                  style="cursor:pointer;"
                  light
                >{{ leftArrowIcon }}</v-icon>
              </v-card>
              <!-- mdi-arrow-left, mdi-reply -->
            </v-toolbar>
          </v-flex>
          <v-flex absolute fill-height>
            <v-card fluid color="transparent" elevation="0">
              <br />
              <br />
              <v-list :key="updater">
                <v-list-item style="cursor:pointer" v-show="!isLogin">
                  <v-list-item-content>
                    <v-list-item-title>
                      <span class="display-1 text-shadow font-weight-bold">
                        <div>
                          <p id="effect" @click="moveLoginPage()">로그인</p>
                        </div>
                      </span>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item style="cursor:pointer" v-show="isLogin">
                  <v-list-item-content>
                    <v-list-item-title>
                      <span class="display-1 text-shadow font-weight-bold">
                        <div>
                          <p id="effect" @click="logOut()">로그아웃</p>
                        </div>
                      </span>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item style="cursor:pointer" v-show="isLogin">
                  <v-list-item-content>
                    <v-list-item-title>
                      <span class="display-1 text-shadow font-weight-bold">
                        <div>
                          <p id="effect" @click="moveMyPage()">마이페이지</p>
                        </div>
                      </span>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
                <v-list-item style="cursor:pointer" v-show="!isLogin">
                  <v-list-item-content>
                    <v-list-item-title>
                      <span class="display-1 text-shadow font-weight-bold">
                        <div>
                          <p id="effect" @click="moveSignUp()">회원가입</p>
                        </div>
                      </span>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-flex>
        </v-layout>
      </v-navigation-drawer>
    </v-overlay>
  </div>
</template>

<script>
import { mdiArrowLeftThick, mdiCrosshairsGps } from "@mdi/js";
export default {
  created() {
    this.isLogin = sessionStorage.getItem("token");
  },
  data: () => ({
    search_overlay: null,
    overlay: null,
    selected: "이름",
    selected_items: ["이름", "제조사"],
    keyword: "",
    updater: 0,
    isLogin: false,
    leftArrowIcon: mdiArrowLeftThick,
    gpsIcon: mdiCrosshairsGps,
    loginRoutePath: "/login",
    myPageRoutePath: "/MyPage"
  }),
  methods: {
    setSelected(value) {
      this.selected = value;
      console.log(this.selected);
    },
    search(keyword) {
      const data = { keyword: keyword, filter: this.selected };
      if (
        this.$router.currentRoute.path == `/search` &&
        this.$route.query.keyword == data.keyword
      ) {
        this.$router.go(0);
      } else {
        this.$router.push({
          path: "/search",
          query: { keyword: data.keyword, filter: data.filter }
        });
      }
    },
    homeBtn() {
      // console.log(this.$router.currentRoute.path);
      if (this.$router.currentRoute.path === "/") {
        this.$router.go(0);
      } else {
        this.$router.push("/");
      }
    },
    moveLoginPage() {
      this.overlay = false;
      this.$router.push(this.loginRoutePath);
    },
    moveMyPage() {
      this.overlay = false;
      this.$router.push(this.myPageRoutePath);
    },
    logOut() {
      this.overlay = false;
      sessionStorage.clear();
      this.updater++;
      this.$router.go(0);
    },
    moveSignUp() {
      this.overlay = false;
      this.$router.push("/signup");
    }
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Black+Han+Sans|Do+Hyeon|Jua|Nanum+Gothic|Sunflower:300");
#title {
  font-family: sans-serif;
}
#effect::before {
  width: 0;
  transition: width 0.1s ease-out;
}

#effect:hover:before {
  content: "";
  width: 80%;
  height: 30%;
  background-image: linear-gradient(
    to top,
    rgb(18, 192, 149) 30%,
    rgba(0, 0, 0, 0) 50%
  );
  position: absolute;
  left: 0;
  bottom: 10px;
  z-index: -1;
  will-change: width;
  transform: rotate(-2deg);
  transform-origin: left bottom;
  transition-duration: 0.15s;
}
</style>
