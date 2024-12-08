file_path = 'data_8.txt'
#file_path='sample_8.txt'
eq =[]
from collections import defaultdict
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.readlines()
    for line in data :
        cl = line.strip()
        eq.append(list(cl))
m = len(eq)
n = len(eq[0])
ant = defaultdict(list)
for r in range(m):
    for c in range(n):
        if eq[r][c]!='.':
            ant[eq[r][c]].append((r,c))
ans_1=set()
for c in ant.keys():
    coord = ant[c]
    for f,(x,y) in enumerate(coord):
        for s in range(f+1,len(coord)):
            dx,dy = coord[s]
            nx,ny = dx-x,dy-y
            if nx!=0 or ny!=0:
                ans_1.add((nx+dx,ny+dy))
                ans_1.add((x-nx,y-ny))
cnt_1=0
for x,y in ans_1:
    if 0<=x<m and 0<=y<n:
        cnt_1+=1
print(cnt_1)
ans_2=set()
cnt_2=0
for c in ant.keys():
    coord = ant[c]
    for f,(x,y) in enumerate(coord):
        for s in range(f+1,len(coord)):
            dx,dy = coord[s]
            nx,ny = dx-x,dy-y
            if nx!=0 or ny!=0:
                sx,sy=x,y
                while 0<=sx<m and 0<=sy<n:
                    ans_2.add((sx,sy))
                    sx,sy=sx-nx,sy-ny
                sx,sy=x,y
                while 0<=sx<m and 0<=sy<n:
                    ans_2.add((sx,sy))
                    sx,sy=sx+nx,sy+ny
for x,y in ans_2:
    if 0<=x<m and 0<=y<n:
        cnt_2+=1
print(cnt_2)
