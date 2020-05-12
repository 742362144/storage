FROM mybench-base:latest

ADD *.py /home/storage/

ADD start.sh /home/storage/

ADD *.proto /home/storage/

WORKDIR /home/storage

CMD bash start.sh
