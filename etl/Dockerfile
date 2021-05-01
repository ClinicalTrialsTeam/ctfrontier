FROM python:3.8.4-slim-buster

ARG USER=django-user

ENV PYTHONUNFUFFERED=1
ENV MODE=$MODE
ENV DJANGO_SECRET=$DJANGO_SECRET
ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV DB_PASSWORD=$DB_PASSWORD

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install sudo vim 

# set up passwordless sudo for user
RUN useradd -m -s /bin/bash $USER && \
    echo "$USER ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER

WORKDIR /usr/src/app

# Copy application files over
COPY . .

# Grant user application file permissions and start running as user
RUN chown -R $USER /usr/src/app
USER $USER

# Make sure pip-compile and pip-sync are on PATH
ENV PATH "$PATH:/home/django-user/.local/bin"

RUN pip install --no-cache-dir pip-tools \
      && pip-compile requirements/base.in \
      && pip install --no-cache-dir -r requirements/base.txt \
      && pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_sm-0.4.0.tar.gz
