from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView

from .forms import ClothingForm
from .models import Clothing, CoordinateClothing
from .coordinate_clothings import fashion_tools, recommend, resize_with_padding
from PIL import Image, ImageOps
import cv2
import numpy as np
import tensorflow as tf


class Home(TemplateView):
    template_name = 'home.html'


def clothing_list(request):
    clothings = Clothing.objects.all()
    return render(request, 'clothing_list.html', {
        'clothings': clothings
    })


def upload_clothing(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clothing_list')
    else:
        form = ClothingForm()
    return render(request, 'upload_clothing.html', {
        'form': form
    })


def delete_clothing(request, pk):
    if request.method == 'POST':
        clothing = Clothing.objects.get(pk=pk)
        clothing.delete()
    return redirect('clothing_list')


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



        context = {
            'coordinateImages': result[0],
            'clothing_kind': result[1]
        }

    return render(request, 'coordinate_list.html', context)

