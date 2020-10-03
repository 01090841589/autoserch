# AutoSearch

자동차 검색 사이트

<table>
   <tr>
      <td>
        <img width="160px" src="https://user-images.githubusercontent.com/58671945/78890548-d085b100-7aa0-11ea-9723-b146362f6dc5.jpg"><br>
         임현수<br>
         <i>Project dev & Front Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
      <td>
        <img width="160px" src="https://user-images.githubusercontent.com/58671945/78890552-d1b6de00-7aa0-11ea-85af-76bce9309754.jpg"><br>
         문준호<br>
         <i>Project dev & Front Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
      <td>
        <img width="160px" src="https://lab.ssafy.com/webmobile1-sub1/s02p11d138/raw/develop/KakaoTalk_20200109_090135135.jpg"><br>
         홍성욱<br>
         <i>Project Lead & Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
      <td>
        <img width="160px" src="https://user-images.githubusercontent.com/58671945/78890557-d380a180-7aa0-11ea-9d6d-2fef84900de9.jpg"><br>
         오세봉<br>
         <i>Project dev & Back Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
      <td>
        <img width="160px" src="https://user-images.githubusercontent.com/58671945/78890559-d4b1ce80-7aa0-11ea-80a2-6231f6a8f1ed.jpg"><br>
         박찬환<br>
         <i>Project dev & Back Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
   </tr>
</table>

## 1. Frontend - Vue.js

### 1-1. 개발환경 구성

Node.js 설치

https://nodejs.org/ko/download/

Vue.js 설치

https://kr.vuejs.org/v2/guide/installation.html



### 1-2 컴포넌트 설치

```
npm install
```



### 1-3 서버 실행

```
npm run serve
```

## 2. Backend - Anaconda

### 2-1 개발환경 구성

아나콘다 설치

https://www.anaconda.com/download/

### 2-2 가상환경 구성

```
conda create -n AI
```

### 2-3 가상환경 실행

```
conda activate AI
```



## 3. Backend - Django

### 3-1 개발환경 구성

https://tutorial.djangogirls.org/ko/django_installation/

### 3-2 필요 pip 설치

아나콘다 가상환경이 실행된 상태에서 ./web/backend/ 에서

```
pip install -r requirement.txt
```

필요 패키지들이 설치된다.



## 4. 자동차 학습파일 생성



### 4-1 네이버 자동차 정보 크롤링

./AI/car_training/crawl.py에서 자동차 정보를 json파일로 저장한다.

네이버 자동차의 각페이지에 있는 정보를 저장



### 4-2 구글 이미지 크롤링

./AI/car_training/create_imate.py 이전에 얻은 자동차 정보들을 이용하여 각각여 자동차에 대한 이미지를 ./models_origin에 저장한다.



### 4-3 이미지 Augumentation

./AI/car_training/spread_image.py에서 각각의 폴더에 저장된이미지를 여러방법으로 바꾸어서 ./models 에 저장한다.



### 4-4. 자동차 모델 학습

./AI/car_training/Learning_cars.py 에서 이미지들을이용하여 학습을 시작한다.

학습 모델은 Inception V3를 사용했다.



### 4-5 자동차 모델 추정

Django의 views.py에서 모델 추정이 필요할때 해당 경로의 guess.py를 불러와서 결과를 받아온다.

## 5. 서비스 페이지

### 5-1. 메인 페이지





### 5-2. 예측 결과 페이지





### 5-3. 상세정보 페이지



### 5-4. 회사별 정보 페이지



### 5-3. 검색 페이지

