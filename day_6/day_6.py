file_path = 'data_6.txt'
#file_path='sample.txt'
mat =[]
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.readlines()
    for line in data :
        cl = line.strip("\n'")
        l = list(cl)
        mat.append(l)
rows = len(mat)
cols = len(mat[0])
visited = set()
ans_1=0

for x in range(rows):
    for y in range(cols):
        if mat[x][y]=='^':
            start=(x,y)
            break
dirs={'^':(-1,0),'>':(0,1),'V':(1,0),'<':(0,-1)}
ch={(0,1):'V',(-1,0):'>',(0,-1):'^',(1,0):'<'}     
visited.add(start)
x,y=start
orient='^'
while 0<=x<rows and 0<=y<cols:
    dx,dy = dirs[orient]
    nx,ny = x+dx,y+dy
    if  not (0<=nx<rows and 0<=ny<cols):
        break
    if mat[nx][ny]=='#':
        orient = ch[(dx,dy)]
    elif mat[nx][ny] == '.':
        visited.add((nx,ny))
        x,y=nx,ny
    else:
        x,y=nx,ny

print(len(visited))
cands = list(visited)
cands.remove(start)
def cycle(st,mat):
    per = [i[:] for i in mat]
    l = set(st)
    x,y=st
    orient = '^'
    while 0<=x<rows and 0<=y<cols:
        dx,dy = dirs[orient]
        nx,ny = x+dx,y+dy
        if  not (0<=nx<rows and 0<=ny<cols):
            break
        if (dx,dy,nx,ny) in l:
            return True
        if per[nx][ny]=='#':
            orient = ch[(dx,dy)]
            l.add((dx,dy,nx,ny))
        elif per[nx][ny] == '.':
            per[nx][ny]='X'
            x,y=nx,ny
        else:
            x,y=nx,ny
    return False
ans_2=0
for i in cands:
    mat[i[0]][i[1]] = '#'
    if cycle(start,mat):
        ans_2+=1
    mat[i[0]][i[1]]='.'
print(ans_2)

    

