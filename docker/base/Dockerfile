FROM python:slim

RUN mkdir -p /home/storage

RUN pip3 install

RUN pip3 install grpcio protobuf grpcio-tools

RUN apt-get update -y

RUN apt-get install -y gcc flex bison make

ADD filebench-1.5-alpha3.tar.gz /home/

RUN cd /home && ls

RUN cd /home/filebench-1.5-alpha3 && ./configure && make && make install

