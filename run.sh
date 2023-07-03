docker build -t resnet50server:v0 .
docker run -d -p 2333:$1 resnet50server:v0
export API_URL=http://127.0.0.1:$1/model
python app.py