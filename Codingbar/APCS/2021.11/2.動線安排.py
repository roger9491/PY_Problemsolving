def find1(record,i,j):  #上
    for x in range(count):
        # print("11",record,count)
        if record[x][1] == j and i > record[x][0]:
            return x
    return "NO"

def find2(record,i,j):  #下
    for x in range(count):
        if record[x][1] == j and i < record[x][0]:
            return x
    return "NO"

def find3(record,i,j):  #左
    for x in range(count):
        if record[x][0] == i and j > record[x][1]:
            return x
    return "NO"


def find4(record,i,j):  #右
    for x in range(count):
        if record[x][0] == i and j < record[x][1]:
            return x
    return "NO"

def delete(record,i,j): # 刪掉樁
    for i in range(count):
        if record[i] == [i,j]:
            del record[i]
            break



def printm():
    for i in range(m):
        print(matrix[i])

m,n,h = map(int,input().split())

matrix = [['0']*n for i in range(m)]
# print(matrix)
record = []
count = 0
maxv = 0
now = 0
for i in range(h):
    r,c,a = map(int,input().split())
    if a == 0:
        record.append([r,c])
        count += 1
        matrix[r][c] = "@"

        #上 下 左 右
        x1,x2,y1,y2 = find1(record,r,c),find2(record,r,c),find3(record,r,c),find4(record,r,c)
        # print(x1,x2,y1,y2,c)
        if x1 != "NO":
            for j in range(r-1,record[x1][0],-1):
                if matrix[j][c] == "0":
                    matrix[j][c] = str(r)+str(c)
 
        # printm()
        if x2 != "NO":
            for j in range(r+1,record[x2][0]):
                if matrix[j][c] == "0":
                    matrix[j][c] = str(r)+str(c)
 
        # printm()
        if y1 != "NO":
            for j in range(c-1,record[y1][1],-1):
                if matrix[r][j] == "0":
                    matrix[r][j] = str(r)+str(c)

        # printm()
        if y2 != "NO":
            for j in range(c+1,record[y2][1]):
                if matrix[r][j] == "0":
                    matrix[r][j] = str(r)+str(c)

        maxv = max(now,maxv)
        # printm()
        # print(now)
    elif a == 1:
        printm()
        now = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != "0":
                    now += 1
        maxv = max(now,maxv)
        matrix[r][c] = '0'
        delete(record,r,c)
        now -= 1
        count -= 1
        x1,x2,y1,y2 = find1(record,r,c),find2(record,r,c),find3(record,r,c),find4(record,r,c)
        # print(x1,x2,y1,y2,c)
        if x1 != "NO":
            for j in range(r-1,record[x1][0],-1):
                if matrix[j][c] == str(r)+str(c):
                    matrix[j][c] = '0'

        # printm()
        if x2 != "NO":
            for j in range(r+1,record[x2][0]):
                if matrix[j][c] == str(r)+str(c):
                    matrix[j][c] = '0'
 
        # printm()
        if y1 != "NO":
            for j in range(c-1,record[y1][1],-1):
                if matrix[i][j] == str(r)+str(c):
                    matrix[r][j] = '0'
     
        # printm()
        if y2 != "NO":
            for j in range(c+1,record[y2][1]):
                if matrix[i][j] == str(r)+str(c):
                    matrix[r][j] = '0'
now = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] != "0":
            now += 1
printm()


print(maxv)
print(now)