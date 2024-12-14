file_path = 'data_14.txt'
#file_path='sample_14.txt'
e=[]
from collections import defaultdict,deque
import re
pat = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.readlines()
    for line in data :
        line = line.strip()
        m = re.match(pat,line)
        if m:
            px, py, vx, vy = map(int, m.groups())
            e.append([py,px,vy,vx])
m=103
n = 101
grid = grid = [[0]*n for _ in range(m)]
pos_1 = []
steps = 100
ans_1=0
for x,y,dx,dy in e:
    nx = (x + dx*100)% m 
    ny = (y + dy*100)% n
    pos_1.append((nx,ny))
    grid[nx][ny]+=1
q = [0,0,0,0]
for x,y in pos_1:
    mid_x, mid_y = m // 2, n // 2
    if x == mid_x or y == mid_y:
        continue  # Skip robots on the middle lines
    if x < mid_x and y < mid_y:
        q[0] += 1  # Q1
    elif x >= mid_x and y < mid_y:
        q[1] += 1  # Q2
    elif x < mid_x and y >= mid_y:
        q[2] += 1  # Q3
    elif x >= mid_x and y >= mid_y:
        q[3] += 1  # Q4
ans_1 = q[0]*q[1]*q[2]*q[3]
print(ans_1)
ans_2=0
sf = float('inf')
for s in range(m*n):
    pos=[]
    for x,y,dx,dy in e:
        nx = (x + dx*s)% m 
        ny = (y + dy*s)% n
        pos.append((nx,ny))
    q = [0,0,0,0]
    for x,y in pos:
        mid_x, mid_y = m // 2, n // 2
        if x == mid_x or y == mid_y:
            continue  # Skip robots on the middle lines
        if x < mid_x and y < mid_y:
            q[0] += 1  # Q1
        elif x >= mid_x and y < mid_y:
            q[1] += 1  # Q2
        elif x < mid_x and y >= mid_y:
            q[2] += 1  # Q3
        elif x >= mid_x and y >= mid_y:
            q[3] += 1  # Q4
    t = q[0]*q[1]*q[2]*q[3]
    if t<sf:
        sf = t
        ans_2 = s
print(ans_2)
