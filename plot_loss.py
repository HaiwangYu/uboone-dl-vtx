import matplotlib.pyplot as plt
import numpy as np

inputs   = [
    # 'backup/point-based/test-m16-l4-lr0.0001-0.00001-adam-t4000v1000-e77/loss.txt',
    # 'm16-l4-q-avg-t200/loss.csv',
    'checkpoints/loss.csv',
    ]
in_labels = [
    # 'ref',
    'test'
    ]
col_labels = [
    'epoch', # 0
    'tloss', # 1
    'vloss', 
    'thit',  # 3
    'vhit',
    'teff',  # 5
    'veff',
    'tpur',  # 7
    'vpur',
    ]
col_symbol = [
    '',
    '-',
    '--',
    '-',
    '--',
    '-o',
    '--o',
    '-^',
    '--^',
    ]

fontsize = 18
    
ax = plt.subplot(121)
ax.set_title('loss')
for input, in_lable in zip(inputs, in_labels) :
    data = np.genfromtxt(input, delimiter=',')
    for icol in [1, 2] :
        plt.plot(data[:,0], data[:,icol], col_symbol[icol], label='{}:{}'.format(in_lable, col_labels[icol]))
plt.legend(loc='best',fontsize=fontsize)
plt.grid()
plt.xlabel("Epoch", fontsize=fontsize)
plt.ylabel("Mean Loss", fontsize=fontsize)
    
ax = plt.subplot(122)
ax.set_title('hit rate')
for input, in_lable in zip(inputs, in_labels) :
    data = np.genfromtxt(input, delimiter=',')
    for icol in range(3, 9) :
        plt.plot(data[:,0], data[:,icol], col_symbol[icol], label='{}:{}'.format(in_lable, col_labels[icol]))
# plt.legend(loc='best',fontsize=fontsize)
plt.grid()
plt.ylim(0,1)
plt.xlabel("Epoch", fontsize=fontsize)
plt.ylabel("Hit rate", fontsize=fontsize)

plt.show()