FROM python:3.9
ARG TG_API_TOKEN
ENV TG_API_TOKEN = $TG_API_TOKEN
EXPOSE 5000
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install python-qrtools --no-install-recommends &&\
    apt-get clean

RUN mkdir -p /srv/tg_bot
WORKDIR /srv/tg_bot/
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt