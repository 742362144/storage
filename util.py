import os
import subprocess
import socket
import threading
import time
from json import dumps


def runCmd(cmd):
    if not cmd:
        #         logger.debug('No CMD to execute.')
        return
    print(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        std_out = p.stdout.readlines()
        std_err = p.stderr.readlines()
        if std_out:
            result = []
            for line in std_out:
                result.append(line.decode("utf-8").strip())
            print(result)
            return result
    finally:
        p.stdout.close()
        p.stderr.close()


class MyThread(threading.Thread):

    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None


def get_IP():
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myaddr

def collect_system(nums, cid, workload):
    cmd = 'curl --unix-socket /var/run/docker.sock http://localhost/containers/%s/stats > %s_%d_%s.txt 2>/dev/null &' % (cid, workload, nums, cid)
    runCmd(cmd)
    output = runCmd('ps -ef | grep curl | grep %s' % cid)
    pid = output[0].split()[1]

    return pid


if __name__ == '__main__':
    print(collect_system('ab789404daa7', 'res'))
    # print(dumps(runCmd('ls /')))
