file_path = 'data_13.txt'
#file_path='sample_13.txt'
grid=[]
from collections import defaultdict,deque
import re

patt = re.compile(r"X\+(\d+), Y\+(\d+)|X=(\d+), Y=(\d+)")
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.read()
    for line in data.split("\n\n") :
        m = patt.findall(line)
        a = tuple(map(int, m[0][:2]))
        b = tuple(map(int, m[1][:2]))
        p = tuple(map(int, m[2][2:]))
        grid.append((a,b,p))
ans_1=0
n = len(grid)
for _ in range(n):
    p_a = grid[_][0]
    p_b = grid[_][1]
    tgt = grid[_][2]
    cost =1e9
    flag=False
    for i in range(1,101):
        for j in range(1,101):
            dx = i*p_a[0]+j*p_b[0]
            dy = i*p_a[1]+j*p_b[1]
            if (dx,dy)==tgt:
                flag=True
                cost = min(cost,(3*i+j))
    if flag:
        ans_1+=cost
print(ans_1)
ans_2=0
for _ in range(n):
    p_a = grid[_][0]
    p_b = grid[_][1]
    tgt = grid[_][2]
    cost = 1e14
    t = [tgt[0]+10000000000000,tgt[1]+10000000000000]
    flag=False
    xa,ya=p_a
    xb,yb=p_b
    xp,yp=t
    pa = (xp*yb-yp*xb)/(xa*yb-ya*xb)
    pb = (xp-xa*pa)/xb
    if pa%1==pb%1==0:
        flag = True
        cost = min(cost,3*pa+pb)
    if flag:
        ans_2+=cost
print(ans_2)

