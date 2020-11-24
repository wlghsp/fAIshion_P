from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from .forms import ClothingForm
from .models import Member, Clothing, CoordinateClothing
from .coordinate_clothings import fashion_tools, recommend, resize_with_padding
from PIL import Image, ImageOps
import cv2
import numpy as np
import tensorflow as tf
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
ERROR_MSG = {
    'ID_EXIST': '이미 사용 중인 아이디 입니다.',
    'ID_NOT_EXIST': '존재하지 않는 아이디 입니다.',
    'ID_PW_MISSING': '아이디와 비밀번호를 다시 확인해주세요.',
    'PW_CHECK': '비밀번호가 일치하지 않습니다.',

}

# 비로그인 시 첫화면으로 리다이렉트 시킴
# URL_LOGIN = '/'


class Home(TemplateView):
    template_name = 'index.html'


def signup(request):


    context = {
        'error': {
            'state': False,
            'msg': ''
        }
    }

    if request.method == "POST":

        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']

        # 추가
        name = request.POST['name']

        if (user_id and user_pw):

            user = User.objects.filter(username=user_id)

            if len(user) == 0:

                if user_pw == user_pw_check:

                    created_user = User.objects.create_user(
                        username=user_id,
                        password=user_pw
                    )

                    # 추가
                    Member.objects.create(
                        user=created_user,
                        name=name,
                    )

                    auth.login(request, created_user)
                    loginUser = Member.objects.get(user=created_user)
                    print(loginUser.id)
                    request.session['user'] = loginUser.id

                    return redirect('home')

                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_EXIST']

        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(request, 'home.html', context)

def login(request):

    context = {
        'error': {
            'state': False,
            'msg': ''
        },
    }
    if request.method == 'POST':

        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        user = User.objects.filter(username=user_id)

        if (user_id and user_pw):
            if len(user) != 0:

                user = auth.authenticate(
                    username=user_id,
                    password=user_pw
                )
                if user != None:
                    auth.login(request, user)
                    loginUser = Member.objects.get(user=user)
                    print(loginUser.id)
                    request.session['user'] = loginUser.id

                    return redirect('home')
                else:
                    context['error']['state'] = True
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['state'] = True
                context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']
        else:
            context['error']['state'] = True
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']
    return render(request, 'home.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')


# @login_required(login_url=URL_LOGIN)
def closet(request):
    clothings = Clothing.objects.all()
    return render(request, 'closet.html', {
        'clothings': clothings
    })

# @login_required(login_url=URL_LOGIN)
def add_clothing(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('closet')
    else:
        form = ClothingForm()
    return render(request, 'add_clothing.html', {
        'form': form
    })

# @login_required(login_url=URL_LOGIN)
def delete_clothing(request, pk):
    if request.method == 'POST':
        clothing = Clothing.objects.get(pk=pk)
        clothing.delete()
    return redirect('closet')

# @login_required(login_url=URL_LOGIN)
def coordinate_clothing(request, pk):
    if request.method == 'POST':
        clothing = Clothing.objects.get(pk=pk)

        # 모델 임포트 후 의상 부분만 추출하는 코드.
        # 훈련된 모델 가지고 오는 경로 설정.
        saved = tf.keras.models.load_model('./mysite/core/train_models/topwears.h5', custom_objects={'tf': tf})
        f = '.' + clothing.image.url
        print(f)
        img = Image.open(f)
        img = resize_with_padding(img, (750, 750))
        img = np.array(img)

        ###running code
        api = fashion_tools(img, saved)
        image = api.get_dress(True)

        # 이미지 자르고, 투명값 검정배경 입혀주기.
        image_crop = image[:, 512:]
        image_crop = np.uint8(image_crop)

        for i in image_crop:
            for j in i:
                if j[3] < 40:
                    j[0] = 0
                    j[1] = 0
                    j[2] = 0

        # 리사이즈 인풋값 맞춰 주기.
        image_resize = cv2.resize(image_crop, (28, 28))

        # 그레이 스케일.. 후 픽셀 출력..
        image_gray = cv2.cvtColor(image_resize, cv2.COLOR_BGRA2GRAY)

        # 정규화 해준다.
        input_image = image_gray / 255.0

        # input값이 3차원 이여서 차원을 늘려준다.
        input_image = np.reshape(input_image, (1, 28, 28, 1))

        # 저장된 훈련모델 불러오는 방법
        model = tf.keras.models.load_model('./mysite/core/train_models/fAIshion_P_T9.h5', custom_objects={'tf': tf})

        # 예측 수행
        input_predict = model.predict(input_image) + 1
        print(input_predict)

        # 예측 결과 확인
        max_value = np.max(input_predict)
        max_idx = np.where(input_predict == max_value)
        predict_idx = max_idx[1][0]
        print(predict_idx)

        ## 여기까지 오케이 ^_^

        # recommend return 값 받기
        result = recommend(predict_idx)
        # result = recommend(2)

        clothings = Clothing.objects.all()

        context = {
            'coordinateImages': result[0],
            'clothing_kind': result[1],
            'clothings': clothings
        }

    return render(request, 'recommend.html', context)

