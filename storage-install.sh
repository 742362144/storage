#!/usr/bin/env bash

yum install centos-release-gluster -y
yum install -y glusterfs glusterfs-server glusterfs-fuse glusterfs-rdma

systemctl start glusterd
systemctl enable glusterd

gluster volume create  swarm-manager:/home/glusterfs/
gluster volume create glusterfs1 node30:/home/glusterfs/glusterfs1 force
gluster volume start glusterfs1
gluster volume stop glusterfs1
gluster volume delete glusterfs1