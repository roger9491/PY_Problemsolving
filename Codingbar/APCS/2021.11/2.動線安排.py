def find1(i,j):  #上
    for x in range(i-1,-1,-1):
        if matrix[x][j] == "@":
            return x
    return "NO"

def find2(i,j):  #下
    for x in range(i+1,m):
        if matrix[x][j] == "@":
            return x
    return "NO"

def find3(i,j):  #左
    for x in range(j-1,-1,-1):
        if matrix[i][x] == "@":
            return x
    return "NO"


def find4(i,j):  #右
    for x in range(j+1,n):
        if matrix[i][x] == "@":
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

def count_array(matrix):
    temp = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != "":
                temp += 1
    return temp


m,n,h = map(int,input().split())

matrix = [['']*n for i in range(m)]
# print(matrix)
record = []
count = 0
max_ans = 0
now_ans = 0
for i in range(h):
    r,c,a = map(int,input().split())
    if a == 0:
        matrix[r][c] = "@"

        #上 下 左 右
        x1,x2,y1,y2 = find1(r,c),find2(r,c),find3(r,c),find4(r,c)
        # print(x1,x2,y1,y2)
        if x1 != "NO":
            for j in range(r-1,x1,-1):
                if 'x' not in matrix[j][c]:
                    matrix[j][c] += "x"
        if x2 != "NO":
            for j in range(r+1,x2):
                if 'x' not in matrix[j][c]:
                    matrix[j][c] += "x"
        if y1 != "NO":
            for j in range(c-1,y1,-1):
                if 'y' not in matrix[r][j]:
                    matrix[r][j] += "y"
        if y2 != "NO":
            for j in range(c+1,y2):
                if 'y' not in matrix[r][j]:
                    matrix[r][j] += "y"
    else:
        max_ans = max(max_ans,count_array(matrix))
        matrix[r][c] = ""
        x1,x2,y1,y2 = find1(r,c),find2(r,c),find3(r,c),find4(r,c)
        if x1 != "NO":
            for j in range(r-1,x1,-1):
                if len(matrix[j][c]) == 2:
                    matrix[j][c] = "y"
                else:
                    matrix[j][c] = ""
        if x2 != "NO":
            for j in range(r+1,x2):
                if len(matrix[j][c]) == 2:
                    matrix[j][c] = "y"
                else:
                    matrix[j][c] = ""
        if y1 != "NO":
            for j in range(c-1,y1,-1):
                if len(matrix[r][j]) == 2:
                    matrix[r][j] = "x"
                else:
                    matrix[r][j] = ""
        if y2 != "NO":
            for j in range(c+1,y2):
                if len(matrix[r][j]) == 2:
                    matrix[r][j] = "x"
                else:
                    matrix[r][j] = ""

    # for i in range(m):
    #     print(matrix[i])

now_ans = count_array(matrix)
max_ans = max(max_ans,now_ans)
print(max_ans)
print(now_ans)
