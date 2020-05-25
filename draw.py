import numpy as np
import matplotlib.pyplot as plt

def average(workload, x, y):
    # 开始画图
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    fig = plt.figure()  # Creates a new figure
    fig.set_size_inches(12, 9)
    # 开始绘制
    ax = fig.add_subplot(111)  # add a subplot to the new figure, 111 means "1x1 grid, first subplot"
    fig.subplots_adjust(
        top=0.80)  # adjust the placing of subplot, adjust top, bottom, left and right spacing

    total_width, n = 0.8, 4
    width = 0.5

    colors = ['y', 'r', 'b', 'g', 'k', 'k']

    # ax.bar(x, np.zeros(5), width=width, label='a', tick_label=x)

    for i in range(len(y)):
        x = []
        for j in range(len(y[i])):
            x.append(i + 1 - (0.1 * len(y[i]) + 0.2 * (len(y[i]) - 1)) / 4 + j * 0.2)
        ax.bar(x, y[i], width=width, label=str(i + 1), fc=colors[i])
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # ax.bar(x, y[2], width=width, label='c', fc='b')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # ax.bar(x, y[3], width=width, label='d', fc='g')
    # for i in range(len(x)):
    #     x[i] = x[i] + width
    # ax.bar(x, y[4], width=width, label='d', fc='k')

    ax.set_xlabel(u'Number of containers to run %s at the same time' % workload, fontsize=28, weight='heavy')
    ax.set_ylabel(u'Average Throughput(ops/s)', fontsize=28, weight='heavy')

    # 设置坐标刻度值的大小以及刻度值的字体
    ax.tick_params(labelsize=23)
    labels = ax.get_xticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    labels = ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]

    # ax.legend(fontsize='20')
    # 保存图片
    fig.savefig('%s.png' % workload, dpi=300)
    plt.clf()

def filebench(workload, x, y):
    # 开始画图
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    fig = plt.figure()  # Creates a new figure
    fig.set_size_inches(12, 9)
    # 开始绘制
    ax = fig.add_subplot(111)  # add a subplot to the new figure, 111 means "1x1 grid, first subplot"
    fig.subplots_adjust(
        top=0.80)  # adjust the placing of subplot, adjust top, bottom, left and right spacing

    total_width, n = 0.8, 4
    width = 0.15

    colors = ['g', 'purple', 'b', 'k', 'y', 'r']

    # ax.bar(x, np.zeros(5), width=width, label='a', tick_label=x)

    for i in range(len(y)):
        x = []
        for j in range(len(y[i])):
            x.append(i + 1 - (0.1 * len(y[i]) + 0.2 * (len(y[i]) - 1)) / 4 + j * 0.2)
        ax.bar(x, y[i], width=width, label=str(i + 1), fc=colors[i])


    ax.set_xlabel('Run %s Container Numbers' % workload, fontsize=28, weight='heavy')
    ax.set_ylabel(u'Average Throughput(ops/s)', fontsize=28, weight='heavy')

    # 设置坐标刻度值的大小以及刻度值的字体
    ax.tick_params(labelsize=23)
    labels = ax.get_xticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    labels = ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]

    # ax.legend(fontsize='20')
    # 保存图片
    fig.savefig('%s.png' % workload, dpi=300)
    plt.clf()


def draw_var(data):
    print(data)
    # 开始画图
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    fig = plt.figure()  # Creates a new figure
    fig.set_size_inches(12, 9)
    # 开始绘制
    ax = fig.add_subplot(111)  # add a subplot to the new figure, 111 means "1x1 grid, first subplot"
    fig.subplots_adjust(
        top=0.80)  # adjust the placing of subplot, adjust top, bottom, left and right spacing

    total_width, n = 0.8, 4
    width = 0.1

    markers = ['.', ',', 'o', 'v', '^', 'v', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*']
    colors = ['y', 'r', 'b', 'g', 'k', 'c']

    # ax.bar(x, np.zeros(5), width=width, label='a', tick_label=x)

    i = 0
    for key in data.keys():
        if len(data[key]) == 0:
            continue
        ax.plot(range(1, len(data[key]) + 1), data[key], label=key, marker=markers[i])
        i += 1

    ax.set_xlabel(u'Container Numbers', fontsize=28, weight='heavy')
    ax.set_ylabel(u'Performance Difference(Var)', fontsize=28, weight='heavy')

    # 设置坐标刻度值的大小以及刻度值的字体
    ax.tick_params(labelsize=23)
    labels = ax.get_xticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    labels = ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]

    ax.legend(fontsize='18', bbox_to_anchor=(1.06, 1.25),ncol=4)
    # 保存图片
    fig.savefig('%s.png' % 'var', dpi=300)
    plt.clf()

def draw_I(data):
    print(data)
    # 开始画图
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    fig = plt.figure()  # Creates a new figure
    fig.set_size_inches(12, 9)
    # 开始绘制
    ax = fig.add_subplot(111)  # add a subplot to the new figure, 111 means "1x1 grid, first subplot"
    fig.subplots_adjust(
        top=0.80)  # adjust the placing of subplot, adjust top, bottom, left and right spacing

    total_width, n = 0.8, 4
    width = 0.1

    markers = ['.', ',', 'o', 'v', '^', 'v', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*']
    colors = ['y', 'r', 'b', 'g', 'k', 'c']

    # ax.bar(x, np.zeros(5), width=width, label='a', tick_label=x)

    i = 0
    for key in data.keys():
        if len(data[key]) == 0:
            continue
        ax.plot(range(1, len(data[key]) + 1), data[key], label=key, marker=markers[i])
        i += 1

    ax.set_xlabel(u'Container Numbers', fontsize=28, weight='heavy')
    ax.set_ylabel(u'Interference(I)', fontsize=28, weight='heavy')

    # 设置坐标刻度值的大小以及刻度值的字体
    ax.tick_params(labelsize=23)
    labels = ax.get_xticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    labels = ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]

    ax.legend(fontsize='18', bbox_to_anchor=(1, 1.15),ncol=4)
    # 保存图片
    fig.savefig('%s.png' % 'I', dpi=300)
    plt.clf()