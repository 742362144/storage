import os
import threading
import time
import traceback
import uuid
import random

from client import rpcCall, HOST
from server import DEFAULT_PORT
from util import *

DOCKER_DIR = '/sys/fs/cgroup/memory/docker'
TRACE_DIR = '/root/'
LTTNG_HOME = '/root/lttng-traces'

# mounts = [
#     '/home/nfs/nfs1',
#     '/home/nfs/nfs2',
#     '/home/nfs/nfs3',
#     '/home/nfs/nfs4',
#     '/home/nfs/nfs5',
#     '/home/nfs/nfs6'
# ]

mounts = [
    '/home/nfs/nfs1'
]

# mounts = [
#     '/home/nfs1/glusterfs/glusterfs1',
#     '/home/nfs1/glusterfs/glusterfs2',
#     '/home/nfs1/glusterfs/glusterfs3',
#     '/home/nfs1/glusterfs/glusterfs4',
#     '/home/nfs1/glusterfs/glusterfs5',
#     '/home/nfs1/glusterfs/glusterfs6'
# ]

def run_container(path, port, cpu, mount='/tmp', image='mybench'):
    file_dir = '%s/%s' % (path, os.path.basename(path))
    runCmd('mkdir %s' % file_dir)
    output = runCmd('docker run -d -m 1G --cpuset-cpus="%d" -v %s:%s -p %s:%s %s' % (
    cpu, file_dir, mount, port, DEFAULT_PORT, image))
    cid = output[0]
    runCmd('docker cp workloads %s:/usr/local/share/filebench' % cid)
    return cid


def get_container_pids(cid):
    dirs = os.listdir(DOCKER_DIR)
    for dir in dirs:
        if dir.find(cid) == 0:
            c_dir = '%s/%s' % (DOCKER_DIR, dir)
            if os.path.isdir(c_dir):
                return runCmd('cat %s/cgroup.procs' % c_dir)


def filebench(nums, cid, workload, host, port):
    # rpcCall("echo 'run times'>> /usr/local/share/filebench/workloads/%s.f" % workload, host=host, port=port)
    # pid = collect_system(nums, cid, workload)
    output = runCmd('docker exec eb84f4bd9fdf sysdig container.id=%s and proc.name=filebench >  %s.log 2>/dev/null &' % (cid[:12], cid[:12]))
    # pid = output[0].split()[1]
    output = rpcCall('filebench -f /usr/local/share/filebench/workloads/%s.f' % workload, host=host, port=port)
    # runCmd('kill -9 %s' % pid)
    return output


def collect_syscall(cid, test, host, port, workload):
    pid = get_container_pids(cid)
    runCmd('lttng create %s' % cid)
    runCmd('lttng add-context -k -t procname -t pid -t vpid -t tid -t vtid')
    runCmd('lttng enable-event -k --syscall -a')

    for p in pid:
        filter_pid = 'lttng track -k --pid="%s"' % p
        runCmd(filter_pid)
    runCmd('lttng start')
    # time.sleep(10)
    output = test(workload, host=host, port=port)
    runCmd('lttng stop')
    runCmd('lttng destroy')

    dirs = os.listdir(LTTNG_HOME)
    syscalls = []
    for dir in dirs:
        if dir.find(cid) >= 0:
            syscalls = parse_syscall('%s/%s' % (LTTNG_HOME, dir))
            os.removedirs('%s/%s' % (LTTNG_HOME, dir))
    return output, syscalls


def parse_syscall(record_dir):
    record = {}
    output = '/tmp/%s' % str(uuid.uuid4())
    runCmd('babeltrace %s > %s' % (record_dir, output))
    with open(output, 'r') as f:
        for line in f.readlines():
            cols = line.split()
            for col in cols:
                if col.find('syscall') >= 0:
                    call = col.replace(':', '')
                    if call in record.keys():
                        record[call] += 1
                    else:
                        record[call] = 1
    return record


