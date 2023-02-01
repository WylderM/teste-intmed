FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN chmod -R 777 /code/ 

COPY ./requirements.txt /code/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt 


EXPOSE 8000