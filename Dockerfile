# FROM ubuntu:20.04
FROM python:3.10.12

COPY ./* /
RUN pip install -r requirements_docker.txt
EXPOSE 2333

ENTRYPOINT ["python", "model_with_docker.py"]