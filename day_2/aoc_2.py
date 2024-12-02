
file_path = 'data.txt' 
data =[]
with open(file_path, 'r') as file:
    for line in file:
        data.append([int(i) for i in line.split()])

ans_1=0
for row in data:
    flag=False
    if row==sorted(row) or row==sorted(row,reverse=True):
                flag=True
                row.sort()
                for x,y in zip(row,row[1:]):
                    if not 1<=abs(x-y)<=3:
                        flag= False
    if flag:
        ans_1+=1
        
#----------part_2---------------
ans_2=0
count=0
for row in data:
    flag=False
    for i in range(len(row)):
        trow = row[:i]+row[i+1:]
        if trow==sorted(trow) or trow==sorted(trow,reverse=True):
            trow.sort()
            bad=True
            for x,y in zip(trow,trow[1:]):
                if not 1<=abs(x-y)<=3:
                    bad = False
            if bad:
                flag=True
    if flag:
        ans_2+=1

    
            
            
        

print(ans_1,ans_2)