<template>
  <v-container>
    <div id="uploader">
      <p>Input Image URL and Click the button or Drag and Drop or Attach an Image File</p>
      <div class="input-group">
        <input
          type="text"
          class="form-control"
          placeholder="Input Image URL or  Drag & Drop or Select"
          v-model="filename"
          @dragover.prevent
          @dragenter.prevent
          @drop.prevent="onDrop"
        />
        <div class="input-group-append">
          <span class="input-group-text" @click="onClickFile">
            <i class="fa fa-paperclip"></i>
          </span>
          <button class="btn btn-outline-info" @click="onClickUpload">Upload</button>
        </div>
        <input
          type="file"
          class="file-input"
          accept="image/*"
          ref="fileInput"
          @change="onFileChange"
        />
      </div>
      <div v-show="imageSrc" class="upload-image">
        <img :src="imageSrc" />
      </div>
    </div>
  </v-container>
</template>

<script>
import ContentsApi from "../apis/ContentsApi";

export default {
  name: "imageUpload",
  data() {
    return {
      uploadImage: "",
      filename: "",
      imageSrc: ""
    };
  },
  methods: {
    onDrop(event) {
      this.inputImageFile(event.dataTransfer.files);
      this.uploadImage = event.dataTransfer.files[0];
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
    onClickUpload() {
      this.preview(this.filename);

      const formData = new FormData();
      formData.append("file", this.uploadImage);
      ContentsApi.imgupload(
        formData,
        res => {
          console.log(res);
        },
        error => {
          console.log(error);
        }
      );
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
    }
  }
};
</script>

<style lang="scss" scoped>
#uploader {
  width: 90%;
  padding: 2rem;

  .input-group {
    border: 2px solid black;
    width: 200px;
    height: 100px;
  }
  .file-input {
    display: none;
  }
  .upload-image {
    padding-top: 1rem;
    width: 200px;
    height: 200px;
    img {
      width: 100%;
      height: 100%;
    }
  }
}
</style>
