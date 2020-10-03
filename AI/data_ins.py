import json
import guess
import pickle
import urllib.request
import numpy as np
import tensorflow.compat.v1 as tf

imagePath = 'https://imgauto-phinf.pstatic.net/20200330_142/auto_1585547248870fGwBQ_PNG/20200330144726_jJxZhNkX.png?type=f160_116'                                    # 추론을 진행할 이미지 경로

urllib.request.urlretrieve('https://imgauto-phinf.pstatic.net/20200330_142/auto_1585547248870fGwBQ_PNG/20200330144726_jJxZhNkX.png?type=f160_116', './data.png')
imagePath = './data.png'                                  # 추론을 진행할 이미지 경로


# imagePath = Image.open('https://imgauto-phinf.pstatic.net/20200330_142/auto_1585547248870fGwBQ_PNG/20200330144726_jJxZhNkX.png?type=f160_116')


result = guess.run_inference_on_image(imagePath)

for i in range(len(result)):
    print(i+1, "번째:",result[i][0], result[i][1])
# with open('./car_data.json', encoding='utf-8') as fh:
#     data = json.load(fh)