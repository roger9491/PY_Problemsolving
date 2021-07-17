n = list(map(int,input().split()))
l = []
dp = [[0]*(n[0]) for i in range(n[1]+1)]
for i in range(n[1]):
    e = list(map(int,input().split()))
    l.append(e)
    
for i in range(n[0]):
    dp[0][i] = l[0][i]


print(dp)


for i in range(1,n[0]):
    for j in range(n[0]):
        print(dp)
        print(i,j)
        print(dp[i-1][j])
        print(dp[i-1][j+1])
        print(l[i][j])
        if i == n[1]:
            dp[i][j] = min(dp[1][j-1],dp[1][j]) + l[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j+1]) + l[i-1][j]

print(dp)