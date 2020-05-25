import math
import os
from json import loads, load

from draw import filebench, draw_var, draw_I

NFS_LOG_DIR = 'C:\\Users\\coder\\Desktop\\实验结果\\nfs'
GLUSTERFS_LOG_DIR = 'C:\\Users\\coder\\Desktop\\实验结果\\glusterfs'

WORKLOADS = [
    'fileserver',
    'webserver',
    'randomread',
    'randomwrite',
    'randomrw',
    'mongo',
    'netsfs',
    'networkfs',
    'oltp',
    'openfiles',
    'tpcso',
    'videoserver',
    'webproxy',
    'varmails',
    'randomfileaccss'
]


def parse_filebench_result(log_file):
    print(os.path.basename(log_file))
    result = {}
    with open(log_file, 'r') as f:
        data = load(f)
        for num in data.keys():
            result[num] = {}
            result[num]['ops_ps'] = []
            result[num]['speed'] = []

            cids = data[num]
            for cid in cids.keys():
                # print(cids[cid]['output'])
                for line in cids[cid]['output'].split(','):
                    if line.find('IO Summary') >= 0:
                        split_line = line.replace('"', '').split(':')[-1].split()
                        ops_ps = int(float(split_line[2]))
                        r_to_w = split_line[4]
                        speed = int(float(split_line[6].replace('mb/s', '')))
                        # opt = split_line[7]
                        result[num]['ops_ps'].append(ops_ps)
                        result[num]['speed'].append(speed)
        # print(result)
    return result


def parse_container_useage(filename):
    print(filename)
    with open(filename, 'r') as f:
        for line in f.readlines():
            try:
                info = loads(line)
                print(info)
            except:
                pass


# draw every time result
def draw1():
    for workload in WORKLOADS:
        # nfs = parse_filebench_result('%s/%s' % (NFS_LOG_DIR, workload))
        glusterfs = parse_filebench_result('%s/%s' % (GLUSTERFS_LOG_DIR, workload))
        y = []
        for key in glusterfs.keys():
            one = []
            for i in range(len(glusterfs[key]['ops_ps'])):
                print(glusterfs[key])
                one.append(glusterfs[key]['ops_ps'][i])
            # sum = 0
            # for i in range(len(nfs[key]['ops_ps'])):
            #     sum += nfs[key]['ops_ps'][i]
            # one.append(sum / len(nfs[key]['ops_ps']))
            # for i in range(len(glusterfs[key]['speed'])):
            #     one.append(glusterfs[key]['speed'][i])
            print(one)
            y.append(one)

        x = list(range(1, 6))
        print(x)
        print(y)
        filebench(workload, x, y)


def draw2():
    y = {}
    for workload in WORKLOADS:
        try:
            nfs = parse_filebench_result('%s/%s' % (NFS_LOG_DIR, workload))
        except:
            continue
        # glusterfs = parse_filebench_result('%s/%s' % (GLUSTERFS_LOG_DIR, workload))
        one = []
        for key in nfs.keys():
            if len(nfs[key]['ops_ps']) <= 0:
                continue

            sum = 0
            for i in range(len(nfs[key]['ops_ps'])):
                sum += nfs[key]['ops_ps'][i]

            aver = sum / len(nfs[key]['ops_ps'])
            var = 0
            for i in range(len(nfs[key]['ops_ps'])):
                var += (nfs[key]['ops_ps'][i] - aver) * (nfs[key]['ops_ps'][i] - aver)

            var /= len(nfs[key]['ops_ps'])
            one.append(math.sqrt(var))
        y[workload] = one

    x = list(range(1, 6))
    draw_var(y)


def draw3():
    y = {}
    for workload in WORKLOADS:
        try:
            # nfs = parse_filebench_result('%s/%s' % (NFS_LOG_DIR, workload))
            glusterfs = parse_filebench_result('%s/%s' % (GLUSTERFS_LOG_DIR, workload))
        except:
            continue
        one = []
        for key in glusterfs.keys():
            if len(glusterfs[key]['ops_ps']) <= 0:
                continue
            sum = 0
            for i in range(len(glusterfs[key]['ops_ps'])):
                sum += (glusterfs[key]['ops_ps'][i] - glusterfs[key]['ops_ps'][0]) / glusterfs[key]['ops_ps'][0]
            one.append(sum / len(glusterfs[key]['ops_ps']))
        y[workload] = one

    x = list(range(1, 6))
    draw_I(y)

def draw_glusterfs_var():
    data = {'fileserver': [0.0, 65.0, 348.7084105030384, 291.77259981019466, 372.569456611784, 575.3511970961736],
            'webserver': [0.0, 6.5, 11.841546445554409, 45.37827123194536, 68.80813905345791, 63.86117756509036],
            'randomread': [0.0, 163.5, 276.7959537276512, 361.90433818897503, 428.97944006677056, 431.8154183856287],
            'randomwrite': [0.0, 372.5, 1657.7189146535065, 2327.2230769739285, 2303.993802074997, 2856.44322346671],
            'randomrw': [0.0, 1368.5, 2333.2167113712826, 2698.3259972620062, 2950.426342073294, 2343.557178734925],
            'mongo': [0.0, 62.5, 0.0, 83.5, 0.0, 64.42480543669151], 'netsfs': [], 'networkfs': [], 'oltp': [],
            'openfiles': [0, 1208.5, 864.1104610458601, 791.7382774629505, 1262.1807477536645, 923.4857274960392],
            'tpcso': [], 'videoserver': [],
            'webproxy': [0.0, 60.0, 68.90250761442253, 251.28905169147342, 450.17978630764844, 327.4112687261831],
            'varmails': [], 'randomfileaccss': []}
    draw_var(data)
def draw_nfs_var():
    data = {'fileserver': [0.0, 9.0, 106.302503367617, 125.86699329053666, 101.4561974450058, 108.99184475098227],
            'webserver': [],
            'randomread': [0.0, 789.5, 825.4131625367315, 741.9236399387743, 680.2119081580387, 622.7004139677085],
            'randomwrite': [0.0, 307.0, 409.9401040260503, 489.98539519050973, 208.86742206481125, 773.2528693771527],
            'randomrw': [0.0, 455.5, 180.68942046137252, 451.0789149361783, 652.6412797241683, 396.36196280111886],
            'mongo': [0.0, 31.5, 20.270394394014364, 16.887495373796554, 16.049922118191105, 12.641422212534298],
            'netsfs': [],
            'networkfs': [], 'oltp': [],
            'openfiles': [0.0, 389.5, 8266.318420084132, 8283.247038450561, 11098.832435891623, 14087.02452219378],
            'tpcso': [], 'videoserver': [], 'webproxy': [], 'varmails': [], 'randomfileaccss': []}
    draw_var(data)


# draw1()

def draw_container(workload):
    for file in os.listdir(GLUSTERFS_LOG_DIR):
        if file.find(workload) >= 0 and file.find('txt') >= 0:
            parse_container_useage('%s/%s' % (GLUSTERFS_LOG_DIR, file))


# draw_container('randomwrite')
draw_nfs_var()
draw3()
