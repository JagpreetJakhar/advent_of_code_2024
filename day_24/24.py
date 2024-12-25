from collections import defaultdict,deque
import heapq
import re
from itertools import count,product,combinations
from functools import cache
file_path = 'data_24.txt'
#file_path='sample_24.txt'
wires=defaultdict(int)
with open(file_path, "r") as file:
    data = file.read()
    seg1,seg2 = data.split('\n\n')

for line in seg1.strip().split('\n'):
    k,v = line.split(':')
    wires[k] = int(v)
#print(wires)
conns=defaultdict(list)
for line in seg2.strip().split('\n'):
    inw,out = line.split(' ->')
    w1,gate,w2 = inw.split()
    conns[(w1,w2)].append((gate,out.strip()))
#print('\n')
while conns:
    for w1 in wires:
        for w2 in wires:
            if w1==w2:
                continue
            if (w1,w2) not in conns and (w2,w1) not in conns:
                continue
            if (w1,w2) in conns:
                a,b=w1,w2
            if (w2,w1) in conns:
                a,b = w2,w1
            for gate,out in conns[(a,b)]:
                x = wires[a]
                y = wires[b]
                match gate:
                    case 'AND':
                        wires[out] = x & y
                    case 'OR':
                        wires[out] = x | y
                    case 'XOR':
                        wires[out] = x ^ y
            conns.pop((a,b))
            break
        else:
            continue
        break
zs=[]
for k in wires:
    if k.startswith('z'):
        zs.append((k,wires[k]))
zs.sort(reverse=True)
ans_1=""
for _,v in zs:
    ans_1+=str(v)
print(int(ans_1,2))
