import os
import csv
import numpy as np
import random

# Req. 3-1	이미지 경로 및 캡션 불러오기


def get_path_caption():
    img_paths = '.\\datasets\\images'
    csv_data = np.loadtxt('.\\datasets\\captions.csv',
                          delimiter='|', dtype="str", encoding="utf-8")

    # csv_data[i][0] : image_name
    # csv_data[i][1] : comment_number
    # csv_data[i][2] : comment

    # img_data[0] : 경로
    # img_data[1]: comment 1
    # img_data[2]: comment 2
    # img_data[3]: comment 3
    # img_data[4]: comment 4
    # img_data[5]: comment 5
    img_data = ["", "", "", "", "", ""]
    captions = []

    for i in range(1, len(csv_data), 5):
        img_data[0] = img_paths + '\\' + csv_data[i][0]
        img_data[0] = img_data[0].replace("\"", "")
        img_data[1] = csv_data[i][2]
        img_data[2] = csv_data[i + 1][2]
        img_data[3] = csv_data[i + 2][2]
        img_data[4] = csv_data[i + 3][2]
        img_data[5] = csv_data[i + 4][2]
        captions.append(img_data[:])

    return img_paths, captions


# Req. 3-2	전체 데이터셋을 분리해 저장하기
def dataset_split_save(captions):
    # caption : 158916 rows...
    train_dataset = []
    test_dataset = []

    # 1~5번 comment중 랜덤으로 학습,테스트용으로 나누기
    for i in range(len(captions)):
        num = random.randint(1, 5)
        if num < 2:
            train_dataset.append(captions[i])
        else:
            test_dataset.append(captions[i])

    # csvfile 오픈..
    # url, 파일 모드, 인코딩 타입 주의
    # 참고 링크 : https://m.blog.naver.com/PostView.nhn?blogId=real_77&logNo=221224637207&proxyReferer=https%3A%2F%2Fwww.google.com%2F
    csvfile = open(".\\datasets\\train_dataset.csv", "w", newline="", encoding="utf-8")
    csvwriter = csv.writer(csvfile, quotechar="|", delimiter="|")

    for row in train_dataset:
        csvwriter.writerow(row)
    csvfile.close

    csvfile = open(".\\datasets\\test_dataset.csv", "w", newline="", encoding="utf-8")
    csvwriter = csv.writer(csvfile, quotechar="|", delimiter="|")

    for row in test_dataset:
        csvwriter.writerow(row)
    csvfile.close
    return ".\\datasets\\train_dataset.csv", ".\\datasets\\test_dataset_path"


# Req. 3-3	저장된 데이터셋 불러오기
def get_data_file(data, train_dataset_path, test_dataset_path):
    # data : parser.add_argument("--data", type=int, default=1)
    # train_dataset_path : 분리된 학습 데이터셋 경로
    # test_dataset_path : 분리된 테스트 데이터 경로

    # data가 1이면 학습 데이터셋 패스, 아니면 테스트 데이터셋 패스
    if data == 1:
        caption = np.loadtxt(
            train_dataset_path, delimiter="|", dtype="str", encoding="UTF8"
        )
        img_paths = caption[:, 0]
    else:
        caption = np.loadtxt(
            test_dataset_path, delimiter="|", dtype="str", encoding="UTF8"
        )
        img_path = caption[:, 0]

    return img_paths, caption


# Req. 3-4	데이터 샘플링
def sampling_data(img_paths, caption, sampling_count):
    if sampling_count > 10:
        return img_paths, caption
    cal_img_paths = []
    cal_csv_data = []

    for i in random.sample(list(range(len(caption))), sampling_count):
        cal_img_paths.append(caption[i][0])
        cal_csv_data.append(caption[i][1:6].tolist())
    return cal_img_paths, cal_csv_data
