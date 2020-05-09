#!/usr/bin/env bash

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
cd $SHELL_FOLDER

protoc --python_out=. cmdcall.proto

python -m py_compile *.py

cp -rf *.pyc Dockerfile docker/


cd docker
docker build -t mybench .