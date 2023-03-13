import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
Visualization of HMean, Precision, Recall calculated through CLEval (https://github.com/clovaai/CLEval)
and processing time calculated through zerohertzPlotLib.meanProcessingTime()
'''

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20

def CLEvalPlot(time_dir, figname=''):
    org = os.getcwd()
    os.chdir(time_dir)
    data = pd.read_csv('./time.csv', header=None)
    K = data[0][:]
    N = len(K)
    Ver = ['' for _ in range(N)]
    Time = [[0 for _ in range(N)] for _ in range(6)]
    met = {}
    Met = [[0 for _ in range(N)] for _ in range(3)]
    for i in range(N):
        Ver[i] = K[i]
        for j in range(6):
            Time[j][i] = data[j+1][i]
    cnt = 0
    for i in range(N):
        try:
            data = pd.read_csv('../evaluation/' + Ver[i] + '.csv', header=None)        
            for j in range(3):
                Met[j][i] = data[j+1][0]
            cnt += 1
        except:
            Ver[i] += '\t-----X'
            continue
    tmp = []
    opt = []
    for v in Ver:
        opt.append(v)
    while True:
        print('='*20)
        for i, j in enumerate(opt):
            print(i, j)
        print('='*20)
        if cnt <= 0:
            break
        x = input()
        if x == '':
            break
        else:
            x = int(x)
            tmp.append(Ver.index(opt[x]))
            opt[x] += '\t-----X'
            cnt -= 1
    print("Plotting...")
    N = len(tmp)
    Met, Time = np.array(Met), np.array(Time)
    Ver, Met, Time = [Ver[i] for i in tmp], Met[:,tmp], Time[:,tmp]
    idx = np.arange(N) * 4 # 0 ~ 4X(N-1)
    bar_width = 1
    fig = plt.figure(figsize=(15, 10))
    plt.subplot(2,1,1)
    plt.grid(True)
    fig.set_facecolor('white')
    plt.bar(idx - bar_width, Met[0], bar_width, label='HMean', color='black', zorder=10)
    plt.bar(idx, Met[1], bar_width, label='Precision', color='red', zorder=10)
    plt.bar(idx + bar_width, Met[2], bar_width, label='Recall', color='blue', zorder=10)
    plt.xticks(idx, Ver, rotation=0)
    plt.xlim([-N, 4*(N - 1) + N])
    plt.ylabel('[%]')
    plt.ylim([95, 97.25])
    plt.legend(loc='upper right', bbox_to_anchor=(1.21, 1.02))
    plt.subplot(2,1,2)
    plt.grid(True)
    plt.bar(idx, Time[5], label='Total\nprocessing\ntime', color='olive', zorder=10)
    plt.xticks(idx, Ver, rotation=0)
    plt.xlim([-N, 4*(N - 1) + N])
    plt.ylim([0, 170])
    plt.ylabel('Time [ms]')
    plt.legend(loc='upper right', bbox_to_anchor=(1.21, 1.02))
    os.chdir(org)
    if figname != '':
        print("Saving...")
        plt.savefig(figname + '.png', dpi=300, bbox_inches='tight', pad_inches=0.3, transparent=False)