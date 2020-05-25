#!/usr/bin/env bash

yum install centos-release-gluster -y
yum install -y glusterfs glusterfs-server glusterfs-fuse glusterfs-rdma

systemctl start glusterd
systemctl enable glusterd

gluster volume create glusterfs1 node31:/home/glusterfs/glusterfs1 force
gluster volume create glusterfs2 node31:/home/glusterfs/glusterfs2 force
gluster volume create glusterfs3 node31:/home/glusterfs/glusterfs3 force
gluster volume create glusterfs4 node31:/home/glusterfs/glusterfs4 force
gluster volume create glusterfs5 node31:/home/glusterfs/glusterfs5 force
gluster volume create glusterfs6 node31:/home/glusterfs/glusterfs6 force
gluster volume start glusterfs1
gluster volume start glusterfs2
gluster volume start glusterfs3
gluster volume start glusterfs4
gluster volume start glusterfs5
gluster volume start glusterfs6
gluster volume stop glusterfs1
gluster volume delete glusterfs1


#mount -t glusterfs node30:glusterfs1 /home/nfs1/glusterfs/glusterfs1