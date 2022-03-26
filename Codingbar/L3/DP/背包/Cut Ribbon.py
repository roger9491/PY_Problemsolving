'''
https://codeforces.com/problemset/problem/189/A
完全背包(恰好裝滿)


'''
n, a, b, c = map(int,input().split())

dp = [-1]*(n+1)

for i in [a,b,c]:
      for j in range(n+1):
            if j == i:
                  dp[j] = max(dp[j], 1) 
            elif j >= i:
                  if dp[j-i] != -1:
                        dp[j] = max(dp[j], dp[j-i] + 1)

print(dp[-1])

