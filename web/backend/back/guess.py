# -*- coding: utf-8 -*-

"""Inception v3 architecture 모델을 retraining한 모델을 이용해서 이미지에 대한 추론(inference)을 진행하는 예제"""

import numpy as np
import tensorflow.compat.v1 as tf
import pickle

# imagePath = './cuss.jpg'                                      # 추론을 진행할 이미지 경로
# 읽어들일 graph 파일 경로
modelFullPath = './back/tmp/output_graph.pb'
# 읽어들일 labels 파일 경로
labelsFullPath = './back/tmp/output_labels.txt'


with open('./back/change_car_name.pickle', 'rb') as f:
    change_car_lists = pickle.load(f)


def create_graph():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image(imagePath):
    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
    create_graph()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
        top_k = predictions.argsort()[-6:][::-1]
        result = []
        f = open(labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "").replace("b'", '').replace(
            "\\n'", '').replace("\r", "").replace("\\r", "") for w in lines]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            result.append([change_car_lists[human_string], score])
        answer = labels[top_k[0]]
        return result
