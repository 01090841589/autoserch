<template>
  <div class="text-center">
    <h1>정상적으로 탈퇴 되었습니다.</h1>
    <h1></h1>
    <h1></h1>
    <div align="center">
      <router-link :to="{name: 'main'}">
        <v-btn color="blue" dark @click="sheet3 = !sheet3" lg="8">
          <h3>홈으로</h3>
        </v-btn>
      </router-link>
      <router-link :to="{name: 'signUp'}">
        <v-btn large color="green">
          <h3>회원 가입</h3>
        </v-btn>
      </router-link>
      <router-link :to="{name: 'login'}">
        <v-btn color="blue" dark @click="sheet3 = !sheet3" lg="8">
          <h3>로그인</h3>
        </v-btn>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>