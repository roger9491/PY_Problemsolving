def find1(record,i,j):  #上
    for x in range(c):
        print(record,c)
        if record[x][1] == j and i > record[x][0]:
            return x
    return "NO"

def find2(record,i,j):  #下
    for x in range(c):
        if record[x][1] == j and i < record[x][0]:
            return x
    return "NO"

def find3(record,i,j):  #左
    for x in range(c):
        if record[x][0] == i and j > record[x][1]:
            return x
    return "NO"


def find4(record,i,j):  #右
    for x in range(c):
        if record[x][0] == i and j < record[x][1]:
            return x
    return "NO"


m,n,h = map(int,input().split())

matrix = [[0]*n for i in range(m)]
print(matrix)
record = []
count = 0
for i in range(h):
    r,c,a = map(int,input().split())
    if a == 0:
        record.append([r,c])
        count += 1
        matrix[r][c] = "@"
        #上 下 左 右
        x1,x2,y1,y2 = find1(record,r,c),find2(record,r,c),find3(record,r,c),find4(record,r,c)
        print(x1,x2,y1,y2)
        if x1 != "NO":
            for j in range(r-1,record[x1][0],-1):
                matrix[j][c] = "x"
        if x2 != "NO":
            for j in range(r-1,record[x2][0]):
                matrix[j][c] = "x"
        if y1 != "NO":
            print("y1",c)
            for j in range(c-1,record[y1][1],-1):
                matrix[r][j] = "x"
        if y2 != "NO":
            for j in range(c-1,record[y1][1]):
                matrix[r][j] = "x"
for i in range(m):
    print(matrix[i])