file_path = 'data_5.txt'
#file_path='sample.txt'
data=[]
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.readlines()
rules=[]
x,y=0,0
if file_path=='sample.txt':
    x,y=0,21
if file_path=='data_5.txt':
    x,y=0,1176
for i in range(x,y):
    cl = data[i].strip()
    clean = cl.split("|")
    rules.append((int(clean[0]),int(clean[1])))
if file_path=='sample.txt':
    x,y=22,28
if file_path=='data_5.txt':
    x,y=1177,1379
print(len(data))
#print(len(rules))
pages=[]
for i in range(x,y):
    cl = data[i].strip()
    clean = cl.split(',')
    pages.append( [int(x)for x in clean])
#print(len(pages))
#print(pages)
ans_1=0
from collections import defaultdict,deque
def check(update,graph):
    pos = {p:i for i,p in enumerate(update)}
    for i in graph:
        for j in graph[i]:
            if i in pos and j in pos and pos[i]>pos[j]:
                return False
    return True
graph = defaultdict(list)
for i,j in rules:
    graph[i].append(j)
for u in pages:
    if check(u,graph):
        idx = int(len(u)/2)
        ans_1+=u[idx]
#print(graph)
#print(rules)
#print(pages)
print(ans_1)
ans_2=0
graph=defaultdict(set)
for i,j in rules:
    graph[i].add(j)
from functools import cmp_to_key
def compare(a,b):
    if a in graph[b]:
        return -1
    if b in graph[a]:
        return 1
    return 0
for u in pages:
    if not check(u, graph):  # If the update is not valid
        u.sort(key=cmp_to_key(compare))
        ans_2+=u[len(u)//2]
print(ans_2)
