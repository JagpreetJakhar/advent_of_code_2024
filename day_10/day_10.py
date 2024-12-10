file_path = 'data_10.txt'
#file_path='sample_10.txt'
e=[]
from collections import defaultdict,deque
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.readlines()
    for line in data :
        line = line.strip()
        e.append([int(x) for x in list(line)])
ans_1=0
starts=[]
rows = len(e)
cols = len(e[0])
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
for r in range(rows):
    for c in range(cols):
        if e[r][c]==0:
            starts.append((r,c))
def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited=set()
    nines=set()
    while q:
        x,y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for d in dirs:
            dx,dy = d
            nx,ny = x+dx,y+dy
            if (0<=nx<rows and 0<=ny<cols)and (nx,ny) not in visited:
                if e[nx][ny] - e[x][y] == 1:
                    if e[nx][ny]==9 and (nx,ny) not in nines:
                        nines.add((nx,ny))
                    else:
                        q.append((nx,ny))
            
    return len(nines)

cnt=0
for coord in starts:
    s,end=coord
    cnt=0
    cnt = bfs(s,end)
    ans_1+=cnt
print(ans_1)

ans_2=0
def dfs(a,b,look):
    if not (0<=a<rows and 0<=b<cols):
        return 0
    if (a,b) in look:
        return look[(a,b)]
    if e[a][b]==9:
        return 1
    tmp=0
    for dx,dy in dirs:
        nx,ny = a+dx,b+dy
        if (0<=nx<rows and 0<=ny<cols) and e[nx][ny] - e[a][b]==1:
            tmp+=dfs(nx,ny,look)
    look[(a,b)]=tmp
    return tmp
look={}
for start in starts:
    ans_2+=dfs(start[0],start[1],look)
print(ans_2)
