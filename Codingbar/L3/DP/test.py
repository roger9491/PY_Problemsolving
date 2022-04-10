def f1(a,m):
    gifts = a
    cost = m

    mem = [{} for i in range(cost+1)]
    mem[0] = {0:1}

    for i in range(1,cost+1):
        for j in gifts:
            if i >= j:
            
                for k in mem[i-j]:
                    if k <= j:
                        big = j
                        if big in mem[i]:
                            mem[i][big] += mem[i-j][k]
                        else:
                            mem[i][big] = mem[i-j][k]
        # print(i,mem[i])
    sum = 0
    for k in mem[-1]:
        sum += mem[-1][k]

    print(sum)
    return sum

def f2(value,n):
    dp = [0]*(n+1)
    dp[0] = 1
    for v in value: #從價值最小的開始放，避免重複放
        for i in range(n+1):
            if i - v >= 0:
                dp[i] += dp[i-v]
    return dp[n]

import random
while True:
    c = random.randint(2,6)
    value = []
    while len(value) != c:
        a = random.randint(1,50)
        if a not in value:
            value.append(a)
    m = random.randint(1,500)
    ans1 = f1(value, m)
    ans2 = f2(value,m)
    print(value,m)
    if ans1 != ans2:
        break