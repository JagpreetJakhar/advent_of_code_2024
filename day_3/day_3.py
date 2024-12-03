import re
file_path = 'data.txt'
with open(file_path, 'r') as file:
    for line in file:
        string = line
string=string[4:]
n = len(string)
with open(file_path, 'r') as file:
    for line in file:
        string = line
p1=0
p2=0
f=True
for i in range(n-11):
    if string[i:i+4].startswith('do()'):
        f=True
    if string[i:i+7].startswith("don't()"):
        f=False
    word = re.match(r'mul\((\d{1,3}),(\d{1,3})\)',string[i:i+12])
    if word:
        x,y=int(word.group(1)),int(word.group(2))
        p1+=x*y
        if f:
            p2+=x*y
print(p1,p2)
