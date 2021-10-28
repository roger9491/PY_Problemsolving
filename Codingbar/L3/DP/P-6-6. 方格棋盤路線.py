'''https://judge.tcirc.tw/ShowProblem?problemid=d069'''

m,n = map(int,input().split())

matrix = []
for i in range(m):
    a = list(map(int,input().split()))
    matrix.append(a)

dp = [[0]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        if i == 0:
            dp[i][j] = dp[i][j-1] + matrix[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + matrix[i][j]
        else:
            dp[i][j] = matrix[i][j] + max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])

'''

    2 1 1 7 3 2 9 2
0   1 2 3 4 5 6 7 8
(1) 1
(2) 2
'''