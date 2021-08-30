FROM       ubuntu:16.04 as BACKINTIME-BUILDER
# Using 16.04 for python 3.5

ARG        BACKINTIME_VERSION=1.2.0~alpha0

RUN        apt-get update && \
           apt-get install -q -y \
             git \
             rsync \
             openssh-client \
             sshfs \
             dpkg-dev \
             dh-python \
             debhelper \
             python3 \
             python3-keyring \
             python3-dbus && \
           rm -rf /var/lib/apt/lists/* /var/tmp/*

WORKDIR    /tmp/backintime

RUN        git clone https://github.com/belsander/backintime.git src

WORKDIR    /tmp/backintime/src

RUN        ./makedeb.sh

WORKDIR    /tmp/backintime

RUN        mv backintime-common_${BACKINTIME_VERSION}_all.deb  \
             backintime-common.deb


FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install kubernetes

RUN        apt-get update && \
           apt-get install -q -y \
             vim   \
             rsync \
             nfs-common \
             sshfs \
             openssh-server \
             openssh-client \
             python3-keyring \
             python3-dbus \
             cron && \
           rm -rf /var/lib/apt/lists/* /var/tmp/*
#RUN        add-apt-repository universe
WORKDIR    /root

COPY       --from=BACKINTIME-BUILDER /tmp/backintime/backintime-common.deb .

RUN        dpkg -i backintime-common.deb && \
           rm -f backintime-common.deb

RUN        mkdir .ssh && \
           chmod 700 .ssh
RUN        mkdir -p  /root/backintime/worker/imen/1
RUN        service cron start
COPY       do-backup.sh .
COPY	   backintime.example /root/.config/backintime/config
COPY       backintime.example .
COPY       main.py .
EXPOSE 22
#ENTRYPOINT ["sh", "-c", "/root/do-backup.sh"]
