# pull official base image
FROM python:3.8

#set work directory
WORKDIR /foxy

# set enviroment variables
ENV  PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# RUN pip3 install --upgrade pip3
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

