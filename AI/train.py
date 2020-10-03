import tensorflow as tf
import numpy as np
import time
import matplotlib.pyplot as plt

from data import preprocess
from sklearn.model_selection import train_test_split  # 데이터를 학습용/테스트용으로  분리해주는 유틸리티
import my_token
import img_preprocess, create, CNN, RNN, pre_trained_model
# - 이미지 데이터 불러오기 링크
# https://m.blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221400912923&categoryNo=36&proxyReferer=https%3A%2F%2Fwww.google.com%2F

# - Augmentation 링크
# https://keraskorea.github.io/posts/2018-10-24-little_data_powerful_model/

# GPU 메모리 초기화
gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)

# Req 3번에서 이미지 파일 경로랑 캡션을 입력으로 받으라고 함
#  이미지 파일 경로, 캡션 받기
img_paths, captions = preprocess.get_path_caption()
print("이미지/캡션 데이터 로딩")
# ===========================
# 이미지 정규화 데이터 받아오기
# 여기 구현
# 데이터 augumentation 함수 인에 구현

# 30000개 데이터까지만 써봅시다,,,
test_data_num = 30000
img_name_vector, train_captions = img_preprocess.img_pre(img_paths, captions, test_data_num)
print("샤용 데이터수: ",len(train_captions))
# ===========================


# ============================================
# 이미지 특징 추출 -  InceptionV3 모델
image_features_extract_model = pre_trained_model.Pre_trained_img(img_name_vector)


# ===========================================
# 캡션 토큰화 데이터 받아오기,, 리턴은 토크나이저, 토큰화된 캡션벡터
tokenizer, cap_vector, train_seqs, max_length = my_token.tokenization(train_captions[:test_data_num*5])


#     my_token.Save_Tokenizer(my_tokenizer)
#     my_token.Save_Captions(cap_vector)
#     my_token.Save_Seqs(train_seqs)
#     tokenizer = my_token.Load_Tokenizer()
#     cap_vector = my_token.Load_Captions()
#     train_seqs = my_token.Load_Seqs()
# else:
#     tokenizer = my_token.Load_Tokenizer()
#     cap_vector = my_token.Load_Captions()
#     train_seqs = my_token.Load_Seqs()

# ===========================================


# ==================
# 토크나이저 저장하기
# my_token.Save_Tokenizer(my_tokenizer)
# # 토크나이저 불러오기
# my_tokenizer = my_token.Load_Tokenizer()
# ==================


# =============================
# 학습/테스트용 데이터로 분할하기
# (학습용 80% / 테스트용 20%로 설정)
# test_size가 0.2이면 train_size는 0.8
# 따라서 train:test = 80% : 20%
img_name_train, img_name_val, cap_train, cap_val = train_test_split(
    img_name_vector, cap_vector, test_size=0.2, random_state=0
)

print("데이터 분할 완료")
print("트레이닝 데이터수: ", len(img_name_train), len(cap_train), "테스트 데이터수: ",len(img_name_val), len(cap_val))
# ====================-=======


# # tf 데이터셋 만들기
BATCH_SIZE = 512
dataset = create.create_tf_data(tokenizer, img_name_train, cap_train, BATCH_SIZE)
print()

# 환경 변수
embedding_dim = 256
units = 512
vocab_size = my_token.top_k + 1


# CNN : relu모델 사용
# RNN : GRU 모델 사용
encoder = CNN.CNN_Encoder(embedding_dim)
decoder = RNN.RNN_Decoder(embedding_dim, units, vocab_size)
print("인코딩, 디코딩")



# encoder, decoder에 가중치 갱신해주는 optimizer 
# optimizer에서 learning rate를 변경 가능
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-5)


#############################################
# 체크포인트
# 체크 포인트 저장 
checkpoint_path = "./checkpoints/train"
ckpt = tf.train.Checkpoint(encoder=encoder, decoder=decoder, optimizer=optimizer)
ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

start_epoch = 0

# 학습을 지속할때 이전에 학습한 자료로 초반epoch 사용
# 학습시간 감소를 위해 사용한듯?
# 나머지 구현 후에 주석 해제
if ckpt_manager.latest_checkpoint:
    start_epoch = int(ckpt_manager.latest_checkpoint.split('-')[-1])
    # restoring the latest checkpoint in checkpoint_path
    ckpt.restore(ckpt_manager.latest_checkpoint)
###################################################


print("학습을 시작합니다")
# batch size, epoch 지정
# Batch size: 한번에 학습할 양
# Epochs: batch size 만큼 학습할 횟수
BATCH_SIZE = 512
EPOCHS = 100


num_steps = len(img_name_train) // BATCH_SIZE
loss_plot = []


# 지정한 epoch만큼 학습
for epoch in range(start_epoch, EPOCHS):
    # 시간 측정을 하기위해 타이머 작동
    start = time.time()
    # epoch당 손실함수
    total_loss = 0

    # batch당 손실함수
    for (batch, (img_tensor, target)) in enumerate(dataset):
        batch_loss, t_loss = pre_trained_model.train_step(img_tensor, target, encoder, decoder, tokenizer, optimizer)
        total_loss += t_loss

        if batch % 100 == 0:
            print(
                "Epoch {} Batch {} Loss {:.4f}".format(
                    epoch + 1, batch, batch_loss.numpy() / int(target.shape[1])
                )
            )
    # 손실률 기록
    loss_plot.append(total_loss / num_steps)

    # epoch 5개 진행시 체크포인트 저장
    if epoch % 5 == 0:
        ckpt_manager.save()

    # Epoch당 손실률
    print("Epoch {} Loss {:.6f}".format(epoch + 1, total_loss / num_steps))
    # 1 epoch 소요 시간
    print("Time taken for 1 epoch {} sec\n".format(time.time() - start))



# 손실함수 그래프
plt.plot(loss_plot)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Loss Plot")
plt.show()


print(max_length)





# predict 하기
attention_features_shape = 64
# 테스트할 랜덤 이미지 하나 뽑아오기
rid = np.random.randint(0, len(img_name_val))
image = img_name_val[rid]
# 해당 이미지 실제 캡션
real_caption = ' '.join([tokenizer.index_word[i] for i in cap_val[rid] if i not in [0]])


# 학습한 모델로 테스트
result, attention_plot = pre_trained_model.evaluate(image, max_length, attention_features_shape, encoder, decoder, pre_trained_model, image_features_extract_model, tokenizer)

print ('Real Caption:', real_caption)
print ('Prediction Caption:', ' '.join(result))
pre_trained_model.plot_attention(image, result, attention_plot)
