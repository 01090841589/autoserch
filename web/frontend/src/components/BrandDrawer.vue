<template>
  <v-card class="overflow-hidden">
    <v-navigation-drawer
      expand-on-hover
      permanent
      absolute
      right
      style="position:fixed;top:100px; right:10px; scrollable{height:100%; overflow:auto;}"
      height="800"
      id="box"
      width="200"
    >
      <template v-slot:prepend>
        <v-list dense v-for="(item, idx) in items" :key="idx">
          <v-list-item
            v-for="(data, idx2) in item.children"
            :key="idx2"
            @click="search(data.name)"
            class="pl-3"
          >
            <v-list-item-avatar size="30">
              <v-img :src="data.imgUrl"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>
                <div class="underlined">{{ data.name }}</div>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </template>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
export default {
  name: "BrandDrawer",
  data() {
    return {
      items: [
        {
          icon: "keyboard-arrow-up",
          "icon-alt": "keyboard-arrow-down",
          text: "국산차",
          model: true,
          children: [
            {
              name: "현대",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20180529_88/auto_1527592677868AxMTJ_PNG/20180529201748_nbVe4EOk.png?type=f40_40"
            }, //현대
            {
              name: "기아",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_181/auto_149940895782493s0w_PNG/20170707152915_q71wMr3r.png?type=f40_40"
            }, //기아
            {
              name: "쌍용",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_290/auto_14994089867715m7Kc_PNG/20170707152945_ov1NwuMf.png?type=f40_40"
            }, //쌍용
            {
              name: "르노삼성",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_188/auto_14994089761732i2AM_PNG/20170707152934_4UQVPJ4f.png?type=f40_40"
            }, //르노삼성
            {
              name: "제네시스",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20200210_194/auto_158131011533438Psz_PNG/20200210134830_T0xCqY1D.png?type=f40_40"
            } //제네시스
          ]
        },
        {
          icon: "keyboard-arrow-up",
          "icon-alt": "keyboard-arrow-down",
          text: "해외차",
          model: false,
          children: [
            {
              name: "쉐보레",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20200210_175/auto_15813076774623FdaV_PNG/20200210130752_EvOsbnkP.png?type=f40_40"
            }, // 쉐보레)
            {
              name: "벤츠",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_151/auto_1499404806991Xuw2o_PNG/20170707142004_4ANaTv3h.png?type=f40_40"
            }, //벤츠
            {
              name: "BMW",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20200310_214/auto_1583815678479PKzIr_PNG/20200310134752_3hMT5CTc.png?type=f40_40"
            }, //bmw
            {
              name: "아우디",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_207/auto_1499404828979BICft_PNG/20170707142026_ovRGcdML.png?type=f40_40"
            }, //아우디
            {
              name: "폭스바겐",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20200422_10/auto_15875288567367G6VE_PNG/20200422131406_lmRMWJht.png?type=f40_40"
            }, //폭스바겐
            {
              name: "재규어",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20200210_83/auto_1581307501553E0yRR_PNG/20200210130456_nFc7LE10.png?type=f40_40"
            }, //재규어
            {
              name: "랜드로버",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_56/auto_1499407965482n6u8s_PNG/20170707151243_JgB80ept.png?type=f40_40"
            }, //랜드로버
            {
              name: "볼보",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_20/auto_1499407892646zwj3j_PNG/20170707151130_ECGx0tRI.png?type=f40_40"
            }, //볼보
            {
              name: "미니",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170718_248/auto_1500352107292eUlzC_PNG/20170718132824_jfupLnkX.png?type=f40_40"
            }, //미니
            {
              name: "토요타",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_157/auto_1499408657856g9GA0_PNG/20170707152416_RYNsQlax.png?type=f40_40"
            }, //토요타
            {
              name: "렉서스",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_52/auto_14994086479909zBvg_PNG/20170707152405_Q81trl9v.png?type=f40_40"
            }, //렉서스
            {
              name: "혼다",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_163/auto_1499412516283v1k4a_PNG/20170707162834_NTGXoypb.png?type=f40_40"
            }, //혼다
            {
              name: "닛산",
              imgUrl:
                "https://imgauto-phinf.pstatic.net/20170707_205/auto_1499412137135mBn5U_PNG/20170707162215_NaaURKNg.png?type=f40_40"
            } //닛산
          ]
        }
      ]
    };
  },
  methods: {
    search(keyword) {
      const data = { keyword: keyword, filter: "제조사" };

      // console.log(this.$route);
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
    }
  }
};
</script>
<style scoped>
#box {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
#box::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera*/
}
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
</style>
