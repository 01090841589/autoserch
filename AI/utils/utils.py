from datetime import datetime
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import tensorflow as tf
import json

# Req. 2-2	세팅 값 저장


def save_config(args):
    data = dict()
    # 데이터 생성
    # 캡션 파일경로
    data["caption_file_path"] = args.caption_file_path
    data["image_file_path"] = args.image_file_path
    data["do_sampling"] = args.do_sampling
    data["epochs"] = args.epochs
    data["batch_size"] = args.batch_size
    data["data"] = args.data

    with open(".\\settings.json", "a", encoding="utf-8") as make_file:
        json.dump(data, make_file, indent="\t")

    # 다음은 csv 파일로 저장하는 방법... (아직 덜함)
    # data = {'캡션 파일 경로': [args.caption_file_path],
    #         '이미지 파일 경로': [args.image_path]}
    # df = pd.DataFrame(data)

    # # .to_csv
    # # 최초 생성 이후 mode는 append
    # if not os.path.exists('setting.csv'):
    #     df.to_csv('setting.csv', index=False,
    #               mode='w', encoding='utf-8-sig')
    # else:
    #     df.to_scv('setting.csv', index=False, mode='a',
    #               encoding='utf-8-sig', header=False)
    return data


# Req. 4-1	이미지와 캡션 시각화


def visualize_img_caption(img_paths, caption):
    # .png파일 처리하기 위해 :: plt.imshow() 사용
    # 1) 가상환경 라이브러리 설치
    # conda install pillow
    # 2) 해당 py파일에 라이브러리 임포트
    # import matplotlib.image as img
    imgs = img.imread(img_paths[0])
    plt.title(caption[0][0])
    plt.imshow(imgs)
    plt.show()
