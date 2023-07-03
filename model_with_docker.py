import torch
from torchvision import transforms as T
from torchvision.models import resnet50

from flask import Flask, request

from utils import decode_img

class Model:
    def __init__(self):
        self.model = resnet50(pretrained=True).eval()
        self.preprocess = T.Compose([
            T.ToTensor(),
            T.Resize([256, ]),
            T.CenterCrop(224),
            # T.PILToTensor(),
            T.ConvertImageDtype(torch.float),
            T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        with open("imagenet_classes.txt", "r") as f:
            self.categories = [s.strip() for s in f.readlines()]

    def predict(self, img, top_n=5):
        batch = self.preprocess(img).unsqueeze(0)
        prediction = self.model(batch).squeeze(0).softmax(0)
        # class_id = prediction.argmax().item()
        # score = prediction[class_id].item()
        # category_name = self.categories[class_id]
        # return {category_name: score}
        score, label = prediction.topk(top_n)
        return {self.categories[int(c)]: float(s) for c, s in zip(label, score)}


model = Model()

app = Flask(__name__)



@app.route('/model', methods=['POST', 'GET'])
def inference():
    if request.method == "POST":
        img = request.form['img']
        img = decode_img(img)
        label = model.predict(img, top_n=5)
        return label
    else:
        return "Please use POST"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2333)
