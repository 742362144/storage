import os

from util import runCmd

WORKLOAD_DIR = '/home/nfs/filebench-1.5-alpha3/workloads'

for wl in os.listdir(WORKLOAD_DIR):
    runCmd('filebench -f %s/%s > %s.log' % (WORKLOAD_DIR, wl, wl.split('.')[0]))