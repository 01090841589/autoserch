<template>
  <v-layout wrap>
    <v-flex v-for="item in aiItems" :key="item.id" lg2 sm2 md6 xs12>
      <v-hover v-slot:default="{ hover }">
        <v-card elevation="0" max-width="344" class="ma-auto">
          <v-img :src="item.imagelink" class="white--text" height="200px">
            <v-expand-transition>
              <div
                v-if="hover"
                class="d-flex transition-fast-in-fast-out grey darken-2 display-3 white--text justify-center"
                style="height: 100%; opacity:.8;"
              >
                <v-card-title v-text="item.name" @click="getDetail(item.id)"></v-card-title>
              </div>
            </v-expand-transition>
          </v-img>
        </v-card>
      </v-hover>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "CarImages",
  props: ["aiItems"],
  data() {
    return {};
  },
  methods: {
    getDetail(id) {
      this.$router.push({ path: "/detail", query: { id: id } });
    }
  }
};
</script>

<style scoped>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.5;
  position: absolute;
  width: 100%;
}
</style>
