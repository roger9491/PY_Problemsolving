r,c,k,m = map(int,input().split())

matrix = []
for i in range(r):
    a = list(map(int,input().split()))
    for i in range(c):
        if a[i] == -1:
            a[i] = -10**9
    matrix.append(a)


dir = [[1,0],[0,1],[-1,0],[0,-1]]
for day in range(m):
    temp = [[0]*c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if matrix[i][j] >= 0:
                per = matrix[i][j] // k
                for x in dir:
                    now_x = i + x[0]
                    now_y = j + x[1]
                    if 0 <= now_x < r and 0 <= now_y < c and matrix[now_x][now_y] >= 0:
                        temp[now_x][now_y] += per
                        matrix[i][j] -= per
                        


    # print(temp)
    # print(matrix)
    for i in range(r):
        for j in range(c):
            if matrix[i][j] >= 0:
                matrix[i][j] += temp[i][j]
    # print(matrix)
minv = 10**9
maxv = 0
for i in range(r):
    maxv = max(maxv,max(matrix[i]))
    for x in matrix[i]:
        if x >= 0 and minv > x:
            minv = x
print(minv)
print(maxv)
