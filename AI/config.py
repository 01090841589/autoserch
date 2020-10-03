import argparse

# Req. 2-1	Config.py 파일 생성

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='이미지 캡셔닝 모델 Setting..')

# 입력받을 인자값 등록
# 캡션 데이터가 저장된 csv 파일의 경로
parser.add_argument('--caption_file_path', type=str,
                    default='.\\datasets\\captions.csv')
# 실제 이미지 파일들이 저장된 경로
parser.add_argument('--image_file_path', type=str,
                    default='.\\datasets\\images\\')

# 샘플링 추출할 갯수
parser.add_argument('-s', '--do_sampling', type=int,
                    help="샘플링 여부 지정", default=0)

# 데이터 1개당 반복학습할 횟수
parser.add_argument('--epochs', type=int, default=32)

# 몇개의 샘플당 가중치를 갱신할 것인지..
parser.add_argument('--batch_size', type=int, default=10)

# data가 1이면 학습 데이터셋 패스, 아니면 테스트 데이터셋 패스
parser.add_argument("--data", type=int, default=1)

# 입력받은 인자값 args에 저장(type: namespace)
config = parser.parse_args()

# 인자값 테스트
# print(config.caption_file_path)
# print(config.image_file_path)
