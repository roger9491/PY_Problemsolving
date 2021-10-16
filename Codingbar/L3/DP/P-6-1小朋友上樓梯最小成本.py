'''https://judge.tcirc.tw/ShowProblem?problemid=d066'''

n =int(input())

a = list(map(int,input().split()))

dp = [0]*(n)

for i in range(n):
    if i == 0:
        dp[i] = a[i]
    elif i == 1:
        dp[i] = a[i]
    else:
        dp[i] = a[i] + min(dp[i-2],dp[i-1])
print(dp[-1])
