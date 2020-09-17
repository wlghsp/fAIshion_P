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
        coordinateImages = CoordinateClothing.objects.raw('''
                            SELECT * FROM core_coordinateclothing WHERE c_kind = 0 ORDER BY random() LIMIT 3
                            ''')
        result = []
        kind = "티셔츠"
        result.append(coordinateImages)
        result.append(kind)

        return result

    elif predict_idx == 1:
        pass

    # 셔츠
    elif predict_idx == 2:
        coordinateImages = CoordinateClothing.objects.raw('''
                            SELECT * FROM core_coordinateclothing WHERE c_kind = 2 ORDER BY random() LIMIT 3
                            ''')
        result = []
        kind = "셔츠"
        result.append(coordinateImages)
        result.append(kind)
        return result

    elif predict_idx == 3:
        pass

    elif predict_idx == 4:
        pass