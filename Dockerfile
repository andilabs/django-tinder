FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

RUN apt-get update

RUN apt-get -qq -y install binutils libproj-dev gdal-bin

COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

COPY . /code/
WORKDIR /code/

EXPOSE 8000