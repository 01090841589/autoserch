<template>
  <div>
    <v-layout wrap>
      <!-- 차량 리스트 -->
      <v-col v-for="mylikecar in mylikecars" :key="mylikecar.id" :cols="12" :md="3">
        <v-card>
          <v-img
            :src="mylikecar.imagelink"
            class="white--text align-end"
            gradient="to bottom, rgba(0,0,0,.1), rgba(1,2,2,.3)"
            height="300px"
          >
            <v-card-text>
              <br />
              <div class="subtitle-1 font-weight-bold">
                {{mylikecar.company}}
                <br />
                {{ mylikecar.price }}만원
                <br />
                {{mylikecar.fuel_eff}}
              </div>
            </v-card-text>
            <v-card-actions>
              <v-chip
                label
                class="mx-1 mb-3"
                color="grey darken-3"
                text-color="white"
                @click="carDetail(mylikecar.id)"
              >{{ mylikecar.name }}</v-chip>
              <v-spacer></v-spacer>
              <v-btn icon @click="deletelike(mylikecar.id)">
                <v-icon>mdi-heart-broken</v-icon>
              </v-btn>
            </v-card-actions>
          </v-img>
        </v-card>
      </v-col>
    </v-layout>
  </div>
</template>

<script>
import ContentsApi from "../apis/ContentsApi";
export default {
  name: "MyLike",
  data() {
    return {
      mylikecars: [{}]
    };
  },
  mounted() {
    this.init();
  },
  methods: {
    init() {
      this.mylikecars = [];
      this.mylikecars = JSON.parse(sessionStorage.getItem("mylikecars"));
    },
    deletelike(car_id) {
      if (sessionStorage.getItem("id") == null) {
        alert("로그인 해주세요");
      } else {
        ContentsApi.likecarUserlike(car_id, async res => {
          console.log(res.data);
          this.mylikecars = res.data;
          sessionStorage.setItem("mylikecars", JSON.stringify(this.mylikecars));

          await this.init();
        }),
          error => {
            console.log(error);
          };
      }
    },
    carDetail(car_id) {
      this.$router.push({ path: "/detail", query: { id: car_id } });
    }
  }
};
</script>

<style>
</style>