
import pickle




# with open('car_name.pickle', 'rb') as f:
#     car_lists = pickle.load(f)

# print(car_lists)


# ['2021 G80', '2020 아반떼', '2020 GV80', '2020 쏘렌토', '2020 그랜저', 
# '2020 XM3', '2019 팰리세이드', '2019 셀토스', '2020 K5', '2020 G70', 
# '2020 투싼', '2020 벨로스터 N', '2021 K3', '2021 K9', '2019 베뉴', '2019 싼타페', 
# '2020 코나', '2020 카니발', '2020 티볼리', '2019 K7', '2019 G90', '2020 코란도', 
# '2020 QM6', '2019 니로 하이브리드', '2021 K3 GT', '2020 모하비', '2020 그랜저 하이브리드', 
# '2020 스팅어', '2020 스포티지', '2020 레이', '2020 K5 하이브리드', '2020 그랜드 스타렉스', 
# '2020 G4 렉스턴', '2019 모닝', '2020 코나 하이브리드', '2020 코나 일렉트릭', '2018 넥쏘', 
# '2020 쏘렌토 하이브리드', '2020 렉스턴 스포츠 칸', '2019 스토닉', '2019 G90L', '2020 렉스턴 스포츠',
# '2020 SM6', '2020 포터2', '2019 아이오닉 하이브리드', '2021 쏘울 부스터', '2020 카니발 하이리무진', 
# '2021 쏘울 부스터 EV', '2020 포터2 일렉트릭', '2019 i30', '2020 카니발 리무진', '2020 텔루라이드', 
# '2020 봉고3', '2018 벨로스터', '2019 다니고 III 픽업', '2019 K7 하이브리드', '2019 쏠라티', 
# '2020 캠시스 CEVO-C', '2020 봉고3 EV', '2019 아이오닉 일렉트릭', '2020 다마스', '2018 니로 EV', 
# '2019 다니고 III 밴', '2019 니로 플러그인 하이브리드', '2020 라보', '2020 i10', '2020 i30 패스트백', 
# '2017 i30 N', '2018 그랜드 스타렉스 리무진', '2020 라페스타 EV', '2018 다니고', '2019 엑센트', 
# '2020 i30 왜건', '2020 i20', '2019 아이오닉 플러그인 하이브리드', '2019 i30 N 패스트백', 
# '2020 ix25', '2019 리오 세단', '2018 라페스타', '2020 아우라', '2020 X씨드', '2020 프로씨드', 
# '2018 씨드 SW', '2019리오 해치백', '2019 씨드', '2020 씨드 SW 플러그인 하이브리드', 
# '2020 X씨드 플러그인 하이브리드', '2020 쏘나타 하이브리드', '2020 쏘나타']

# import os

# path = "./models"
# file_list = os.listdir(path)

