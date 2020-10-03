<template>
  <v-container fluid class="ma-0 pa-0">
    <NavBar />
    <v-layout mb-5>
      <Carousels></Carousels>
    </v-layout>

    <v-layout my-5 mx-5 row wrap>
      <v-flex md2 lg2 xs12>
        <SortedList></SortedList>
      </v-flex>
      <v-flex md10 lg10 xs12>
        <MainList></MainList>
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
import Carousels from "../../components/Carousels";
import MainList from "../../components/MainList";
import SortedList from "../../components/SortedList";
import BrandDrawer from "../../components/BrandDrawer";
export default {
  components: {
    NavBar,
    Carousels,
    MainList,
    SortedList,
    BrandDrawer
  }
};
</script>
