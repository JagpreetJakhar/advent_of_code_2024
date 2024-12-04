#file_path='sample.txt'
file_path = 'data.txt'
data=[]
with open(file_path, 'r') as file:
    for line in file:
        cl=line.strip()
        data.append(list(cl))
ans_1=0
rows =len(data)
cols=len(data[0])

for x in range(rows):
    for y in range(cols):
        if data[x][y]=='X':
            #search horizontally right
            if y+3<cols and (data[x][y+1]=='M' and data[x][y+2]=='A' and data[x][y+3]=='S'):
                ans_1+=1
            #search horizontally left
            if y-3>-1 and (data[x][y-1]=='M' and data[x][y-2]=='A' and data[x][y-3]=='S'):
                ans_1+=1
            #search vertically down
            if x+3<rows and (data[x+1][y]=='M' and data[x+2][y]=='A' and data[x+3][y]=='S'):
                ans_1+=1
           #search vertically up
            if (x-3>-1) and (data[x-1][y]=='M' and data[x-2][y]=='A' and data[x-3][y]=='S'):
                ans_1+=1
            #search diagonally right down
            if (x+3<rows and y+3<cols) and (data[x+1][y+1]=='M' and data[x+2][y+2]=='A' and data[x+3][y+3]=='S'):
                ans_1+=1
            #search diagonally left up
            if (x-3>-1 and y-3>-1) and (data[x-1][y-1]=='M' and data[x-2][y-2]=='A' and data[x-3][y-3]=='S'):
                ans_1+=1 
            #search diagonally left down
            if (x+3<rows and y-3>-1) and (data[x+1][y-1]=='M' and data[x+2][y-2]=='A' and data[x+3][y-3]=='S'):
                ans_1+=1
            #search diagonally right up
            if (x-3>-1 and y+3<cols) and (data[x-1][y+1]=='M' and data[x-2][y+2]=='A' and data[x-3][y+3]=='S'):
                ans_1+=1

print(ans_1)
#print(used)

#----------------------------part_2------------------------------

ans_2=0
def xcenter(x, y):
    tl_br = (
        x - 1 >= 0 and y - 1 >= 0 and data[x - 1][y - 1] in 'MS' and
        x + 1 < rows and y + 1 < cols and data[x + 1][y + 1] in 'MS' and
        ((data[x - 1][y - 1] == 'M' and data[x + 1][y + 1] == 'S') or
         (data[x - 1][y - 1] == 'S' and data[x + 1][y + 1] == 'M'))
    )
    tr_bl = (
        x - 1 >= 0 and y + 1 < cols and data[x - 1][y + 1] in 'MS' and
        x + 1 < rows and y - 1 >= 0 and data[x + 1][y - 1] in 'MS' and
        ((data[x - 1][y + 1] == 'M' and data[x + 1][y - 1] == 'S') or
         (data[x - 1][y + 1] == 'S' and data[x + 1][y - 1] == 'M'))
    )
    return tl_br and tr_bl
for x in range(rows):
    for y in range(cols):
        if data[x][y] == 'A' and xcenter(x, y):
            ans_2 += 1

print(ans_2)
