<template>
  <v-container>
    <NavBar></NavBar>
    <LoadingBar v-if="ImageOn" />
    <v-layout row wrap justify-center>
      <v-flex lg2 md2 xs12 sm12>
        <v-card elevation="0" class="justify-center text-center" style="border:1px solid;">
          <v-img :src="item.imagelink" />
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout row wrap justify-center text-center>
      <v-flex lg2 md2 xs12 sm12>
        <v-card elevation="0" class="justify-center text-center" style="border:1px solid;">
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title
                class="display-1 font-weight-bold justify-center text-center"
              >{{ item.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-title class="text-center">
              <div class="underlined">제조사</div>
            </v-list-item-title>
            <v-list-item-subtitle>{{ item.company }}</v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title class="text-center">
              <div class="underlined">출시가</div>
            </v-list-item-title>
            <v-list-item-subtitle>{{ item.price }}만</v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title class="text-center">
              <div class="underlined">연비</div>
            </v-list-item-title>
            <v-list-item-subtitle>{{ item.fuel_eff }}</v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title class="text-center">
              <div class="underlined">연료</div>
            </v-list-item-title>
            <v-list-item-subtitle class="text-center">
              {{
              item.engine
              }}
            </v-list-item-subtitle>
          </v-list-item>
          <v-list-item>
            <v-list-item-title class="text-center">
              <div class="underlined">분류</div>
            </v-list-item-title>
            <v-list-item-subtitle>{{ item.size }}</v-list-item-subtitle>
          </v-list-item>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex wrap lg12 sm12 md12 xs12>
        <v-divider />
        <p></p>
        <div class="text-center headline font-italic font-weight-light">
          <v-icon>{{ quoteopen }}</v-icon>이런 차는 어떠신가요?
          <v-icon>{{ quoteclose }}</v-icon>
        </div>
      </v-flex>
    </v-layout>
    <v-layout my-5>
      <v-flex wrap lg12 sm12 md12 xs12>
        <CarImages :aiItems="aiItems"></CarImages>
      </v-flex>
    </v-layout>
    <v-layout class="hidden-xs-only">
      <v-flex>
        <BrandDrawer></BrandDrawer>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import NavBar from "../../components/NavBar";
import ContentsApi from "../../apis/ContentsApi";
import CarImages from "../../components/CarImages";
import LoadingBar from "../../components/LoadingBar";
import BrandDrawer from "../../components/BrandDrawer";
import { mdiFormatQuoteClose, mdiFormatQuoteOpen } from "@mdi/js";
export default {
  name: "detail",
  components: {
    NavBar,
    CarImages,
    LoadingBar,
    BrandDrawer
  },
  created() {
    this.getItemDetail(this.$route.query.id);
  },
  data: () => ({
    item: {},
    result: {},
    aiItems: {},
    ImageOn: true,
    quoteclose: mdiFormatQuoteClose,
    quoteopen: mdiFormatQuoteOpen
  }),
  methods: {
    getItemDetail(id) {
      ContentsApi.requestCarDetail(
        id,
        async res => {
          console.log(res.data);
          this.item = res.data;
          const link = this.item.imagelink;
          this.ImageOn = true;
          await ContentsApi.requestCarAI(
            link,
            res => {
              console.log(res.data);
              this.aiItems = res.data;
              this.ImageOn = false;
            },
            error => {
              console.log(error);
              this.ImageOn = false;
            }
          );
        },
        error => {
          console.log(error);
          this.ImageOn = false;
        }
      );
      this.ImageOn = false;
    }
  },
  mounted() {}
};
</script>

<style lang="scss" scoped>
.underlined {
  text-decoration: none;
  font-weight: bold;
  font-size: 1.2em;
  position: relative;
  z-index: 1;
  display: inline-flex;
  padding-left: 10px;
  padding-bottom: 5px;
  padding-right: 10px;
}
.underlined::before {
  content: "";
  width: 100%;
  height: 80%;
  background-image: linear-gradient(to top, #fdbb2d 15%, rgba(0, 0, 0, 0) 25%);
  position: absolute;
  left: 0;
  bottom: 2px;
  z-index: -1;
  will-change: width;
  transform: rotate(-2deg);
  transform-origin: left bottom;
}
.main_img {
  background-size: cover;
  height: 40vh;

  .car_img {
    display: block;
    margin: 0px auto;
    width: 500px;
    padding-top: 10px;
  }
  @media (max-width: 768px) {
    .car_img {
      width: 500px;
      padding-top: 10px;
    }
  }

  @media (min-width: 992px) {
    .car_img {
      padding-top: 10px;
      width: 400px;
    }
  }

  @media (min-width: 1200px) {
    .car_img {
      padding-top: 10px;
      width: 450px;
    }
  }
}
.main_subs {
  height: 40vh;
}
</style>
