FROM python:3.9.6

ENV DOCKER_USER_ID 1000
ENV DOCKER_GROUP_ID 1000

ENV PYTHONUNBUFFERED 1

RUN groupadd -g ${DOCKER_GROUP_ID} user \
    && useradd --shell /bin/bash -u $DOCKER_USER_ID -g $DOCKER_GROUP_ID -o -c "" -m user

WORKDIR /opt/chrome-headless-client

RUN pip install requests

USER user
