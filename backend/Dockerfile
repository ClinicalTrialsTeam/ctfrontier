# Modified from https://github.com/tiangolo/meinheld-gunicorn-docker
FROM python:3.8-alpine3.11

ENV PYTHONUNFUFFERED=1
ENV MODE=$MODE
ENV DJANGO_SECRET=$DJANGO_SECRET
ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV DB_PASSWORD=$DB_PASSWORD
ENV ELASTICSEARCH_ENABLED=$ELASTICSEARCH_ENABLED
ENV ES_HOST=$ES_HOST
ENV ES_PORT=$ES_PORT
ENV APP_MODULE=core.wsgi:application

COPY ./ /app
WORKDIR /app/

# Install GCC (Alpine uses musl but we compile and link dependencies with GCC)
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libc-dev \
    && apk add uwsgi-python3 \
    && apk add linux-headers \
    && apk add postgresql-dev \
    && pip install --no-cache-dir pip-tools \
    && pip install meinheld gunicorn \
    && pip-compile requirements/base.in \
    && pip install --no-cache-dir -r requirements/base.txt \
    && apk del .build-deps gcc libc-dev

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

ENV PYTHONPATH=/app

EXPOSE 80

CMD ["/start.sh"]
