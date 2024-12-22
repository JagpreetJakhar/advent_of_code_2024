from collections import defaultdict,deque
import heapq
import re
from itertools import count,product
from functools import cache
file_path = 'data_22.txt'
#file_path='sample_22.txt'
codes=[]
with open(file_path, "r") as file:
    data = file.readlines()
    for line in data:
        codes.append(int(line.strip()))
def mix(x,y):
    return x^y
def prune(x):
    return x%16777216

def prices(x):
    ans = [x]
    for _ in range(2000):
        x = prune(mix(x, 64*x))
        x = prune(mix(x, x//32))
        x = prune(mix(x, x*2048))
        ans.append(x)
    return ans

def changes(P):
    return [P[i+1]-P[i] for i in range(len(P)-1)]

def getScores(P, C):
    ANS = {}
    for i in range(len(C)-3):
        pattern = (C[i], C[i+1], C[i+2], C[i+3])
        if pattern not in ANS:
            ANS[pattern] = P[i+4]
    return ANS

p1 = 0
SCORE = {}
for code in codes:
    P = prices(code)
    p1 += P[-1]
    P = [x%10 for x in P]
    C = changes(P)
    S = getScores(P,C)
    for k,v in S.items():
        if k not in SCORE:
            SCORE[k] = v
        else:
            SCORE[k] += v
print(p1)
print(max(SCORE.values()))
