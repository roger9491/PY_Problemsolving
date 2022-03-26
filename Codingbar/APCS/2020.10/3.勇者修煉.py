'''
https://zerojudge.tw/ShowProblem?problemid=f314
dp

1 5
2 1 4 -7 4
'''
n, m = map(int,input().split())

matrix = []
for i in range(n):
    a = list(map(int,input().split()))
    matrix.append(a)

dp = [[0]*(m+1) for i in range(n)]

for i in range(n):
    if i == 0:
        a = [0]*m
        for j in range(m):
            a[j] = max(a[j-1]+matrix[i][j], matrix[i][j])
        
        b = [0]*(m+1)
        for j in range(m-1,-1,-1):
            b[j] = max(b[j+1]+matrix[i][j], matrix[i][j])

        for j in range(m):
            dp[i][j] = max(a[j], b[j])
    else:
        a = [0]*m
        for j in range(m):
            a[j] = max(a[j-1]+matrix[i][j], dp[i-1][j] + matrix[i][j])
        
        b = [0]*(m+1)
        for j in range(m-1,-1,-1):
            b[j] = max(b[j+1]+matrix[i][j], dp[i-1][j] + matrix[i][j])

        for j in range(m):
            dp[i][j] = max(a[j], b[j])
print(max(dp[-1]))
# import random
# n = 3
# m = 4 
# for i in range(n):
#     t = []
#     for i in range(m):
#         t.append(str(random.randint(-100,100)))
#     print(" ".join(t))







