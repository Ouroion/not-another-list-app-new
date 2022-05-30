FROM python:3.9

MAINTAINER newtonmccollum@gmail.com

WORKDIR /src
COPY ./src/requirements.txt /src
RUN pip install -r requirements.txt

COPY ./src/ /src

CMD ["python", "./main.py"]