FROM python:3.7-slim
RUN mkdir -p /app/user
RUN mkdir /src
WORKDIR /app/user

ADD requirements.txt /app/user
RUN pip install --src /src -r requirements.txt
RUN pip install --src /src ipython
ADD . /app/user
