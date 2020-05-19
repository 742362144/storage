import os
from json import loads, load

from draw import filebench

NFS_LOG_DIR = 'C:\\Users\\coder\\Desktop\\实验结果\\nfs'
GLUSTERFS_LOG_DIR = 'C:\\Users\\coder\\Desktop\\实验结果\\glusterfs'

WORKLOADS = ['fileserver', 'webserver', 'randomread', 'randomwrite', 'randomrw']


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
    


for workload in WORKLOADS:
    nfs = parse_filebench_result('%s/%s' % (NFS_LOG_DIR, workload))
    glusterfs = parse_filebench_result('%s/%s' % (GLUSTERFS_LOG_DIR, workload))
    y = []
    for key in nfs.keys():
        one = []
        sum = 0
        for i in range(len(glusterfs[key]['ops_ps'])):
            sum += glusterfs[key]['ops_ps'][i]
        one.append(sum / len(glusterfs[key]['ops_ps']))
        # for i in range(len(glusterfs[key]['speed'])):
        #     one.append(glusterfs[key]['speed'][i])
        y.append(one)

    x = list(range(1, 6))
    print(x)
    print(y)
    filebench(workload, x, y)