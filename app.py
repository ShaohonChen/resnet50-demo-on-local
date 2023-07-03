import json
import os
import requests

import gradio as gr

from utils import encode_img

url = os.environ.get("API_URL")
print(f"MY SERVER:{url}")

def inference(img):
    b64_code = encode_img(img)
    # 以字典的形式构造数据
    data = {
        'img': b64_code
    }
    # 对接口进行请求，
    r = requests.post(url, data=data)  # 与 get 请求一样，r 为响应对象
    result = r.content.decode('utf-8')
    result=json.loads(result)
    return result


if __name__ == "__main__":
    interface = gr.Interface(fn=inference, inputs="image",
                             outputs=gr.Label(),
                             title="ResNet50 (demo on local with GPU)"
                             )
    interface.launch(server_name="0.0.0.0")
    # interface.launch(server_port=7680)


