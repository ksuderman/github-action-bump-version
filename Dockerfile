# Container image that runs your code
FROM python:3.10.0-alpine

RUN apk update && apk add bash

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY bump.py /bump.py
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
