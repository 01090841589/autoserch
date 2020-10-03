from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.parse import quote_plus
import pickle
import json
# url = "https://www.netcarshow.com/"
import time


car_lists = []
car_info = []
for i in range(1, 5):
    time.sleep(0.5)
    # url = "https://auto.naver.com/car/mainList.nhn?importYn=N&page="+str(i)
    url = "https://auto.naver.com/car/mainList.nhn?importYn=Y&page="+str(i)


    res = requests.get(url)

    soup = BeautifulSoup(res.content, 'html.parser')

    
    lists = soup.find('div', class_='model_group_new')
    label = lists.find_all('span', {'class':'box'})
    

    car_name = lists.find_all('strong')
    car_price = []
    car_size = []
    car_fuel_eff = []
    car_fuel_class = []
    car_company = []
    car_image = []
    image_links = lists.find_all('span', {'class':'thmb'})

    for i in range(len(image_links)):
        image = str(image_links[i])
        car_image.append(image[image.find('src="')+5:image.find('width=')-2])
    logos = lists.find_all('a', {'class':'emblem'})
    for i in range(len(logos)):
        logo = str(logos[i])
        car_company.append(logo[logo.find('alt')+5:logo.find('height')-2])
    
    prices = lists.find_all('ul', {'class':'lst'})
    for i in range(len(prices)):
        price = prices[i].find('span', class_='cont').string
        if price == None:
            price = 'None'
        else:
            price = price.replace('<span class="cont">', '').replace("</span>",'')
        car_price.append(price)
        size = prices[i].find('li', class_='info')
        size = size.find('span', class_='cont').string        
        size = size.replace('<span class="cont">', '').replace("</span>",'')
        car_size.append(size)

    fuel = lists.find_all('span', {'class':'ell'})
    for i in range(len(fuel)//2):
        fuel_eff = str(fuel[i*2])
        fuel_eff = fuel_eff.replace('<span class="en">', '').replace("</span>",'').replace('<span class="ell">', '').replace('<span class="empty">', '').strip()
        car_fuel_eff.append(fuel_eff)
        fuel_class = str(fuel[i*2+1])
        fuel_class = fuel_class.replace('<span class="cont">', '').replace("</span>",'').replace('<span class="ell">', '').strip()
        car_fuel_class.append(fuel_class)
    print(len(car_price), len(car_size), len(car_fuel_eff), len(car_fuel_class))
    for i in range(len(car_name)):
        car_lists.append(car_name[i].text)
        car_info.append({'id':i+1, 'name':car_name[i].text, 'price': car_price[i], 'image_link':car_image[i],'company': car_company[i], 'size': car_size[i], 'fuel_eff': car_fuel_eff[i], 'engine': car_fuel_class[i]})
    
print(car_info) 
print(car_lists)   
# car_info_json = json.dumps(car_info)

with open('./car_data_out.json','w',encoding='UTF-8') as f:
    json.dump(car_info, f, ensure_ascii=False)



# for i in range(1, 88):
#     url = "https://auto.naver.com/car/mainList.nhn?importYn=Y&page="+str(i)

#     res = requests.get(url)

#     soup = BeautifulSoup(res.content, 'html.parser')

#     lists = soup.find('div', class_='model_group_new')
#     label = lists.find_all('span', {'class':'box'})
#     label = lists.find_all('strong')
#     for lab in label:
#         car_lists.append(lab.text)
# print(len(car_lists))

# save
# print(car_lists)
# with open('car_name.pickle', 'wb') as f:
#     pickle.dump(car_lists, f, pickle.HIGHEST_PROTOCOL)