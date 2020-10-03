<template>
  <v-layout my-5>
    <v-flex lg12 md12 xs12>
      <v-card>
        <v-img
          :src="imagelink"
          class="white--text align-end"
          gradient="to bottom, rgba(0,0,0,.1), rgba(1,2,2,.3)"
          height="300px"
        >
          <v-card-text>
            <br />
            <div class="subtitle-1 font-weight-bold">
              {{ company }}
              <br />
              {{ price }}만원
              <br />
              {{ fuel_eff }}
            </div>
          </v-card-text>
          <v-card-actions>
            <v-chip
              label
              class="mx-1 mb-3"
              color="grey darken-3"
              text-color="white"
              @click="goDetail(id)"
            >{{ name }}</v-chip>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-img>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import UserApi from "../apis/UserApi";
export default {
  name: "carCard",
  props: ["id", "imagelink", "name", "company", "price", "fuel_eff", "engine"],
  created() {
    this.getLikeInfo();
  },
  data: () => ({
    isLike: false,
    icon: "mdi-heart-outline"
  }),
  methods: {
    goDetail(idx) {
      this.$router.push({ path: "/detail", query: { id: idx } });
    },
    getLikeInfo() {
      const likList = sessionStorage.getItem("likeList");

      if (this.id in likList) {
        this.isLike = true;
      } else {
        this.isLike = false;
      }
    },
    like() {
      this.isLike = !this.isLike;
      const data = {
        carId: this.id,
        userId: sessionStorage.getItem("id")
      };
      if (this.isLike) {
        this.icon = "mdi-heart";
        UserApi.requestLike(
          data,
          res => {
            const carItemList = res.data;
            for (const idx in carItemList) {
              const carItem = carItemList[idx];
              this.carItems.push(carItem);
            }
          },
          error => {
            console.log(error);
          }
        );
      } else {
        this.icon = "mdi-heart-outline";
      }
    }
  },
  watch: {
    iconWatch: function() {
      this.isLike;
    }
  }
};
</script>

<style>
.bottom-gradient {
  background-image: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.4) 0%,
    transparent 72px
  );
}

.repeating-gradient {
  background-image: repeating-linear-gradient(
    -45deg,
    rgba(255, 0, 0, 0.25),
    rgba(255, 0, 0, 0.25) 5px,
    rgba(0, 0, 255, 0.25) 5px,
    rgba(0, 0, 255, 0.25) 10px
  );
}
</style>
