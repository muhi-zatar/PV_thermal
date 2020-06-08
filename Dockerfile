FROM ubuntu:16.04

MAINTAINER Muhy Zater (muhizatar95@gmail.com)
# Install necessary system packages
RUN apt-get clean &&  \
    apt-get update &&  \
    apt-get install -yq --no-install-recommends awscli  \
                                                python3.5  \
                                                python3-pip \
                                                locales \
                                                git \
                                                curl \
                                                openssh-server &&\
    rm -rf /var/lib/apt/lists/* && \
    pip3 install --no-cache-dir --upgrade pip setuptools

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
ENV LANG=en_US.UTF-8   \
    LANGUAGE=en_US.UTF-8   \
    LC_ALL=en_US.UTF-8


ENV APP_USER="muhi" \
    APP_DIR="/app"
RUN adduser --disabled-password --gecos "" "$APP_USER"

#ENV SSH_DIR="/root/.ssh"
#RUN mkdir -p "$SSH_DIR"
#COPY private_key "$SSH_DIR/id_rsa"
#RUN chmod 400 "$SSH_DIR/id_rsa"
#RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> "$SSH_DIR/config"

#ARG AWS_ACCESS_KEY_ID
#ARG AWS_SECRET_ACCESS_KEY
#ARG AWS_DEFAULT_REGION=eu-west-1
#ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
#ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
#ENV AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION

WORKDIR "$APP_DIR"
COPY PV_detection "$APP_DIR/PV_detection"
COPY ["requirements*.txt", "README.md", "config.py", "$APP_DIR/"]
RUN mkdir "$APP_DIR/mlogs" && chown -R "$APP_USER"."$APP_USER" "$APP_DIR"
RUN pip3 install --no-cache-dir --upgrade --requirement "$APP_DIR/requirements.txt"

#Run the APP:
USER "$APP_USER"
CMD ./run.sh
USER root
USER "$APP_USER"
