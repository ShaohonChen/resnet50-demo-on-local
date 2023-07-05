# resnet50 demo on local

## Description

This project is a demo of how to deploy a Resnet50 model API using the Flask framework. We can build a model that can be accessed via a web API using Flask. This comes with many benefits, including saving server costs or containing some private data. For example, when you need to build a demo of a deep learning model that requires a GPU using SwanHub, HuggingFace, or Replicate, you can build an API on your local GPU server and access it using the Gradio backend online.

Pre-requisites you may need:

**Flask** is a lightweight web framework developed in Python. It is widely used to build web applications and APIs, as well as for rapid prototyping.

**Docker** is an open-source containerization platform designed to simplify the process of building, deploying, and managing applications. By using container technology, Docker allows developers to package an application and all its dependencies into a standalone, portable container.

## Installation & Usage

This project consists of two parts, the model API service and the Gradio frontend rendering service. You can deploy them separately on two different servers (which need to be able to access each other), or you can deploy them on the same server.

The model API server can be run via Docker. Make sure the deployment server has Docker installed. You can refer to [Install Docker](https://docs.docker.com/desktop/) for instructions. Run the following command to start it:

```
bash run.sh <API_PORT>
```

Replace `<API_PORT>` with the port number for the model API service, ensuring that it is not already in use.

The Gradio frontend server requires Python >= 3.8 to be installed on the server. Run the following command to install the necessary dependencies:

```
pip install -r requirements.txt
```

Alternatively, you can upload this project to SwanHub and choose to run the Gradio-based demo using the environment built from the `requirements.txt` file. Refer to [Getting Started with SwanHub](https://geektechstudio.feishu.cn/wiki/SpdSwReT8iNF5NkfngwciSS6nVf) for a detailed tutorial. You can also deploy it using HuggingFace's Space or Replicate.

Next, run the following command to set the access URL for your model API:

```
export API_URL=http://<IP or URL>:<API_PORT>/model
```

Finally, run the following command to start your Gradio service:

```
python app.py
```

## License

This project is licensed under the [GPL](https://www.gnu.org/licenses/gpl-3.0.en.html) license.

## Author Information

This project is developed by 陈少宏 (shaohon chen).

For any inquiries or feedback, please contact shaohon chen via email: shaohon_chen@115lab.club.

## Thanks

Thanks for [Auto-README](https://swanhub.co/SwanHub/Auto-README/demo) help me write this readme! : )