n,m,k = map(int,input().split())

move = []
matrix1 = []     #魔王 初始
flag = [1]*k
matrix2 = [[0]*m for i in range(n)]     #炸彈

for i in range(k):
    r,c,s,t = map(int,input().split())
    matrix1.append([r,c])
    move.append([s,t])
'''
移動 -> 放置炸彈 -> 檢查消失
'''
while flag.count(1) != 0:

    for i in range(k):
        if flag[i]:
            x,y = matrix1[i][0],matrix1[i][1]
            matrix2[x][y] += 1  #放置炸彈
            # matrix2[matrix1[i][0]][matrix1[i][1]] = 1
            x += move[i][0]
            y += move[i][1]
            matrix1[i][0],matrix1[i][1] = x,y
    # print(matrix1)
    # print(matrix2)
    for i in range(k):
        if flag[i]:
            x = matrix1[i][0]
            y = matrix1[i][1]
            # print(x,y)
            if not(0 <= x < n and 0 <= y < m):
                flag[i] = 0
            elif matrix2[x][y] == 'x':
                flag[i] = 0
            elif matrix2[x][y] > 0:
                matrix2[x][y] = 'x'
                flag[i] = 0
            
    for i in range(k):
        x = matrix1[i][0]
        y = matrix1[i][1]
        if 0 <= x < n and 0 <= y < m:
            if matrix2[x][y] == 'x':
                matrix2[x][y] = 0
    # print(flag)


ans = 0
for i in range(n):
    for j in range(m):
        if matrix2[i][j] != 0:
            ans += 1
print(ans)


'''
1 6 3
0 0 0 0
0 2 0 -1
0 4 0 2

4




5 5 2
0 0 3 2
0 0 2 3

3
'''
