FROM nginx:stable-alpine

RUN mkdir -p /srv/project/media &&\
    mkdir -p /srv/project/static

COPY conf.d/ /etc/nginx/conf.d
COPY run.sh /run.sh

ENTRYPOINT []
CMD /run.sh
