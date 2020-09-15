import cv2
import numpy as np
import glob
import tensorflow as tf
from .models import Clothing, CoordinateClothing

class fashion_tools(object):
    def __init__(self, imageid, model, version=1.1):
        self.imageid = imageid
        self.model = model
        self.version = version

    def get_dress(self, stack=False):
        """limited to top wear and full body dresses (wild and studio working)"""
        """takes input rgb ----> return PNG"""

        name = self.imageid
        file = cv2.imread(name)
        file = tf.image.resize_with_pad(file, target_height=512, target_width=512)
        rgb = file.numpy()
        file = np.expand_dims(file, axis=0) / 255.
        seq = self.model.predict(file)
        seq = seq[3][0, :, :, 0]
        seq = np.expand_dims(seq, axis=-1)
        c1x = rgb * seq
        c2x = rgb * (1 - seq)
        cfx = c1x + c2x
        dummy = np.ones((rgb.shape[0], rgb.shape[1], 1))
        rgbx = np.concatenate((rgb, dummy * 255), axis=-1)
        rgbs = np.concatenate((cfx, seq * 255.), axis=-1)
        if stack:
            stacked = np.hstack((rgbx, rgbs))
            return stacked
        else:
            return rgbs

    def get_patch(self):
        return None





def recommend(predict_idx):
    # 0이 t-shirt 라는 가정
    if predict_idx == 0:

        coordinateImages = CoordinateClothing.objects.filter(c_kind=predict_idx)

        return coordinateImages

    # 아직 미완성...
    elif predict_idx == 1:
        # t_shirt_path = glob.glob("경로설정")

        # # 코디 예시 사진과 url은 (브랜드 - 질 스튜어트 뉴욕)
        # t_shirt_cody_url_list = ["url 따오기"]

        # t_shirt_img_url_list = []

        # for idx, img in enumerate(t_shirt_path):
        #     t_shirt = cv2.imread(img)
        #     t_shirt_img_url_list.append([t_shirt, t_shirt_cody_url_list[idx]])
        pass

    elif predict_idx == 2:
        # t_shirt_path = glob.glob("경로설정")

        # # 코디 예시 사진과 url은 (브랜드 - 질 스튜어트 뉴욕)
        # t_shirt_cody_url_list = ["url 따오기"]

        # t_shirt_img_url_list = []

        # for idx, img in enumerate(t_shirt_path):
        #     t_shirt = cv2.imread(img)
        #     t_shirt_img_url_list.append([t_shirt, t_shirt_cody_url_list[idx]])
        pass

    elif predict_idx == 3:
        # t_shirt_path = glob.glob("경로설정")

        # # 코디 예시 사진과 url은 (브랜드 - 질 스튜어트 뉴욕)
        # t_shirt_cody_url_list = ["url 따오기"]

        # t_shirt_img_url_list = []

        # for idx, img in enumerate(t_shirt_path):
        #     t_shirt = cv2.imread(img)
        #     t_shirt_img_url_list.append([t_shirt, t_shirt_cody_url_list[idx]])
        pass

    elif predict_idx == 4:
        # t_shirt_path = glob.glob("경로설정")

        # # 코디 예시 사진과 url은 (브랜드 - 질 스튜어트 뉴욕)
        # t_shirt_cody_url_list = ["url 따오기"]

        # t_shirt_img_url_list = []

        # for idx, img in enumerate(t_shirt_path):
        #     t_shirt = cv2.imread(img)
        #     t_shirt_img_url_list.append([t_shirt, t_shirt_cody_url_list[idx]])
        pass