FROM python:3.8-alpine3.11

ENV PYTHONUNFUFFERED=1
ENV MODE=$MODE
ENV DJANGO_SECRET=$DJANGO_SECRET
ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT
ENV DB_PASSWORD=$DB_PASSWORD

ENV MODULE_NAME=core.wsgi
ENV VARIABLE_NAME=application

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

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

ENV PYTHONPATH=/app

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Meinheld
CMD ["/start.sh"]

# WORKDIR /app
# COPY . /app

# ARG USER=django-user

# ENV PYTHONUNFUFFERED=1
# ENV MODE=$MODE
# ENV DJANGO_SECRET=$DJANGO_SECRET
# ENV DB_HOST=$DB_HOST
# ENV DB_PORT=$DB_PORT
# ENV DB_PASSWORD=$DB_PASSWORD

# RUN set -ex && apk --no-cache add sudo

# # Add user and set up passwordless sudo
# RUN adduser -D $USER \
#     && echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER \
#     && chmod 0440 /etc/sudoers.d/$USER

# # Copy application files over
# WORKDIR /app
# COPY . /app
# ENV UWSGI_INI /app/uwsgi.ini

# # Grant user application file permissions and start running as user
# RUN chown -R $USER /app
# USER $USER

# # Make sure pip-compile and pip-sync are on PATH
# ENV PATH "$PATH:/home/django-user/.local/bin"

# # Install GCC (Alpine uses musl but we compile and link dependencies with GCC)
# RUN sudo apk add --no-cache --virtual .build-deps gcc musl-dev \
#     && sudo apk add uwsgi-python3 \
#     && sudo apk add linux-headers \
#     && sudo apk add postgresql-dev \
#     && pip install --no-cache-dir pip-tools \
#     && pip-compile requirements/base.in \
#     && pip install --no-cache-dir -r requirements/base.txt \
#     && sudo apk del .build-deps

# USER root
# EXPOSE 80

#CMD ["python", "manage.py" "migrate", "&&", "nginx", "-c", "nginx.conf", "-g", "daemon off;"]

# Run uwsgi server
# FROM base as build
# EXPOSE 8000
# CMD python manage.py migrate\ 
#   && uwsgi \
#   --plugins-dir /usr/lib/uwsgi/ \
#   --need-plugin python --plugins-list \
#   --ini uwsgi.ini \
#   --show-config

# CMD uwsgi \
#   --plugins-dir /usr/lib/uwsgi/ \
#   --need-plugin python --plugins-list \
#   --ini uwsgi.ini \
#   --show-config




#uwsgi --shared-socket 0.0.0.0:443 --uid roberto --gid roberto --https =0,foobar.crt,foobar.key


# # # production environment
# FROM tiangolo/uwsgi-nginx:python3.8-alpine
# EXPOSE 80
# COPY --from=base /usr/src/app /usr/src/app
# ENV UWSGI_INI /usr/src/app/uwsgi.ini
# WORKDIR /usr/src/app
# CMD ["nginx", "-c", "nginx.conf", "-g", "daemon off;"]


