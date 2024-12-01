
file_path = 'data.txt' 
from collections import defaultdict,Counter
list1 = []
list2 = []
lookup=Counter()

with open(file_path, 'r') as file:
    for line in file:
        if line.strip():  
            left, right = line.split()  
            list1.append(int(left))    
            list2.append(int(right))  
            lookup[int(right)]+=1 
list1.sort()
list2.sort()

ans=0
for i,j in zip(list1,list2):
    ans+=abs(j-i)
    
print(ans) #1603498
sim_score=0
for i in list1:
    sim_score+= i * lookup.get(i,0)
print(sim_score) #25574739