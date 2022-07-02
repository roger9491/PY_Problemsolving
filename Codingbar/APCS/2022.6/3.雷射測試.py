
def bs(target, a):
    global n
    i = 0
    j = len(a) - 1
    index = -1
    while i <= j:
        mid = (i + j) // 2
        # print("mid",mid)
        if a[mid][0] == target:
            return mid
        elif a[mid][0] > target:
            j = mid - 1
        else:
            i = mid + 1
    return -1


n = int(input())

matrix_x = {0:[[0,0]]}
matrix_y = {0:[[0,0]]}
for i in range(n):
    x, y, t = map(int,input().split())
    if y in matrix_x:
        matrix_x[y].append([x,t])
    else:
        matrix_x[y] = [[x,t]]
    if x in matrix_y:
        matrix_y[x].append([y,t])
    else:
        matrix_y[x] = [[y,t]]
for i in matrix_x:
    # print(matrix_x[i])
    matrix_x[i].sort()
for i in matrix_y: matrix_y[i].sort()

flag = 0    #0右 1左 2上 3下
x = 0
y = 0
ans = 0
flag_matrix = [[2,3,0,1],[3,2,1,0]]
'''
    0   1   2   3
0   2   3   0   1   /
1   3   2   1   0   \\

'''
while True:
    # print("cur flag",x,y,flag)
    if flag == 0:
        index = bs(x, matrix_x[y])  
        if index + 1 == len(matrix_x[y]) or index == -1: break
        tmp = matrix_x[y][index+1]
        x = tmp[0]
        flag = flag_matrix[tmp[1]][flag]
    elif flag == 1:
        index = bs(x, matrix_x[y])  
        if index - 1 < 0 or index == -1: break
        tmp = matrix_x[y][index-1]
        x = tmp[0]
        flag = flag_matrix[tmp[1]][flag]
    elif flag == 2:
        index = bs(y, matrix_y[x])  
        if index + 1 == len(matrix_y[x]) or index == -1: break
        tmp = matrix_y[x][index+1]
        y = tmp[0]
        flag = flag_matrix[tmp[1]][flag]
    elif flag == 3:
        index = bs(y, matrix_y[x])
 
        if index - 1 < 0 or index == -1: break
        tmp = matrix_y[x][index-1]
        y = tmp[0]
        flag = flag_matrix[tmp[1]][flag]
    ans += 1
print(ans)