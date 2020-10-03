# CNN 구조

conv - pooling - activation - conv - pooling - activation - dropout - flatten - dense -dropout - dense

## Convolution

- 제일 앞의 숫자: 사용할 필터의 개수
- kernel_size : 필터의 크기
- strides : 필터의 이동간격
- padding : 여백. same으로 설정할 시 인풋배열과 같은 크기로 출력하도록 여백이 자동으로 추가된다.
- activation: 활성화 함수. relu, softmax, adam 등의 함수를 쓴다. cnn에서는 relu,softmax 사용.
- input_shape: 인풋이미지의 shape. `.shape` 메소드를 통해 최초 convolution layer의 인풋 형태를 지정한다.



## Max Pooling

convolution layer를 통과한 feature의 수 조절. feature가 너무 많아지면 overfit 확률이 증가하기 때문에 feature의 수가 너무 많다면 조절할 필요가 있다. 이 때 사용되는 것이 pooling이다.



Max pooling은 pool size 만큼의 배열에 각각의 max 값을 출력한다.

- pool_size: pooling을 통해 출력할 배열의 비율. (2,2)는 입력대비 절반으로 출력한다.

## Dropout

Dropout이란?

학습이 진행되는 동안 무작위로 신경망의 일부를 제거한다.

학습 데이터에 의해 신경망이 동조화(co-adaption: 두개 이상의 신경망이 하나의 신경망처럼 활동)되는 것을 방지한다.

`Dropout(float)`: 0~1 사이의 부동소수점으로 드롭할 신경망의 비율을 지정한다. rate로도 지정할 수 있다.

## Flatten

인풋을 일렬화한다. 배치 크기에는 영향을 주지 않음.



## Dense

활성화 함수와 이전 계층을 연결한다.



## model.fit

verbose

- 0 == 아무것도 표시하지 않음
- 1 == 진행바로 표시
- 2 == epoch으로 진행상태 표시