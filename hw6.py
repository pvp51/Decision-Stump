import sys
from sys import argv
import random
import math

################
##  py hw6.py datafile trainlabelfile
################

################
##best Split
###############

def bestsplit(data, labels, col):
    colvals = {}
    indices = []
    rows = 0
    minus = 0
    for i in range(0, len(data), 1):
        if(labels.get(i) != None):
            colvals[i] = data[i][col]
            indices.append(i)
            rows += 1
            if(labels[i] == 0):
                minus += 1

    sorted_indices = sorted(indices, key=colvals.__getitem__)

    lsize = 1
    rsize = rows - 1
    lp = 0
    rp = minus
    if(labels[sorted_indices[0]] == 0):
        lp += 1
        rp -= 1

    best_s = -1
    bestgini = 10000
    for i in range(1, len(sorted_indices), 1):
        s = (colvals[sorted_indices[i]] + colvals[sorted_indices[i-1]])/2
        gini = (lsize/rows)*(lp/lsize)*(1 - lp/lsize) + (rsize/rows)*(rp/rsize)*(1 - rp/rsize);
        if(gini < bestgini):
            bestgini = gini
            best_s = s
        if(labels[sorted_indices[i]] == 0):
            lp += 1
            rp -= 1
        lsize += 1
        rsize -= 1

    return(best_s, bestgini)


################
##Read Data
################
f = open(argv[1])
data = []
l = f.readline()
while (l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()
rows = len(data)
cols = len(data[0])
f.close()

################
##Read Train Labels
###############
trainlabels = {}
f = open(argv[2])
l = f.readline()
while (l != ''):
    a = l.split()
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
f.close()

################
##Main
###############

best_split = -1
best_col =1
best_gini = 100000
for j in range(0, cols, 1):
    [s,gini] = bestsplit(data, trainlabels, j)
    print(s, gini)
    if(gini < best_gini):
        best_gini = gini
        best_split = s
        best_col = j

m=0
p=0
for i in range(0, rows, 1):
    if(trainlabels.get(i) != None):
        if(data[i][best_col] < best_split):
            if(trainlabels[i] == 0):
                m += 1
            else:
                p += 1
if(m > p):
    left=0
    right=1
else:
    left=1
    right=0

print(best_gini, best_split, best_col)

################
##Classify unlabeled points
###############
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        if(data[i][best_col] < best_split):
            print(left, i)
        else:
            print(right,i)
