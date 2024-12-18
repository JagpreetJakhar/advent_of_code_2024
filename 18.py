file_path = 'data_18.txt'
#file_path='sample_18.txt'
e=[]
from collections import defaultdict,deque
import heapq
import re
from itertools import count
with open(file_path, "r") as file:
    data = file.readlines()
    for line in data :
        line = line.strip()
        e.append([int(x) for x in line.split(",")])
R = 71
C = 71
grid = [['.' for _ in range(C)] for _ in range(R)]
for i,j in e[:1024]:
    grid[j][i]='#'
ans_1=0
start = (0,0)
tgt = (70,70)
dirs = [(1,0),(-1,0),(0,-1),(0,1)]
heap = []
visited = set()
q = deque()
q.append((0,0,0))
while q:
    x,y,steps = q.popleft()
    if (x,y)==tgt:
        ans_1=steps
        break
    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
       
        if  (0<=nx<R and 0<=ny<C) and (nx,ny) not in visited and grid[nx][ny]!='#':
        
            visited.add((nx,ny))
            q.append((nx,ny,steps+1))
        else:
            continue
print(ans_1)
grid = [['.' for _ in range(C)] for _ in range(R)]
ans_2=0
for i,j in e:
    grid[j][i]='#'
    flag = False
    start = (0,0)
    tgt = (70,70)
    dirs = [(1,0),(-1,0),(0,-1),(0,1)]
    visited = set()
    q = deque()
    q.append((0,0,0))
    while q:
        x,y,steps = q.popleft()
        if (x,y)==tgt:
            flag=True
            break
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
           
            if  (0<=nx<R and 0<=ny<C) and (nx,ny) not in visited and grid[nx][ny]!='#':
            
                visited.add((nx,ny))
                q.append((nx,ny,steps+1))
            else:
                continue
    if not flag:
        print(i,j)
        break
    
