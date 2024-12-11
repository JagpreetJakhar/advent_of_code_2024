file_path = 'data_11.txt'
#file_path='sample_11.txt'
e=[]
from collections import defaultdict,deque
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.readlines()
    for line in data :
        line = line.strip()
        e = [int(i) for i in line.split()]
import math
ans_1=0
n = len(e)
for i in range(25):
    j=0
    while j<n:
        if e[j]==0:
            e[j]=1
        elif int(math.log10(e[j])+1)%2 ==0: 
            d = int(math.log10(e[j])+1)
            l = e[j] // 10**(d//2)
            r = e[j] % 10**(d//2)
            e[j]=l
            e.insert(j+1,r)
            j= j+1
            n=n+1
        else:
            e[j] = e[j]*2024
        j+=1
ans_1=len(e)
print(ans_1)
#e = [int(i) for i in line.split()]
from functools import cache

@cache
def process(val,st):
    if st==0:
        return 1
    if val==0:
        return process(1,st-1)
    s = str(val)
    k = len(s)
    if k%2==0:
        return process(int(s[:k//2]),st-1) + process(int(s[k//2:]),st-1)
    return process(val*2024,st-1)

ans_2=sum(process(x,50) for x in e)
print(ans_2)
