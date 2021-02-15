FROM python:3.7-alpine 

MAINTAINER Khoa Pham

ENV PYTHONUNBUFFERED 1 
# ? 

COPY ./requirements.txt /requirements.txt  
RUN pip install -r requirements.txt

# created on docker_env folder app
RUN mkdir /app 
WORKDIR /app
COPY ./app /app

# create a new use to use for security
# separate scope to avoid hacker get all directory
RUN adduser -D user 
USER user