FROM python:3.8-alpine

WORKDIR /usr/src/app
ENV PYTHONUNFUFFERED=1

# set up python virtual environment and install requirements
COPY requirements.in .

# Install GCC (Alpine uses musl but we compile and link dependencies with GCC)
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && apk add linux-headers \
    && apk add postgresql-dev \
    && pip install pip-tools \
    && pip-compile \
    && pip-sync \
    && apk del .build-deps
