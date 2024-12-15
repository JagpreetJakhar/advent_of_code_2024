file_path = 'data_15.txt'
#file_path='sample_15.txt'
e=[]
from collections import defaultdict,deque
import re
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.read().split("\n\n")
    g = [list(line) for line in data[0].strip().split("\n")]
    moves = data[1].strip().replace("\n", "")
dirs = {'^':(-1,0),'v':(1,0),'>':(0,1),'<':(0,-1)}
R = len(g)
C = len(g[0])
start=None
for x in range(R):
    for y in range(C):
        if g[x][y]=='@':
            start = (x,y)
            break
    if start:
        break
x,y = start
for move in moves:
    work = [(x,y)]
    dx,dy = dirs[move]
    nx=x
    ny=y
    flag=True
    while True:
        nx+=dx
        ny+=dy
        c = g[nx][ny]
        if c == '#':
            flag=False
            break
        if c == 'O':
            work.append((nx,ny))
        if c=='.':
            break
    if flag:
        g[x][y]='.'
        g[x+dx][y+dy]='@'
        for mx,my in work[1:]:
            g[mx+dx][my+dy]='O'
        x+=dx
        y+=dy
ans_1=0
for r in range(R):
    for c in range(C):
        if g[r][c] == 'O':
            ans_1 += 100*r+c
print(ans_1)
dob = {'#':'##','@':'@.','O':'[]','.':'..'}
g=[list("".join(dob[c] for c in line)) for line in data[0].strip().split("\n")]

R = len(g)
C = len(g[0])
start=None
for r in range(R):
    for c in range(C):
        if g[r][c]=='@':
            start = (r,c)
            break
    if start:
        break
print(start)
x,y = start
for move in moves:
    work = [(x,y)]
    dx,dy = dirs[move]
    flag=True
    for wx,wy in work:
        nx = wx + dx
        ny = wy + dy
        if (nx,ny) in work:
            continue
        c = g[nx][ny]
        if c == '#':
            flag=False
            break
        if c == '[':
            work.append((nx,ny))
            work.append((nx,ny+1))
        if c == ']':
            work.append((nx,ny))
            work.append((nx,ny-1))
    cg = [row[:] for row in g]

    if flag:
        g[x][y]='.'
        g[x+dx][y+dy]='@'
        for mx,my in work[1:]:
            g[mx][my]='.'
        for mx,my in work[1:]:
            g[mx+dx][my+dy]=cg[mx][my]
        x+=dx
        y+=dy
ans_2=0
for r in range(R):
    for c in range(C):
        if g[r][c]=='[':
            ans_2 +=100*r +c
print(ans_2)
