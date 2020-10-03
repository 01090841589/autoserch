<template>
  <div class="text-center">
    <h1>회원 가입</h1>

    <v-card class="mx-auto" max-width="500">
      <v-card-title class="title font-weight-regular justify-space-between">
        <span>{{ message }}</span>
      </v-card-title>
      <v-window>
        <v-avatar size="150" @click="onClickFile">
          <img :src="imageSrc" alt="profile" />
        </v-avatar>

        <v-card-text>
          <input
            type="file"
            class="file-input"
            accept="image/*"
            ref="fileInput"
            @change="onFileChange"
          />
          <v-text-field label="아이디" v-model="userId" value></v-text-field>
          <v-text-field
            label="비밀번호"
            type="password"
            v-model="password"
          ></v-text-field>
          <v-text-field
            label="비밀번호 확인"
            type="password"
            v-model="passwordConfirm"
          ></v-text-field>
          <v-text-field label="이름" v-model="userName" value></v-text-field>
          <v-text-field label="닉네임" v-model="nickName" value></v-text-field>
        </v-card-text>
        <div class="pa-4 text-center">
          <!-- <v-img
            class="mb-4"
            contain
            height="128"
            src="https://post-phinf.pstatic.net/MjAxOTAzMjBfMjY5/MDAxNTUzMDQ4MzgwMzgy.NdWfUZlmPgEr6I_MPh_OiDo9z2ewjX0dTvFz6Pc-ZBEg.Luu3cMmPBUTndKLJe5FGAaz1SiR9hCLbisWYCDIybg0g.JPEG/335790_17345_2048.jpg?type=w1200"
          ></v-img>-->
          <h3 class="title font-weight-light mb-2">Welcome to AutoSearch</h3>
          <span class="caption grey--text">Thanks for signing up!</span>
        </div>
      </v-window>

      <v-divider></v-divider>

      <v-card-actions>
        <v-btn @click="goBack">Back</v-btn>
        <v-spacer></v-spacer>
        <v-btn @click="signUp">SignUp</v-btn>
      </v-card-actions>
    </v-card>

    <v-btn color="blue" dark @click="sheet = !sheet">회원 가입 가이드</v-btn>
    <v-bottom-sheet v-model="sheet">
      <v-sheet class="text-center" height="200px">
        <v-btn class="mt-6" text color="red" @click="sheet = !sheet"
          >close</v-btn
        >
        <div class="py-3">
          아이디는 영문 기준 6자리 이상 20자리 이하, 비밀번호는 8자리 이상으로
          만들어주십시오.
        </div>
      </v-sheet>
    </v-bottom-sheet>
  </div>
</template>

<script>
import UserApi from "../apis/UserApi";
import Swal from "sweetalert2";
export default {
  data: () => ({
    sheet: false,
    userimage: "",
    userId: "",
    password: "",
    passwordConfirm: "",
    userName: "",
    nickName: "",
    passwordValid: false,
    idValid: false,
    isSubmit: false,
    message: "",
    uploadImage: "",
    filename: "",
    imageSrc:
      "data:image/png;base64,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",
  }),
  methods: {
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
    goBack() {
      this.$router.go(-1);
    },
    checkId() {
      if (20 >= this.userId.length && this.userId.length >= 6) {
        this.idValid = true;
      } else {
        this.idValid = false;
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
      this.checkId();
      this.checkPwd();

      if (this.idValid == false) {
        this.isSubmit = false;
      }
      if (this.passwordValid == false) {
        this.isSubmit = false;
      }
      if (this.nickName.length == 0) {
        this.message = "닉네임을 입력해주세요";
        this.isSubmit = false;
      }
      if (this.userName.length == 0) {
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
      if (this.userId.length == 0) {
        this.message = "아이디를 입력해주세요";
        this.isSubmit = false;
      }
      console.log("Valid Check:", this.isSubmit);
    },
    signUp() {
      this.checkForm();
      this.preview(this.filename);

      const formData = new FormData();
      formData.append("identify", this.userId);
      formData.append("password", this.password);
      formData.append("name", this.userName);
      formData.append("nickname", this.nickName);
      formData.append("image", this.uploadImage);
      if (this.isSubmit == true) {
        UserApi.join(
          formData,
          (res) => {
            console.log(res);
            this.$router.push("login");
          },
          (error) => {
            console.log(error);
          }
        );
      } else {
        Swal.fire({
          icon: "error",
          title: "회원가입 양식이 올바르지 않습니다"
        });
        return;
      }
    }
  },
  watch: {
    checkValid: function() {
      this.checkForm();
    }
  }
};
</script>
<style>
.file-input {
  display: none;
}
</style>
