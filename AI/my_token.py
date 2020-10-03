import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.preprocessing.text import Tokenizer
import pickle
# ========================캡션 전처리===========================
# =============================
# 텍스트 데이터 토큰화하면,,
# I am hungry -> [4, 19, 290]

# <start>, <end> 토큰 추가하면,,,
# I am hungry -> <start> I am hungry <end> -> [0, 4, 19, 290, 1]

# <pad>토큰 추가하면 ,,(모든 캡션 길이 통일 시키기 위해서)
# ============================

# 내 캡션데이터 중에서 최대 길이 찾기


def calc_max_length(captions):
    return max(len(c) for c in captions)


# 단어 집합에서 상위 10000단어 제한
top_k = 10000


def tokenization(train_captions):
    # 가장 빈도가 높은 10000개의 단어만 선택하도록

    # 토크나이저 객체 생성
    # num_words : 상위 10000개 단어
    # oov_token : 10000개를 초과한 애들은 "UNK"토큰으로 대체, 메모리 절약하기!
    # filters : 다음과 같은 문자 거르기
    tokenizer = Tokenizer(num_words=top_k, oov_token="<unk>",
                          filters='!"#$%&()*+.,-/:;=?@[\]^_`{|}~ ')

    # 단어 인덱스 구축하기
    # (입력으로 들어오면 train_captions에 대해서,,, )
    tokenizer.fit_on_texts(train_captions)

    # ====================================
    # 캡션을 이용해 토큰화 벡터 생성하는 과정
    # (토큰화 벡터가 있어야 시각화 할수 있다,,)
    # 토큰화된 벡터생성~~
    train_seqs = tokenizer.texts_to_sequences(train_captions)

    # 현재 토크나이저 pad 토큰값을 0으로 만들기 설정
    tokenizer.word_index['<pad>'] = 0
    tokenizer.index_word[0] = '<pad>'

    # 다시 토큰화된 벡터 생성!!
    train_seqs = tokenizer.texts_to_sequences(train_captions)
    # 토큰화 벡터를 설정한 pad로 채우기
    # (만약에 위에서 토크나이저 생성할때, 최대 길이 설정안하면, 자동으로 됨)
    cap_vector = preprocessing.sequence.pad_sequences(train_seqs)

    # max_length : 가중치를 저장하는데 사용되는 길이
    max_length = 30

    return tokenizer, cap_vector, train_seqs, max_length


# ======================= 토크 나이저 저장 및 불러오기 ==================
# 토크나이저 객체 저장
def Save_Tokenizer(my_tokenizer):
    with open('tokens.txt', 'wb') as f:
        pickle.dump(my_tokenizer, f)  # pickle 방식으로 저장

def Save_Captions(cap_vector):
    with open('captions.txt', 'wb') as f:
        pickle.dump(cap_vector, f)  # pickle 방식으로 저장
        
def Save_Seqs(train_seqs):
    with open('train_seqs.txt', 'wb') as f:
        pickle.dump(train_seqs, f)  # pickle 방식으로 저장


# 토크나이저 객체 불러오기
def Load_Tokenizer():
    try:
        with open('tokens.txt', 'rb') as f:
            my_tokenizer = pickle.load(f)

        if(my_tokenizer is None):
            return None
        else:
            return my_tokenizer
    except:
        return None
        
def Load_Captions():
    try:
        with open('captions.txt', 'rb') as f:
            cap_vector = pickle.load(f)

        if(cap_vector is None):
            return None
        else:
            return cap_vector
    except:
        return None

        
def Load_Seqs():
    try:
        with open('train_seqs.txt', 'rb') as f:
            train_seqs = pickle.load(f)

        if(cap_vector is None):
            return None
        else:
            return train_seqs
    except:
        return None
