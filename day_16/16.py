file_path = 'data_16.txt'
#file_path='sample_16.txt'
e=[]
from collections import defaultdict,deque
import heapq
import re
with open(file_path, "r") as file:
    data = file.readlines()
    for line in data :
        line = line.strip()
        e.append(list(line))

R=len(e)
C = len(e[0])
for r in range(R):
    for c in range(C):
        if e[r][c]=='S':
            start = (r,c)
            break
ans_1=0
x,y=start
heap = [(0,x,y,0,1)]
visited = set((x,y,0,1))
while heap:
    c,x,y,dx,dy =  heapq.heappop(heap)
    visited.add((x,y,dx,dy))
    if e[x][y] == 'E':
        ans_1 = c
        break
    for nc,nx,ny,mx,my in [(c+1,x+dx,y+dy,dx,dy),(c+1000,x,y,dy,-dx),(c+1000,x,y,-dy,dx)]:
        if e[nx][ny]=='#':
            continue
        if (nx,ny,mx,my) in visited:
            continue
        heapq.heappush(heap,(nc,nx,ny,mx,my))

print(ans_1)
bc=float('inf')
x,y=start
heap=[(0,x,y,0,1,None,None,None,None)]
bt = {}
visit = {(x,y,0,1):0}
fin = set()
while heap:
    c,x,y,dx,dy,lx,ly,ldx,ldy = heapq.heappop(heap)
    if c>visit.get((x,y,dx,dy),float('inf')):
        continue
    visit[(x,y,dx,dy)]=c
    if e[x][y]=='E':
        if c>bc:
            break
        bc = c
        fin.add((x,y,dx,dy))
    if (x,y,dx,dy) not in bt:
        bt[(x,y,dx,dy)]= set()
    bt[(x,y,dx,dy)].add((lx,ly,ldx,ldy))
    for nc,nx,ny,mx,my in [(c+1,x+dx,y+dy,dx,dy),(c+1000,x,y,dy,-dx),(c+1000,x,y,-dy,dx)]:
        if e[nx][ny]=='#':
            continue
        if nc>visit.get((nx,ny,mx,my),float('inf')):
            continue
        heapq.heappush(heap,(nc,nx,ny,mx,my,x,y,dx,dy))

q = deque(fin)
seen = set(fin)
while q:
    k = q.popleft()
    for i in bt.get(k,[]):
        if i in seen:
            continue
        seen.add(i)
        q.append(i)
tiles = {(i,j) for i,j,n_,m_ in seen if i!=None and j!=None}
print(len(tiles))

