<template>
  <v-overlay opacity="0.8">

  <div>
  <vue-typer class="loading"
    :text='["로딩중 입니다...", "정보를 가져오는 중입니다..."]'
    :repeat='Infinity'
    :shuffle='false'
    initial-action='typing'
    :pre-type-delay='70'
    :type-delay='100'
    :pre-erase-delay='2000'
    :erase-delay='250'
    erase-style='clear'
    :erase-on-complete='false'
></vue-typer>
  </div>

<br>
<br>
<div class="midalign">
  <v-progress-circular
      :size="200"
      :width="15"
      color="white"
      indeterminate
    ></v-progress-circular>
</div>
  </v-overlay>
</template>

<script>
import { VueTyper } from 'vue-typer'
export default {
  components: {
    VueTyper,
  },
  data() {
    return {
    }
  },
 mounted() {

 }
}
</script>

<style lang="scss">
  .loading{
    font-size: 3rem;
  }
  .vue-typer .char{
  color: white !important;
  }
  .midalign{
    display: inline-block;
    text-align: center;
  }
</style>
