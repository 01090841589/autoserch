from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

import os

path = "./models_origin"
file_lists = os.listdir(path)

for file_list in file_lists:
        
    path = "./models_origin/"+file_list+'/'
    image_lists = os.listdir(path)
    
    if os.path.exists("./models/"+file_list):
        continue
    os.makedirs("./models/"+file_list)
    for image_list in image_lists:
        datagen = ImageDataGenerator(
                rotation_range=5,
                width_shift_range=0.1,
                height_shift_range=0.1,
                rescale=1./255,
                shear_range=0.2,
                zoom_range=0,
                horizontal_flip=True,
                fill_mode='nearest')




        image = load_img(path+image_list)
        # print('1', image)
        image = img_to_array(image)
        # print(image)
        image = image.reshape((1,) + image.shape)  # (1, 3, 150, 150) 크기의 NumPy 배열
        # print(image)


        # 아래 .flow() 함수는 임의 변환된 이미지를 배치 단위로 생성해서
        # 지정된 `preview/` 폴더에 저장합니다.
        i = 0
        for batch in datagen.flow(image, batch_size=1,
                                  save_to_dir="./models/"+file_list, save_prefix='fix', save_format='jpg'):
            i += 1
            if i > 12:
                break  # 이미지 10장을 생성하고 마칩니다 augmentation!
    
    print("./models/"+file_list)
print("완료")


# from PIL import Image
 
# # img = Image.open('10.jpg')
# # img = img.convert("RGBA")
# # datas = img.getdata()
 
# # newData = []
# # cutOff = 120
 
# # for item in datas:
# #     if item[0] >= cutOff and item[1] >= cutOff and item[2] >= cutOff:
# #         newData.append((255, 255, 255, 0))
# #         # RGB의 각 요소가 모두 cutOff 이상이면 transparent하게 바꿔줍니다.
# #     else:
# #         newData.append(item)
# #         # 나머지 요소는 변경하지 않습니다.
 
# # img.putdata(newData)
# # img.save("10.png", "PNG") # PNG 포맷으로 저장합니다.