FROM nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --upgrade setuptools pip

