from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .models import users
from .models import InputFile
from .models import cars
from .models import likecars
from .serializers import LikeCarsSerializer
from .serializers import UsersSerializer
from .serializers import InputFileSerializer
from .serializers import CarsSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json
import os.path
from rest_framework.parsers import MultiPartParser
from django.db.models import Count
from rest_framework.renderers import JSONRenderer
import back.guess
import urllib.request


@api_view(['GET'])
def likecarAll(request):
    if request.method == 'GET':
        data = likecars.objects.filter().values('carId').annotate(
            like=Count('carId')).order_by('-like')[:5]
        li = []

        for i in data:
            serializer = CarsSerializer(cars.objects.get(id=i['carId']))
            li.append(serializer.data)
        aa = JSONRenderer().render(li)
        return HttpResponse(aa, status=200)


@api_view(['GET'])
def likecarUser(request, pk):
    if request.method == 'GET':
        data = likecars.objects.filter(userId=pk).values('carId')
        if(len(data) == 0):
            return HttpResponse(status=400)
        else:
            li = []
            for i in data:
                serializer = CarsSerializer(cars.objects.get(id=i['carId']))
                li.append(serializer.data)
            aa = JSONRenderer().render(li)
            print(aa)
            return HttpResponse(aa, status=200)


@api_view(['POST'])
def likecar(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        like = likecars.objects.filter(
            userId=data['userId']) & likecars.objects.filter(carId=(data['carId']))
        print(like)
        if(len(like) == 0):
            print("추가~~~")
            serializer = LikeCarsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                result = likecars.objects.filter(userId=data['userId'])
                serializer = LikeCarsSerializer(result, many=True)

                li = []
                for i in serializer.data:
                    obj = CarsSerializer(cars.objects.get(id=i['carId']))
                    print(obj.data)
                    li.append(obj.data)
                aa = JSONRenderer().render(li)
                return HttpResponse(aa, status=200)
        else:
            print("삭제~~~")
            like.delete()
            result = likecars.objects.filter(userId=data['userId'])
            serializer = LikeCarsSerializer(result, many=True)

            li = []
            for i in serializer.data:
                obj = CarsSerializer(cars.objects.get(id=i['carId']))
                print(obj.data)
                li.append(obj.data)
            aa = JSONRenderer().render(li)
            return HttpResponse(aa, status=200)


class usersPostview(APIView):
    parser_classes = (MultiPartParser, )

    def post(self, request, format=None):
        if(request.method == 'POST'):
            print(request.data)
            serializer = UsersSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def put(self, request, pk):
        if(request.method == 'PUT'):
            obj = UsersSerializer(users.objects.get(pk=pk))
            print(obj.data)
            data = UsersSerializer(JSONParser().parse(request))
            print(data.data)
            serializer = UsersSerializer(obj, data=data)
            if serializer.is_valid():
                serializer.save()
                obj.delete()
                return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def join(request):
    # 전체회원조회
    if request.method == 'GET':
        # GET통신이면 users모델전부 불러옴
        queryset = users.objects.all()
        # 불러온 모델을 json형태로 맞춰줌
        serializer = UsersSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False, content_type='application/json; charset=utf-8')
    # 회원가입기능
    elif request.method == 'POST':
        # POST 통신이면 request로 들어온 JSON형태 데이터 추출
        data = JSONParser().parse(request)

        # 추출한 데이터와 우리가 선언한 serializer포맷이랑 비교 후
        serializer = UsersSerializer(data=data)
        # 같은데이터면
        if serializer.is_valid():
            # 저장
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        # 다른형태면 오류 보냄
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    obj = users.objects.get(pk=pk)
    # 회원 정보 하나 가져오기
    if request.method == 'GET':
        serializer = UsersSerializer(obj)
        return JsonResponse(serializer.data, status=201)
    # 회원정보 업데이트 하기
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    # 회원 삭제하기
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


@api_view(['POST'])
def login(request):
    # login 기능
    # login TEST 할 때, identify ,password 제이슨 형태로 보내야함
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        search_id = data['identify']
        try:
            obj = users.objects.get(identify=search_id)
            if(obj.password == data['password']):
                print(search_id)
                print(obj.password)
                serializer = UsersSerializer(obj)
                return JsonResponse(serializer.data, status=200)
            else:
                return JsonResponse({"message:": "login fail"}, status=400)
        except Exception as ex:
            return JsonResponse({"message": "login fail"}, ex, status=400)


@api_view(['GET'])
def car(request):
    if request.method == 'GET':
        queryset = cars.objects.all()
        serializer = CarsSerializer(queryset, many=True)
        return JsonResponse(serializer.data, status=201, safe=False)


@api_view(['GET'])
def car_datail(request, num):
    obj = cars.objects.get(id=num)
    if request.method == 'GET':
        serializer = CarsSerializer(obj)
        return JsonResponse(serializer.data, status=201)


@api_view(['GET'])
def car_company_list(request, company):
    if request.method == 'GET':
        obj = cars.objects.filter(company__icontains=company)
        serializer = CarsSerializer(obj, many=True)
        print(serializer)
        return JsonResponse(serializer.data, status=201, safe=False)


@api_view(['GET'])
def car_name_list(request, name):
    if request.method == 'GET':
        try:
            obj = cars.objects.filter(name__icontains=name)
            serializer = CarsSerializer(obj, many=True)
            print(serializer)
            return JsonResponse(serializer.data, status=201, safe=False)
        except Exception as ex:
            return JsonResponse(ex, status=400)


@api_view(['GET'])
def car_companyAll(request):
    if request.method == 'GET':
        obj = cars.objects.filter().values('company').distinct()
        print(obj)
        return HttpResponse(obj, status=201)


@api_view(['POST'])
def detailAI(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        urllib.request.urlretrieve(data['link'], './media/detailai.png')
        imagePath = './media/detailai.png'
        result = back.guess.run_inference_on_image(
            imagePath)
        print(result)
        li = []
        for i in result:
            serializer = CarsSerializer(cars.objects.get(name=str(i[0])))
            print(serializer.data)
            li.append(serializer.data)

        aa = JSONRenderer().render(li)
        return HttpResponse(aa, status=200)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = InputFileSerializer(data=request.data)
        print(request.data['file'])
        if file_serializer.is_valid():
            file_serializer.save()
            result = back.guess.run_inference_on_image(
                "./media/" + str(request.data['file']))
            print(result)
            li = []
            for i in result:
                serializer = CarsSerializer(
                    cars.objects.get(name=str(i[0])))
                print(serializer.data)
                li.append(serializer.data)

            aa = JSONRenderer().render(li)
            return HttpResponse(aa, status=200)


# @api_view(['GET'])
# def insertdata(request):
#    if(request.method == 'GET'):
#        with open('./back/cardata.json', encoding='utf-8') as f:
#            json_data = json.load(f)
#            print(json_data)
#            for i in range(len(json_data)):
#                serializer = CarsSerializer(data=json_data[i])
#                print(serializer)
#                if serializer.is_valid():
#                    print("dddddd")
#                    serializer.save()
#                else:
#                    print("aaaa")
#            return JsonResponse(serializer.data, status=201)
