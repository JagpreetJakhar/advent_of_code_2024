file_path = 'data_20.txt'
#file_path='sample_20.txt'
grid=[]

from collections import defaultdict,deque
import heapq
import re
from itertools import count
with open(file_path, "r") as file:
    data = file.readlines()
    for line in data:
        line = line.strip()
        grid.append(list(line))
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
R = len(grid)
C = len(grid[0])
start=tgt=None
for r in range(R):
    if start and tgt:
        break
    for c in range(C):
        if grid[r][c]=='S':
            start = (r,c)
            grid[r][c]='.'
        if grid[r][c]=='E':
            tgt = (r,c)
            grid[r][c]='.'
prob_paths=set()
def traverse(start,end,flag=False):
    q = deque()
    q.append(start)
    visited=defaultdict(int)
    visited[start]=0
    while q:
        x,y = q.popleft()
        if (x,y)==end:
            return visited[(x,y)],visited
        for dx,dy in dirs:
            nx,ny = x+dx,y+dy
            if 0<=nx<R and 0<=ny<C and (nx,ny) not in visited:
                if grid[nx][ny]=='#':
                    if flag:
                        prob_paths.add((nx,ny))
                    continue
                q.append((nx,ny))
                visited[(nx,ny)]=visited[(x,y)]+1
init_time,dists = traverse(start,tgt,True)
print(init_time)
save=100
ans_1=set()
for mx,my in list(prob_paths):
    grid[mx][my]='.'
    tr2,_ = traverse(start,tgt)
    grid[mx][my]='#'
    if init_time - tr2 >=save:
        ans_1.add((mx,my))

print(len(ans_1)) #1450

ans_2=0
for x in range(R):
    for y in range(C):
        if grid[x][y]=='#':continue
        for ch  in range(2,21):
            for dx in range(ch+1):
                dy = ch-dx
                for nx,ny in {(x+dx,y+dy),(x+dx,y-dy),(x-dx,y+dy),(x-dx,y-dy)}:
                    if 0<=nx<R and 0<=ny<C:
                        if grid[nx][ny]=='#':
                            continue
                        if dists[(x,y)]-dists[(nx,ny)]>=100+ch:
                            ans_2+=1
print(ans_2)



