import axios from "axios";
// const host = "http://127.0.0.1:8080";
const host = "http://58.230.252.215:8000";
// const host = "http://119.56.164.135:8000";

const ContentsApi = {
  //   requestAI: (data, callback, errorCallback) => requestAI(data, callback, errorCallback),
  imgupload: (data, callback, errorCallback) => imgupload(data, callback, errorCallback),
  searchCompany: (data, callback, errorCallback) => searchCompany(data, callback, errorCallback),
  searchName: (data, callback, errorCallback) => searchName(data, callback, errorCallback),
  requestCarDetail: (data, callback, errorCallback) => requestCarDetail(data, callback, errorCallback),
  requestCarAI: (data, callback, errorCallback) => requestCarAI(data, callback, errorCallback),
  requestCars: (callback, errorCallback) => requestCars(callback, errorCallback),
  likecarAll: (callback, errorCallback) => likecarAll(callback, errorCallback),
  likecarUserlike: (data, callback, errorCallback) => likecarUserlike(data, callback, errorCallback),
  //   profileLoad: (data, callback, error) => profileLoad(data, callback, error),
};

const likecarUserlike = (data, callback, errorCallback) => {
  axios
    .post(`${host}/back/likecar/`, {
      userId: sessionStorage.getItem("id"),
      carId: data,
    })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      callback(errorCallback);
    });
};

const requestCarAI = (data, callback, errorCallback) => {
  axios
    .post(`${host}/back/cars/detailAi/`, {
      link: data,
    })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

const imgupload = (formdata, callback, errorCallback) => {
  axios({
    url: `${host}/back/upload/`,
    method: "post",
    data: formdata,
    headers: {
      "Content-Type": "multipart/form-data",
    },
  })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

const searchCompany = (data, callback, errorCallback) => {
  axios({
    url: `${host}/back/cars/company/${data}/`,
    method: "get",
  })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

const searchName = (data, callback, errorCallback) => {
  axios({
    url: `${host}/back/cars/name/${data}/`,
    method: "get",
  })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

const requestCarDetail = (data, callback, errorCallback) => {
  axios({
    url: `${host}/back/cars/` + data,
    method: "get",
  })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

const likecarAll = (callback, errorCallback) => {
  axios({
    url: `${host}/back/likecarAll/`,
    method: "get",
  })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

const requestCars = (callback, errorCallback) => {
  axios({
    url: `${host}/back/cars`,
    method: "get",
  })
    .then((res) => {
      console.log(res);
      callback(res);
    })
    .catch((error) => {
      console.log(error);
      errorCallback(error);
    });
};

export default ContentsApi;
