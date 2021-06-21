FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install --no-install-recommends \
        imagemagick  \
        libzbar-dev && \
    apt-get clean

RUN mkdir -p /srv/project/media && \
    mkdir -p /srv/project/static


VOLUME /srv/project/media /srv/project/static

WORKDIR /srv/project/
RUN pip install --upgrade pip
COPY . /srv/project/
RUN pip install --no-cache-dir -r /srv/project/requirements.txt
RUN python -m deeppavlov download /usr/local/lib/python3.7/site-packages/deeppavlov/configs/squad/squad_ru.json
ENV DJANGO_SETTINGS_MODULE=core.settings
EXPOSE 8000