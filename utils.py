import base64
import numpy as np
import cv2


def encode_img(img):
    img = np.array(img)
    img_str = cv2.imencode('.jpg', img)[1].tostring()  # 将图片编码成流数据，放到内存缓存中，然后转化成string格式
    b64_code = base64.b64encode(img_str)  # 编码成base64
    return b64_code


def decode_img(img):
    # img = img.content.decode('utf-8')
    img = base64.b64decode(img)
    np_arr = np.fromstring(img, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img
