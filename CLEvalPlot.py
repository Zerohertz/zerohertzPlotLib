import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def CLEvalPlot(time_dir, figname='', fontsize=20, fontfamily='Times New Roman',
               yl=[95, 97.5]):
    '''
    Visualization of HMean, Precision, Recall calculated through CLEval (https://github.com/clovaai/CLEval)
    and processing time calculated through zerohertzPlotLib.meanProcessingTime()
    '''
    plt.rcParams['font.size'] = fontsize
    plt.rcParams['font.family'] = fontfamily
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
    print('='*20)
    for i, j in enumerate(opt):
        print(i, j)
    print('='*20)
    x = input()
    if ',' in x:
        for i in list(map(int, x.split(','))):
            if '-----' in opt[i]:
                os.chdir(org)
                return
            else:
                tmp.append(Ver.index(opt[i]))
                opt[i] += '\t-----X'
                cnt -= 1
    else:
        os.chdir(org)
        return
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
    plt.xlim([-N/2, 4*(N - 1) + N/2])
    plt.ylabel('[%]')
    plt.ylim(yl)
    plt.legend(loc='upper right', bbox_to_anchor=(1.21, 1.02))
    plt.subplot(2,1,2)
    plt.grid(True)
    plt.bar(idx, Time[5], label='Total\nprocessing\ntime', color='olive', zorder=10)
    plt.xticks(idx, Ver, rotation=0)
    plt.xlim([-N/2, 4*(N - 1) + N/2])
    plt.ylim([0, 170])
    plt.ylabel('Time [ms]')
    plt.legend(loc='upper right', bbox_to_anchor=(1.21, 1.02))
    os.chdir(org)
    MetName = ['HMean', 'Precision', 'Recall']
    for i in range(3):
        print('='*20, '\t', MetName[i], '\t', '='*20)
        print(Ver[0], ': ', Met[i][0], '[%]')
        print(Ver[-1], ': ', Met[i][-1], '[%]')
        print(Met[i][-1] - Met[i][0], '[%p]')
        print((Met[i][-1] - Met[i][0]) / Met[i][0] * 100, '[%]')
    print('='*20, '\tTime\t', '='*20)
    print(Ver[0], ': ', Time[5][0], '[ms]')
    print(Ver[-1], ': ', Time[5][-1], '[ms]')
    print(Time[5][-1] - Time[5][0], '[ms]')
    print((Time[5][-1] - Time[5][0]) / Time[5][0] * 100, '[%]')
    print('='*20, '\tEnd\t', '='*20)
    if figname != '':
        print("Saving...")
        plt.savefig(figname + '.png', dpi=300, bbox_inches='tight', pad_inches=0.3, transparent=False)