import img_preprocess
import my_token
import tensorflow as tf
import numpy as np


def create_tf_data(my_tokenizer, img_name_train, cap_train, input_batch_size):
    # Feel free to change these parameters according to your system's configuration
    BATCH_SIZE = input_batch_size
    BUFFER_SIZE = 1000 # shuffle 기준치, 1000이면 앞에서 부터 1000개만 뽑아서 섞고 다음1000개를 섞고..

    # dataset을 img_name_train, cap_train 로 나누어 사용한다
    dataset = tf.data.Dataset.from_tensor_slices((img_name_train, cap_train))
    # map_func라는 사용자 정의함수를 기반으로, 병렬 처리...
    # 각 칼럼에 해당하는 dataset을 numpy배열로 가져온다..
    dataset = dataset.map(lambda item1, item2: tf.numpy_function(
        map_func, [item1, item2], [tf.float32, tf.int32]),
        num_parallel_calls=tf.data.experimental.AUTOTUNE)

    # shuffle : 설정된 EPOCH단위마다 Dataset을 섞을 수 있다. (overfitting을 피할때 중요하다고 함)
    dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
    dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

    return dataset


def map_func(img_name, cap):
    img_tensor = np.load(img_name.decode('utf-8')+'.npy')
    return img_tensor, cap

# def create_dataSet(img_paths, captions):

#     # 이미지 데이터화해서 받아오기
#     # img_tensor = img_preprocess.preprocess_img(captions[0], True)

#     # 토큰화 된 캡션 쌍 받아오기
#     caption_sample = tokenization.tokenization(captions)

#     # tf 데이터형식 지키는건진 모르겠움,,
#     # 이미지는 tf파일 형식으로 바꿔서 리턴한거라서 ㄱㅊ
#     # 토큰화된 캡션에서는 잘 모르겠음?
#     # return img_tensor, caption_sample
#     # Augmentation.do(img_tensor)
#     return caption_sample
