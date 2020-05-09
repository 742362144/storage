FROM python:slim

RUN mkdir -p /home/storage

ADD *.pyc /home/storage/

ADD start.sh /home/storage/

WORKDIR /home/storage

CMD bash start.sh
