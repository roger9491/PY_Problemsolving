'''
4. 內積
提示:
    先觀察內積特性，把範例做一遍，觀察如何求內積最大值

5 5

    -3  -3  3   3   -3
2   -6  -6  6   6   -6
2   -6  -6  6   6   -6
2   -6  -6  6   6   -6 
2   -6  -6  6   6   -6
2   -6  -6  6   6   -6

ex.1
5 5
-3 -3 3 3 -3
2 2 2 2 2

12


'''
n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[0]*m for i in range(n)]

ans = -10**9
for i in range(n):
    for j in range(m):
        if j == 0:
            dp[i][j] = a[i]*b[j]
            ans = max(ans, dp[i][j])
        else:
            dp[i][j] = max(dp[i-1][j-1], 0) + a[i]*b[j]
            ans = max(ans, dp[i][j])
a = a[::-1]
dp = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if j == 0:
            dp[i][j] = a[i]*b[j]
            ans = max(ans, dp[i][j])
        else:
            dp[i][j] = max(dp[i-1][j-1], 0) + a[i]*b[j]
            ans = max(ans, dp[i][j])
print(ans)