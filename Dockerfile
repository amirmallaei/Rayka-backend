FROM python:3.11

LABEL Maintainer="AMIRMALLAEI@Gmail.com"
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies

RUN mkdir /src
COPY ./src /src
WORKDIR /src/
RUN apt-get update

WORKDIR /src
ADD /src/requirements.txt /src/requirements.txt 

RUN pip install -r requirements.txt 
