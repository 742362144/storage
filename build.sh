#!/usr/bin/env bash

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
cd $SHELL_FOLDER

cp -rf filebench-1.5-alpha3.tar.gz docker/base
cd docker/base

docker build -t mybench-base .

cd $SHELL_FOLDER

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. cmdcall.proto

#python3 -O -m compileall -b .

cp -rf *.py Dockerfile cmdcall.proto start.sh docker/


cd docker
docker build -t mybench-new .
