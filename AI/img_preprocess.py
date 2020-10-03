import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from sklearn.utils import shuffle

# 여기서 이미지를 데이터화 하겠지?


def img_pre(img_path, captions, test_data_num, aug=False):
    all_img_name = []
    all_caption = []

    # 각 캡션에 <start><end>토큰 추가
    # augumentation 적용
    if aug:
        datagen = image.ImageDataGenerator(
            rotation_range=5,
            width_shift_range=0.1,
            height_shift_range=0.1,
            rescale=1./255,
            shear_range=0.2,
            zoom_range=0.12,
            horizontal_flip=True,
            fill_mode='nearest')

    


    num = 0
    for i in range(len(captions)):
        img_path = captions[i][0]

        for j in range(1, 6):
            if aug:
                train_data = image.load_img(img_path, target_size=None)
                # print('1', image)
                train_data = image.img_to_array(train_data)
                # print(image)
                train_data = train_data.reshape((1,) + train_data.shape)  # (1, 3, 150, 150) 크기의 NumPy 배열
                # print(image)
                for batch in datagen.flow(train_data, y=None, batch_size=1, seed=None, subset=None,
                                        save_to_dir='preview', save_prefix='train'+str(num).zfill(5), save_format='jpeg'):
                    break 


            caption = '<start>' + captions[i][j] + '<end>'
            if aug:
                all_img_name.append('./preview/'+'train'+str(num).zfill(5)+'.jpg')
            else:
                all_img_name.append(img_path)
            all_caption.append(caption)
            num+=1

    train_captions, img_name_vector = shuffle(
        all_caption, all_img_name, random_state=1)
    num_example = test_data_num
    train_captions = train_captions[:num_example]
    img_name_vector = img_name_vector[:num_example]

    if aug:
        path = './preview/'
        numbering = 0
        for filename in os.listdir(path):
            os.rename(path+filename, path+'train'+str(numbering)+'.jpg')
            numbering += 1


    return img_name_vector, train_captions


def preprocess_img(img_path, flag, target_size=250):
    # keras.preprocessing의 image클래스 호출

    # img_path : 이미지 파일 경로
    # target_size : 이미지 데이터 사이즈(리사이징 할때 필요)
    # load_img() : 이미지 파일 로딩
    # img_to_array() : 이미지 파일을 array로 변환

    img = image.load_img(img_path, target_size=(target_size, target_size))

    img_tensor = image.img_to_array(img)

    # 3차원 array에 이미지 샘플을 구분하기
    # np.expand_dims() : 1개 차원 추가
    # 3차원 -> 4차원
    img_tensor = np.expand_dims(img_tensor, axis=0)

    # flag가 True : 데이터 정규화 하기
    if flag == True:
        img_tensor /= 255.
        # print(img_tensor[0])

    # flag가 False : 데이터 정규화 X
    else:
        print(img_tensor[0])

        # 테스트 코드
        # plt.rcParams['figure.figsize'] = (10, 10)
        # plt.imshow(img_tensor[0])
        # plt.show()

        # 데이터 리턴
    return img_tensor
