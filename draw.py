import numpy as np
import matplotlib.pyplot as plt



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
    width = 0.1

    colors = ['y', 'r', 'b', 'g', 'k']

    ax.bar(x, np.zeros(5), width=width, label='a', tick_label=x)

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

    ax.set_xlabel(u'同时运行%s的容器数量' % workload, fontsize=23)
    ax.set_ylabel(u'平均吞吐量(ops/s)', fontsize=23)

    # 设置坐标刻度值的大小以及刻度值的字体
    ax.tick_params(labelsize=23)
    labels = ax.get_xticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    labels = ax.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]

    ax.legend()
    # 保存图片
    fig.savefig('%s.png' % workload, dpi=300)
    plt.clf()