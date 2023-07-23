FROM ubuntu:latest
LABEL authors="Shane"

ENTRYPOINT ["top", "-b"]