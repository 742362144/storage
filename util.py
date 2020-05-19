import subprocess
import socket
import threading
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

def collect_system_io():
    pass

def collect_system_net():
    pass



if __name__ == '__main__':
    print(get_IP())
    # print(dumps(runCmd('ls /')))
