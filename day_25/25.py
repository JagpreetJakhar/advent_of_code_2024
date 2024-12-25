from collections import defaultdict,deque
import heapq
import re
from itertools import count,product,combinations
from functools import cache
file_path = 'data_25.txt'
#file_path='sample_25.txt'
grids=[]
with open(file_path, "r") as file:
    data=file.read()
for schema in data.split('\n\n'):
    g = schema.strip().split()
    grid = [list(line) for line in g]
    grids.append(grid)
locks = []
keys=[]
for grid in grids:
    if all(cell == '#' for cell in grid[0]):
        locks.append(grid)
    else:
        keys.append(grid)
#    for lock in locks:
#        for l in lock:
#            print(l)
#        print('$$$$$$$')
#    for key in keys:
#        for k in key:
#            print(k)
#        print('^^^^^^^^^^')
R=len(locks[0])
C = len(locks[0][0])
lstart=(0,0)
kstart=(R-1,0)
hlocks=[]
hkeys=[]
for lock in locks:
    h = 0
    hts=[]
    for c in range(C):
        for r in range(R):
            if lock[r][c]!='#':
                break
            else:
                h = r
        hts.append(h)
    hlocks.append(hts)
for key in keys:
    h=0
    hts=[]
    for c in range(C):
        for r in range(R-1,-1,-1):
            if key[r][c]!='#':
                break
            else:
                h=R-1-r
        hts.append(h)
    hkeys.append(hts)
ans_1=0
for lock in hlocks:
    for key in hkeys:
        flag=True
        for x,y in zip(lock,key):
            if x+y<R-1:
                continue
            else:
                flag=False
        if flag:
            ans_1+=1

                
print(ans_1)
        
        


