file_path = 'data_7.txt'
#file_path='sample_7.txt'
eq =[]
with open(file_path, "r") as file:
    # Read lines and strip any extra whitespace
    data = file.readlines()
    for line in data :
        l = line.strip()
        cl = l.split(": ")
        eq.append((int(cl[0]),[int(x) for x in cl[1].split()]))
ans_1=0

for i in range(len(eq)):
    tgt = eq[i][0]
    vals = eq[i][1]
    n=len(vals)
    flag=False
    for op in range(1<<(n-1)):
        tmp=vals[0]
        for j in range(n-1):
            if (op & (1<<j)) > 0:
                tmp*= vals[j+1]
            else:
                tmp += vals[j+1]
        if tmp==tgt:
                flag = True
    if flag:

        ans_1+=tgt
print(ans_1)
def calc(arr,val,tgt,idx,n):
    if idx == n:
        if val == tgt:
            return True

        else:
            return False

    return (calc(arr,val+arr[idx],tgt,idx+1,n) or
    calc(arr,val*arr[idx],tgt,idx+1,n) or
    calc(arr,int(str(val)+str(arr[idx])),tgt,idx+1,n))
ans_2=0
for i in range(len(eq)):
    tgt = eq[i][0]
    vals = eq[i][1]
    n=len(vals)
    flag = calc(vals,vals[0],tgt,1,n)
    if flag:
        ans_2+=tgt
print(ans_2)
