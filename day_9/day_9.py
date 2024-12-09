file_path = 'data_9.txt'
#file_path='sample_9.txt'
e=[]
from collections import defaultdict
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.readlines()
    for line in data :
        line = line.strip()
        e = [int(x) for x in list(line)]
mem=[]
n = len(e)
file_id=0
for i in range(n):
    if i%2==1:
        for j in range(e[i]):
            mem.append('.')
    else:
        for j in range(e[i]):
            mem.append(file_id)
        file_id+=1
ans_1=0
n = len(mem)
l=0
r=n-1
while l<r:
    if mem[l]!='.':
        l+=1
        continue
    if mem[r]=='.':
        r-=1
        continue
    mem[l],mem[r]=mem[r],mem[l]
for i in range(n):
    if mem[i] !='.':
        ans_1+= i * mem[i]
print(ans_1)
ans_2=0
files={}
spaces=[]
files_id=0
pos=0
for i,v in enumerate(e):
    if i%2==0:
        files[files_id]=((pos,v))
        files_id+=1
    else:
        if v!=0:
            spaces.append((pos,v))
    pos+=v
while files_id>0:
    files_id-=1
    pos,size = files[files_id]
    for i,(s,l) in enumerate(spaces):
        if s>=pos:
            spaces = spaces[:i]
            break
        if size<=l:
            files[files_id]=(s,size)
            if size==l:
                spaces.pop(i)
            else:
                spaces[i] = (s+size,l-size)
            break
for x,(s,l) in files.items():
    for i in range(s,s+l):
        ans_2+= x * i
print(ans_2)
