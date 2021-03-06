FROM ubuntu:focal

# set environment variables for tzdata
ARG TZ=America/New_York
ENV TZ ${TZ}

# include manual pages and documentation
RUN DEBIAN_FRONTEND=noninteractive apt-get update && yes | unminimize

# install programs used for system exploration
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y install \
        blktrace \
        linux-tools-generic \
        strace \
        tcpdump --fix-missing

# install interactive programs (emacs, vim, nano, man, sudo, etc.)
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
        bc \
        curl \
        dc \
        emacs-nox \
        git \
        git-doc \
        man \
        micro \
        nano \
        sudo \
        vim \
        wget

# set up libraries
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
        libreadline-dev \
        locales \
        wamerican

# install programs used for networking
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \
        dnsutils \
        inetutils-ping \
        net-tools \
        netcat \
        telnet \
        traceroute

# install python
RUN DEBIAN_FRONTEND=noninteractive apt-get update \
    && sudo apt-get -y install software-properties-common python 3.9 python3-pip

# update python3 and python version to python3.9
RUN DEBIAN_FRONTEND=noninteractive update-alternatives --install \
    /usr/bin/python3 python3 /usr/bin/python3.8 1
RUN DEBIAN_FRONTEND=noninteractive update-alternatives --install \
    /usr/bin/python3 python3 /usr/bin/python3.9 2
RUN DEBIAN_FRONTEND=noninteractive update-alternatives --install \
    /usr/bin/python python /usr/bin/python3.8 1
RUN DEBIAN_FRONTEND=noninteractive update-alternatives --install \
    /usr/bin/python python /usr/bin/python3.9 2

# update pip to point to pip3
RUN DEBIAN_FRONTEND=noninteractive update-alternatives --install \
    /usr/bin/pip pip /usr/bin/pip3 1

# set up default locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8

# remove unneeded .deb files
RUN rm -r /var/lib/apt/lists/*

# set up passwordless sudo for user ct-user
RUN useradd -m -s /bin/bash ct-user && \
    echo "ct-user ALL=(ALL:ALL) NOPASSWD: ALL" > /etc/sudoers.d/ct-init

# create binary reporting version of dockerfile
RUN (echo '#\!/bin/sh'; echo 'echo 5') > /usr/bin/ct-docker-version; chmod ugo+rx,u+w,go-w /usr/bin/ct-docker-version

# git build arguments
ARG USER=CT\ User
ARG EMAIL=nobody@example.com

WORKDIR /usr/src/app
ENV PYTHONUNFUFFERED=1

# set up python virtual environment and install requirements
COPY requirements.in .
RUN pip install pip-tools && pip-compile && pip install -r requirements.txt