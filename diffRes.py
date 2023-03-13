import os
import matplotlib.pyplot as plt


def printRes(output_dir):
    '''
    A function for printing result image names
    '''
    org = os.getcwd()
    os.chdir(output_dir)
    tmp = os.listdir()
    res = []
    for i in sorted(tmp):
        if ('.jpg' in i) or ('.jpeg' in i) or ('.png' in i) or ('.tif' in i):
            print(i)
            res.append(i)
    os.chdir(org)
    return res


def diffRes(output_dir, img, cut, Ver, figname='',
            fontsize=20, fontfamily='Times New Roman'):
    '''
    A function for comparing results of computer vision models
    '''
    plt.rcParams['font.size'] = fontsize
    plt.rcParams['font.family'] = fontfamily
    if 4 < len(Ver) or len(Ver) <= 1:
        return
    else:
        fig = plt.figure(figsize=(15, 15))
        fig.set_facecolor('white')
        for i, j in enumerate(Ver):
            if len(Ver) == 2:
                plt.subplot(1,2,i+1)
            else:
                plt.subplot(2,2,i+1)
            tmp = plt.imread(output_dir + '/' + j + '/' + img)
            if cut == []:
                plt.imshow(tmp)
            else:
                plt.imshow(tmp[cut[0]:cut[0]+cut[2],cut[1]:cut[1]+cut[3],:])
            plt.title(j)
            plt.axis('off')
        if figname != '':
            plt.savefig(figname + '.png', dpi=300, bbox_inches='tight', pad_inches=0.3, transparent=False)