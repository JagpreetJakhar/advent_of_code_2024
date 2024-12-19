file_path = 'data_19.txt'
#file_path='sample_19.txt'
d=[]
patterns=[]
designs=[]
from collections import defaultdict,deque
import heapq
import re
from itertools import count
with open(file_path, "r") as file:
    data = file.read().strip()
    patterns,designs = data.split("\n\n")
patterns= patterns.split(", ")
designs = designs.split("\n")
ans_1=0
n = len(designs)
look = set(patterns)
dp = {}
def can_construct(design, patterns):
    if design not in dp:
        if len(design)==0:
            return 1
        else:
            cnt=0
            for sub in patterns:
                if design.startswith(sub):
                    cnt+=can_construct(design[len(sub):],patterns)
            dp[design]=cnt
    return dp[design]
ans_2=0
for tgt in designs:
    if can_construct(tgt, patterns):
        ans_1 += 1
    ans_2+= can_construct(tgt,look)
print(ans_1)
print(ans_2)
