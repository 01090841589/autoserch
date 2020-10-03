<template>
  <div>
    <v-layout row wrap>
      <v-flex xs12 lg4 class="text-center">
        <v-avatar class="profile" color="grey" size="164" @click="onClickFile">
          <v-img :src="'58.230.252.215:8000'+user.image" alt="profile"></v-img>
        </v-avatar>
      </v-flex>
      <input type="file" class="file-input" accept="image/*" ref="fileInput" @change="onFileChange" />
      <v-flex xs12 lg8>
        <v-list>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">mdi-phone</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{user.identify}}</v-list-item-title>
              <v-list-item-subtitle>identify</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">mdi-human</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{user.name}}</v-list-item-title>
              <v-list-item-subtitle>name</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-icon>
              <v-icon color="indigo">mdi-phone</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{user.nickname}}</v-list-item-title>
              <v-list-item-subtitle>nickname</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-list>
          <v-list-item>
            <v-btn @click="MyInfoBtnClick()">내 정보 수정</v-btn>
          </v-list-item>
        </v-list>
      </v-flex>
    </v-layout>
    <v-dialog v-model="MyInfoVisible" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">User Profile</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field label="identify*" readonly="user.id" v-model="user.identify"></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-text-field label="name*" required v-model="user.name"></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="Password*" v-model="password" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="PasswordConfirm*" v-model="passwordConfirm" required></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field label="nickname*" required v-model="user.nickname"></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="MyInfoBtnClick() ">Close</v-btn>
          <v-btn color="blue darken-1" text @click="updateuser() ">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import UserApi from "../apis/UserApi";
import Swal from "sweetalert2";
export default {
  name: "MyProfile",
  data() {
    return {
      uploadImage: "",
      filename: "",
      imageSrc: "",
      user: {
        id: sessionStorage.getItem("id"),
        identify: sessionStorage.getItem("identify"),
        name: sessionStorage.getItem("name"),
        nickname: sessionStorage.getItem("nickname"),
        image: sessionStorage.getItem("image")
      },
      password: "",
      passwordConfirm: "",
      update: {
        identify: "",
        name: "",
        nickname: "",
        password: ""
      },
      MyInfoVisible: false,
      passwordValid: false,
      idValid: false,
      isSubmit: false,
      message: ""
    };
  },
  methods: {
    updateuser() {
      this.checkForm();

      const formData = new FormData();
      formData.append("identify", this.user.identify);
      formData.append("password", this.password);
      formData.append("name", this.user.name);
      formData.append("nickname", this.user.nickname);
      formData.append("image", this.uploadImage);
      if (this.isSubmit == true) {
        UserApi.update(
          formData,
          res => {
            console.log(res);
            this.$router.push("/Mypage");
          },
          error => {
            console.log(error);
          }
        );
      } else {
        Swal.fire({
          icon: "error"
        });
        return;
      }
    },
    MyInfoBtnClick() {
      this.MyInfoVisible = !this.MyInfoVisible;
    },
    onClickFile(event) {
      console.log(event);
      this.$refs.fileInput.click();
    },
    onFileChange(event) {
      this.inputImageFile(event.target.files);
    },
    inputImageFile(files) {
      if (files.length) {
        let file = files[0];
        if (!/^image\//.test(file.type)) {
          alert("이미지 파일만 등록이 가능합니다");
          return false;
        }
        this.filename = file.name;
        this.uploadImage = file;
        this.preview(file);
      }
    },
    preview(file) {
      if (typeof file === "string") {
        this.imageSrc = file;
      } else {
        let vm = this;
        let reader = new FileReader();
        reader.onload = () => {
          vm.imageSrc = reader.result;
        };
        reader.readAsDataURL(file);
      }
    },
    checkPwd() {
      if (this.password == this.passwordConfirm) {
        this.passwordValid = true;
      } else {
        this.passwordValid = false;
        this.message = "비밀번호가 다릅니다";
      }
      if (this.password.length < 8) {
        this.message = "비밀번호를 8자리 이상으로 작성해주세요";
        this.passwordValid = false;
      } else if (this.passwordConfirm.length == 0) {
        this.message = "비밀번호를 한번 더 입력해주세요";
        this.passwordValid = false;
      }
    },
    checkForm() {
      this.isSubmit = true;
      this.checkPwd();

      if (this.passwordValid == false) {
        this.isSubmit = false;
      }
      if (this.user.nickname.length == 0) {
        this.message = "닉네임을 입력해주세요";
        this.isSubmit = false;
      }
      if (this.user.name.length == 0) {
        (this.message = "이름을 입력해주세요"), (this.isSubmit = false);
      }
      if (this.passwordConfirm.length == 0) {
        this.message = "비밀번호를 한번 더 입력해주세요";
        this.isSubmit = false;
      }
      if (this.password.length == 0) {
        this.message = "비밀번호를 입력해주세요";
        this.isSubmit = false;
      }
    }
  }
};
</script>

<style>
</style>