import numpy as np
import os
import time

p = 0

for i in range(40):
    if i % 2 == 0:
        p=69
        pp=88
        tree = np.ones((21, 21), dtype="int")
    else:
        p=1
        pp=1
        tree = np.zeros((21, 21), dtype="int")
        tree = tree+69

    tree[2,10] = p
    tree[3,9:12] = p
    tree[4,8:13] = p
    tree[5,7:14] = p
    tree[6,6:15] = p
    tree[7,8:13] = p
    tree[8,7:14] = p
    tree[9,6:15] = p
    tree[10,8:13] = p
    tree[11,7:14] = p
    tree[12,6:15] = p
    tree[13,9:12] = p
    tree[14,9:12] = p
    tree[15,9:12] = p
    tree[16,9:12] = p
    tree[17,:] = p
    tree[18,:] = p
    tree[19,:] = p
    tree[20,:] = p

    tree[16,-2:] = p
    tree[16,:2] = p
    tree[16,5:7] = p
    tree[16,-7:-5] = p

    print(tree)
    time.sleep(.7)
    os.system("clear")