'''def f(n):
    if mem[n] != -1:
        return mem[n]

    minv = 10**9
    for i in range(len(mon)):
        if n >= mon[i]:
            a = f(n - mon[i])
            if minv > a:
                minv = a
    mem[n] = 1 + minv
    return mem[n]
    
    


mon = list(map(int,input().split(",")))
n = int(input())

mem = [-1]*(n+1)
mem[0] = 0
f(n)
print(mem[-1])
'''


def C(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for v in value: #從價值最小的開始放，避免重複放
        for i in range(n+1):
            if i - v >= 0:
                dp[i] += dp[i-v]
    return dp[n]

value = list(map(int,input().split(',')))
value.sort() #依照價值，從小排到大
n = int(input())
print(C(n))

'''n = int(input())


for i in range(n):
    a = int(input())
    dp = [0] * (a+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4,a+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[-1])'''













