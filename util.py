import subprocess


def runCmd(cmd):
    if not cmd:
        #         logger.debug('No CMD to execute.')
        return
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        std_out = p.stdout.readlines()
        std_err = p.stderr.readlines()
        if std_out:
            return std_out

    finally:
        p.stdout.close()
        p.stderr.close()

def get_IP():
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myaddr