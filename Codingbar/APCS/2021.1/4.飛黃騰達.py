'''

1 1
2 5
3 2
4 5
4 6
5 6


'''

n = int(input())
m = []
for i in range(n):
    a = list(map(int,input().split()))
    m.append(a)
m.sort()

dp = [0]*n

for i in range(n):
    for j in range(i+1):
        if i > j:
            if m[i][1] >= m[j][1]:
                dp[i] = max(dp[i],dp[j]+1)
        else:
            dp[i] = max(dp[i],1)

    # print(dp)
print(max(dp))