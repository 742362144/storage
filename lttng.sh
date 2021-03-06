#!/usr/bin/env bash

# rpm -e --nodeps

SHELL_FOLDER=$(cd "$(dirname "$0")";pwd)
cd $SHELL_FOLDER

yum install -y gcc libuuid libxml2 libxml2-devel popt-devel  autoconf automake libtool

git clone git://git.liburcu.org/userspace-rcu.git


cd userspace-rcu

./bootstrap
./configure --prefix=/usr
make && make install
ldconfig
make clean && make distclean

# uname -r
# https://linuxsoft.cern.ch/cern/centos/7/updates/x86_64/repoview/kernel-devel.html
# rpm -Uvh --oldpackage kernel-devel*

cd $(mktemp -d) &&
wget http://lttng.org/files/lttng-modules/lttng-modules-latest-2.12.tar.bz2 &&
tar -xf lttng-modules-latest-2.12.tar.bz2 &&
cd lttng-modules-2.12.* &&
make &&
make modules_install &&
depmod -a

cd $(mktemp -d) &&
wget http://lttng.org/files/lttng-ust/lttng-ust-latest-2.12.tar.bz2 &&
tar -xf lttng-ust-latest-2.12.tar.bz2 &&
cd lttng-ust-2.12.* &&
./configure &&
make &&
make install &&
ldconfig