# def benchmark(mount_paths):
#     # start container
#     result = {}
#     containers = {}
#     ports = set()
#     i = 1
#     try:
#         for path in mount_paths:
#             port = random.randint(19000, 20000)
#             while port in ports:
#                 port = random.randint(19000, 20000)
#             ports.add(port)
#             cid = run_container(path, port)
#
#             time.sleep(10)
#
#             containers[cid] = port
#             i += 1
#             result[i] = {}
#             threads = {}
#             for id in containers.keys():
#                 # t = MyThread(collect_syscall, args=(id, filebench, '192.168.137.187', containers[id], 'webserver'))
#                 t = MyThread(filebench, args=('webserver', '192.168.137.187', containers[id]))
#                 t.start()
#                 # output, syscalls = collect_syscall(id, filebench, '192.168.137.187', containers[id], 'webserver')
#                 threads[id] = t
#
#             for id in threads.keys():
#                 threads[id].join()
#
#             for id in threads.keys():
#                 output, syscalls = threads[id].get_result()
#                 result[i][id] = {}
#                 result[i][id]['output'] = output
#                 result[i][id]['syscalls'] = syscalls
#     except Exception:
#         for id in containers.keys():
#             runCmd('docker rm -f %s' % id)
#         pass
#     print(result)

def benchmark(mount_paths, workload):
    # start container
    result = {}
    containers = {}
    ports = set()
    i = 0
    try:
        for path in mount_paths:
            port = random.randint(19000, 20000)
            while port in ports:
                port = random.randint(19000, 20000)
            ports.add(port)
            cid = run_container(path, port, i + 4)
            time.sleep(30)

            containers[cid] = port
            i += 1
            result[i] = {}
            filebench_threads = {}
            for id in containers.keys():
                t = MyThread(filebench, args=(i, id, workload, '133.133.135.22', containers[id]))
                t.start()
                filebench_threads[id] = t

            for id in filebench_threads.keys():
                filebench_threads[id].join()

            for id in filebench_threads.keys():
                output = filebench_threads[id].get_result()
                result[i][id] = {}
                result[i][id]['output'] = output
        for id in containers.keys():
            runCmd('docker rm -f %s' % id)
        for path in mount_paths:
            runCmd('rm -rf %s/%s' % (path, os.path.basename(path)))
        print(result)
        with open(workload, 'w') as f:
            f.write(dumps(result))
    except Exception:
        traceback.print_exc()
        for id in containers.keys():
            runCmd('docker rm -f %s' % id)
        for path in mount_paths:
            runCmd('rm -rf %s/%s' % (path, os.path.basename(path)))
        pass

def syscall(mount_paths, workload):
    # start container
    result = {}
    containers = {}
    ports = set()
    i = 6
    try:
        for path in mount_paths:
            port = random.randint(19000, 20000)
            while port in ports:
                port = random.randint(19000, 20000)
            ports.add(port)
            cid = run_container(path, port, i + 4)
            time.sleep(5)

            containers[cid] = port

        result[i] = {}
        filebench_threads = {}
        for id in containers.keys():
            t = MyThread(filebench, args=(i, id, workload, '133.133.135.22', containers[id]))
            t.start()
            filebench_threads[id] = t

        for id in filebench_threads.keys():
            filebench_threads[id].join()

        for id in filebench_threads.keys():
            output = filebench_threads[id].get_result()
            result[i][id] = {}
            result[i][id]['output'] = output

        for id in containers.keys():
            runCmd('docker rm -f %s' % id)
        for path in mount_paths:
            runCmd('rm -rf %s/%s' % (path, os.path.basename(path)))
        print(result)
        with open(workload, 'w') as f:
            f.write(dumps(result))
    except Exception:
        traceback.print_exc()
        for id in containers.keys():
            runCmd('docker rm -f %s' % id)
        for path in mount_paths:
            runCmd('rm -rf %s/%s' % (path, os.path.basename(path)))
        pass

# workloads = runCmd('ls /root/filebench-1.5-alpha3/workloads')
# print(workloads)
# for wk in workloads:
#     benchmark(mounts, wk.replace('.f', ''))


# workloads = [
#     'fileserver',
#     'webserver',
#     'randomread',
#     'randomwrite',
#     'randomrw',
#     'mongo',
#     'netsfs',
#     'networkfs',
#     'oltp',
#     'openfiles',
#     'tpcso',
#     'videoserver',
#     'webproxy',
#     'varmails',
#     'randomfileaccss'
# ]
workloads = [
    'webproxy'
]
for wk in workloads:
    syscall(mounts, wk)

runCmd('cd /tmp/pycharm_project_533')
runCmd('rm -rf nfs')
runCmd('mkdir nfs')

for wk in workloads:
    runCmd('mv %s nfs/' % wk.replace('.f', ''))
