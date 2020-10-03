<template>
  <v-container fluid>
    <v-data-iterator :items="items" :items-per-page.sync="itemsPerPage" hide-default-footer>
      <template v-slot:default="props">
        <v-toolbar class="mb-2" color="indigo darken-5" dark flat>
          <v-toolbar-title>마이 페이지</v-toolbar-title>
          <div class="text-center">
            <v-bottom-sheet v-model="sheet" inset>
              <template v-slot:activator="{ on }">
                <v-btn color="blue" dark v-on="on">개인 정보 수정하기</v-btn>
              </template>
              <v-sheet class="text-center" height="600px">
                <v-btn class="mt-6" text color="error" @click="sheet = !sheet">close</v-btn>
                <v-window v-model="step">
                  <v-card-text>
                    <v-text-field label="아이디" value></v-text-field>
                    <v-text-field label="비밀번호" type="password"></v-text-field>
                    <v-text-field label="비밀번호 확인" type="password"></v-text-field>
                    <v-text-field label="e-mail" value></v-text-field>
                    <v-text-field label="주소" value></v-text-field>
                    <v-text-field label="생년월일" value></v-text-field>
                  </v-card-text>
                  <router-link :to="{name: 'leave'}">
                    <v-btn large color="error">
                      <h3>회원 탈퇴</h3>
                    </v-btn>
                  </router-link>
                </v-window>
                <h3 class="title font-weight-light mb-2">Welcome to AutoSearch</h3>
                <span class="caption grey--text">Thanks for using our site!</span>
              </v-sheet>
            </v-bottom-sheet>
          </div>
        </v-toolbar>
        <v-row>
          <v-col
            v-for="item in props.items"
            :key="item.name"
            cols="20"
            sm="10"
            md="4"
            lg="10"
            offset-sm="1"
          >
            <v-card>
              <v-card-title class="subheading font-weight-bold">{{ item.name }}</v-card-title>

              <v-divider></v-divider>

              <v-list dense>
                <v-list-item>
                  <v-list-item-content>아이디:</v-list-item-content>
                  <v-list-item-content class="align-end">{{ item.myName }}</v-list-item-content>
                </v-list-item>

                <v-list-item>
                  <v-list-item-content>비밀번호:</v-list-item-content>
                  <v-list-item-content class="align-end">{{ item.password }}</v-list-item-content>
                </v-list-item>

                <v-list-item>
                  <v-list-item-content>e-mail:</v-list-item-content>
                  <v-list-item-content class="align-end">{{ item.email }}</v-list-item-content>
                </v-list-item>

                <v-list-item>
                  <v-list-item-content>주소:</v-list-item-content>
                  <v-list-item-content class="align-end">{{ item.address }}</v-list-item-content>
                </v-list-item>

                <v-list-item>
                  <v-list-item-content>생년월일:</v-list-item-content>
                  <v-list-item-content class="align-end">{{ item.birthday }}</v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
          </v-col>
        </v-row>

        <v-toolbar class="mb-2" color="indigo darken-5" dark flat>
          <v-toolbar-title>즐겨찾기한 자동차</v-toolbar-title>
        </v-toolbar>
        <v-row align="left">
          <v-col cols="50" sm="12" offset-sm="0">
            <v-card>
              <v-container fluid>
                <v-row align="left">
                  <v-col class="d-flex child-flex" cols="1" sm="1">
                    <v-card flat tile class="d-flex">
                      <div class="pa-1 text-center">
                        <v-img
                          class="mb-1"
                          contain
                          height="128"
                          src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTaN-ujXAbXuBt9dV8akS1Mgu2_L-nadEpxGUPsvPs_V4ObLIfj&usqp=CAU"
                        ></v-img>
                        <h3 class="title font-weight-light mb-2">My Car 1</h3>
                        <router-link :to="{name: 'login'}">
                          <v-btn color="blue" dark @click="sheet1 = !sheet1" lg="8">My Car 1 바로가기</v-btn>
                        </router-link>
                        <v-bottom-sheet v-model="sheet1">
                          <v-sheet class="text-center" height="200px">
                            <v-btn class="mt-6" text color="red" @click="sheet1 = !sheet1">close</v-btn>
                            <div class="py-3">My Car 1 페이지</div>
                          </v-sheet>
                        </v-bottom-sheet>
                      </div>
                      <div class="pa-1 text-center">
                        <v-img
                          class="mb-1"
                          contain
                          height="128"
                          src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRL-i91N289RHesU25SR38igUY9MQ_deDJtt_ROcfvpV6ilekzC&usqp=CAU"
                        ></v-img>
                        <h3 class="title font-weight-light mb-2">My Car 2</h3>
                        <router-link :to="{name: 'signUp'}">
                          <v-btn color="blue" dark @click="sheet2 = !sheet2" lg="8">My Car 2 바로가기</v-btn>
                        </router-link>
                        <v-bottom-sheet v-model="sheet2">
                          <v-sheet class="text-center" height="200px">
                            <v-btn class="mt-6" text color="red" @click="sheet2 = !sheet2">close</v-btn>
                            <div class="py-3">My Car 2 페이지</div>
                          </v-sheet>
                        </v-bottom-sheet>
                      </div>
                      <div class="pa-1 text-center">
                        <v-img
                          class="mb-1"
                          contain
                          height="128"
                          src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQWNxFt2_bMG73tliJic1dW6l4xQLmQXcM7lVxlk2niwnD-BoAA&usqp=CAU"
                        ></v-img>
                        <h3 class="title font-weight-light mb-2">My Car 3</h3>
                        <v-btn color="blue" dark @click="sheet3 = !sheet3" lg="8">My Car 3 바로가기</v-btn>
                        <v-bottom-sheet v-model="sheet3">
                          <v-sheet class="text-center" height="200px">
                            <v-btn class="mt-6" text color="red" @click="sheet3 = !sheet3">close</v-btn>
                            <div class="py-3">My Car 3 페이지</div>
                          </v-sheet>
                        </v-bottom-sheet>
                      </div>
                    </v-card>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-col>
          <v-col cols="50" sm="12" offset-sm="0">
            <v-card>
              <v-container fluid>
                <v-row>
                  <v-col class="d-flex child-flex" cols="1" sm="1">
                    <v-card flat tile class="d-flex">
                      <div class="pa-1 text-center">
                        <v-img
                          class="mb-1"
                          contain
                          height="128"
                          src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSpnNJjKe86ZKuHHLaBt2Awm-GkXRm3y6afgxGney8rCXwyHh1_&usqp=CAU"
                        ></v-img>
                        <h3 class="title font-weight-light mb-2">My Car 4</h3>
                        <v-btn color="blue" dark @click="sheet4 = !sheet4" lg="8">My Car 4 바로가기</v-btn>
                        <v-bottom-sheet v-model="sheet4">
                          <v-sheet class="text-center" height="200px">
                            <v-btn class="mt-6" text color="red" @click="sheet4 = !sheet4">close</v-btn>
                            <div class="py-3">My Car 4 페이지</div>
                          </v-sheet>
                        </v-bottom-sheet>
                      </div>
                      <div class="pa-1 text-center">
                        <v-img
                          class="mb-1"
                          contain
                          height="128"
                          src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQhB5OPB1UFzmvLEq7nhOFaORSLEQdWwGYwbs4nBvisUDTr0wsT&usqp=CAU"
                        ></v-img>
                        <h3 class="title font-weight-light mb-2">My Car 5</h3>
                        <v-btn color="blue" dark @click="sheet5 = !sheet5" lg="8">My Car 5 바로가기</v-btn>
                        <v-bottom-sheet v-model="sheet5">
                          <v-sheet class="text-center" height="200px">
                            <v-btn class="mt-6" text color="red" @click="sheet5 = !sheet5">close</v-btn>
                            <div class="py-3">My Car 5 페이지</div>
                          </v-sheet>
                        </v-bottom-sheet>
                      </div>
                      <div class="pa-1 text-center">
                        <v-img
                          class="mb-1"
                          contain
                          height="128"
                          src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSQs3AFEOSb75UAozVheO9XJb_Ml099g8YW_PuqxTeF-h7CmnHq&usqp=CAU"
                        ></v-img>
                        <h3 class="title font-weight-light mb-2">My Car 6</h3>
                        <v-btn color="blue" dark @click="sheet6 = !sheet6" lg="8">My Car 6 바로가기</v-btn>
                        <v-bottom-sheet v-model="sheet6">
                          <v-sheet class="text-center" height="200px">
                            <v-btn class="mt-6" text color="red" @click="sheet6 = !sheet6">close</v-btn>
                            <div class="py-3">My Car 6 페이지</div>
                          </v-sheet>
                        </v-bottom-sheet>
                      </div>
                    </v-card>
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-col>
        </v-row>
      </template>
    </v-data-iterator>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    sheet: false,
    sheet1: false,
    sheet2: false,
    sheet3: false,
    sheet4: false,
    sheet5: false,
    sheet6: false,
    itemsPerPage: 4,
    items: [
      {
        name: "내 정보",
        myName: 1111,
        password: 1234,
        email: 24,
        address: 124123,
        birthday: 930711
      }
    ]
  })
};
</script>