# print ("file_list: {}".format(file_list))



    
car_lists = {'2017 hyundai i30':'2017 i30 N', '2018 daechang danigo':'2018 다니고', '2018 hyundai grand starex limuzine':'2018 그랜드 스타렉스 리무진',
 '2018 hyundai lafesta':'2018 라페스타', '2018 hyundai nexo':'2018 넥쏘', '2018 hyundai veloster':'2018 벨로스터', 
 '2018 kia ceed sw':'2018 씨드 SW', '2018 kia niro ev':'2018 니로 EV', '2019 daechang danago iii':'2019 다니고 III 픽업',
'2019 hyundai accent':'2019 엑센트', '2019 hyundai genesis g90':'2019 G90', '2019 hyundai i30':'2019 i30',
'2019 hyundai ioniq':'2019 아이오닉 하이브리드', '2019 hyundai palisade':'2019 팰리세이드', '2019 hyundai santa fe':'2019 싼타페',
'2019 hyundai solati':'2019 쏠라티', '2020 hyundai sonata':'2020 쏘나타', '2019 hyundai venue': '2019 베뉴',
'2019 kia ceed':'2019 씨드', '2019 kia k7':'2019 K7', '2019 kia morning':'2019 모닝',
'2019 kia niro hybrid':'2019 니로 하이브리드', '2019 kia rio':'2019 리오 세단', '2019 kia seltos':'2019 셀토스',
'2019 kia stonic':'2019 스토닉', '2020 camsys cevo c':'2020 캠시스 CEVO-C', '2020 gm damas':'2020 다마스',
'2020 gm labo':'2020 라보', '2020 hyundai aura':'2020 아우라', '2020 hyundai avante':'2020 아반떼',
'2020 hyundai creta ix25':'2020 ix25', '2020 hyundai genesis gv80':'2020 GV80', '2020 hyundai genesis g70':'2020 G70',
'2020 hyundai grand i10':'2020 i10', '2020 hyundai grand starex':'2020 그랜드 스타렉스', '2020 hyundai grandeur':'2020 그랜저',
'2020 hyundai i20 elite':'2020 i20', '2020 hyundai i30':'2020 i30 왜건', '2020 hyundai kona':'2020 코나',
'2020 hyundai lafesta':'2020 라페스타 EV', '2020 hyundai porter2':'2020 포터2', '2020 hyundai tucson':'2020 투싼',
'2020 hyundai veloster':'2020 벨로스터 N', '2020 kia bongo3':'2020 봉고3', '2020 kia carnival':'2020 카니발',
'2020 kia k5':'2020 K5', '2020 kia mohave':'2020 모하비', '2020 kia proceed':'2020 프로씨드',
'2020 kia ray':'2020 레이', '2020 kia sorento':'2020 쏘렌토', '2020 kia spotage':'2020 스포티지',
'2020 kia stinger':'2020 스팅어', '2020 kia telluride':'2020 텔루라이드', '2020 kia xceed':'2020 X씨드',
'2020 renaultsamsung qm6':'2020 QM6', '2020 renaultsamsung sm6':'2020 SM6', '2020 renaultsamsung xm3':'2020 XM3',
'2020 ssangyong korando':'2020 코란도',  '2020 ssangyong rexton':'2020 렉스턴 스포츠', '2020 ssangyong rexton g4':'2020 G4 렉스턴',
'2020 ssangyong tivoli':'2020 티볼리', '2021 hyundai genesis g80':'2021 g80', '2021 kia k3':'2021 K3',
'2021 kia k9':'2021 K9', '2021 kia soul':'2021 쏘울 부스터',
'2019 tesla model3': '2019 테슬라 모델3', '2020 mercedes e class':'2020 벤츠 E클래스', '2021 chevrolet trailblazer':'2021 쉐보레 트레일블레이저', 
'2020 mercedes benz s':'2020 벤츠 S클래스', '2020 lincoln aviator':'2020 링컨 에비에이터', '2020 mercedes cls class':'2020 벤츠 CLS클래스', 


'2020 mercedes benz cla':'2020 벤츠 CLA클래스', '2021 tesla cybertruck':'2021 테슬라 사이버트럭', '2019 bentley continental gt':'2019 벤틀리 컨티넨탈 GT', 
'2020 bmw x4':'2020 BMW X4', '2020 audi a6':'2020 아우디 A6',
'2020 mercedes gt 4 door':'2020 메르세데스-AMG GT 4도어', '2020 bmw 5':'2020 BMW 5시리즈', '2020 volkswagen tiguan allspace':'2020 폭스바겐 티구안 올스페이스'
}



a =[
'2020 쉐보레 콜로라도', '2020 BMW X5', '2019 포르쉐 파나메라', 
'2020 볼보 XC60', '2019 테슬라 모델S', '2020 벤츠 C클래스', 
'2020 벤츠 GLE클래스', '2020 벤츠 GLC클래스', '2020 BMW 3시리즈', 
'2020 아우디 Q8', '2020 포르쉐 911 카레라', '2020 아우디 A7', 
'2019 테슬라 모델X', '2020 볼보 XC40', '2020 BMW X6'


]





with open('change_car_name.pickle', 'wb') as f:
    pickle.dump(car_lists, f, pickle.HIGHEST_PROTOCOL)



# with open('change_car_name.pickle', 'rb') as f:
#     car_lists = pickle.load(f)


# print(car_lists['2021 KIA SOUL'])
