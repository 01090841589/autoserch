<template>
  <div>
    <v-container>
      <NavBar />

      <!-- 내 프로필 카드 -->
      <v-layout my-5 row wrap>
        <v-flex xs12>
          <MyProfile></MyProfile>
        </v-flex>
      </v-layout>
      <!-- 내 관심 차량 -->
      <v-layout my-5>
        <v-flex lg12 md12 xs12>
          <v-divider />
          <v-content>
            <h1 class="display-2 font-weight-light">The List Of My Like Car</h1>
            <div class="subheading text-uppercase pl-4 mb-6">Finding Beauty, One flight at a time</div>
          </v-content>
          <MyLike></MyLike>
        </v-flex>
        <v-flex>
          <BrandDrawer></BrandDrawer>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import NavBar from "../../components/NavBar";
import MyProfile from "@/components/MyProfile.vue";
import MyLike from "@/components/MyLike.vue";
import BrandDrawer from "../../components/BrandDrawer";
export default {
  name: "MyPage",
  components: {
    NavBar,
    MyProfile,
    MyLike,
    BrandDrawer,
  },
  data() {
    return {};
  },
};
</script>

<style></style>
