<template>
  <v-container>
    <NavBar />
    <v-layout wrap justify-center>
      <v-flex lg4 sm6 md4 xs12>
        <v-card>
          <img :src="item.imagelink" alt width="340vw" />
        </v-card>
      </v-flex>
      <v-flex lg4 sm6 md4 xs12>
        <v-card>
          <v-card-title>{{ item.name }}</v-card-title>
          <v-card-subtitle>제조사: {{ item.company }}</v-card-subtitle>
          <v-card-text>
            <p>분류: {{ item.size }}</p>
            <p>출시가: {{ item.price }}</p>
            <p>연비: {{ item.fuel_eff }}</p>
            <p>연료: {{ item.engine }}</p>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout my-5>
      <v-flex lg12 md12 xs12>
        <v-divider />
        <p></p>
        <div class="text-center display-1">아니면 혹시 이들 중 하나인가요?</div>
        <CarImages :aiItems="aiItems"></CarImages>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import NavBar from "../../components/NavBar";
import CarImages from "../../components/CarImages";
export default {
  name: "result",
  components: {
    NavBar,
    CarImages
  },
  mounted() {
    this.makeList();
  },
  data: () => ({
    item: {},
    aiItems: []
  }),
  methods: {
    makeList() {
      const lst = this.$route.query.carList;
      for (const idx in lst) {
        if (idx == 0) {
          this.item = lst[idx];
        } else {
          this.aiItems.push(lst[idx]);
        }
      }
    }
  }
};
</script>

<style></style>
