import tensorflow as tf
import my_token
import CNN
import RNN

# 환경 변수
embedding_dim = 256
units = 512
vocab_size = my_token.top_k + 1

# 모델 학습
encoder = CNN.CNN_Encoder(embedding_dim)
decoder = RNN.RNN_Decoder(embedding_dim, units, vocab_size)

# 최적화,코스트오브젝트
optimizer = tf.keras.optimizers.Adam()
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(
    from_logits=True, reduction='none')

# 체크포인트
checkpoint_path = "./checkpoints/train"
ckpt = tf.train.Checkpoint(encoder=encoder,
                           decoder=decoder,
                           optimizer=optimizer)
ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)


def loss_function(real, pred):
    mask = tf.math.logical_not(tf.math.equal(real, 0))
    loss_ = loss_object(real, pred)

    mask = tf.cast(mask, dtype=loss_.dtype)
    loss_ *= mask

    return tf.reduce_mean(loss_)
