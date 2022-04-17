import random
def t1(n,k,a):
    dic = {}
    left = 0
    temp = {}
    for j in range(n):
        print(j,temp,dic,left)
        if a[j] in temp and left <= temp[a[j]]: 
            left = temp[a[j]] + 1
            dic[j] = left
            temp[a[j]] = j
        else:
            temp[a[j]] = j
            dic[j] = left


    dp = [[0]*(n+1) for i in range(k+1)]
    print(dic)
    for i in range(k):
        for j in range(n):
            if j >= i:
                dp[i][j] = max(dp[i][j-1], dp[i-1][dic[j]-1] + j - dic[j] + 1)
            else:
                dp[i][j] = dp[i-1][j]
        print(dp[i])
                
    print(dp[-2][-2])
    return dp[-2][-2]

def t2(n,k,t):
    a = t.copy()
    a = [0] + a
    prev = [0]*100001
    left = [0]*(n+1)
    for i in range(1, n+1):
        left[i] = max(left[i-1], prev[a[i]] + 1)
        prev[a[i]] = i
    
    p = [0]*(n+1)
    d = [0]*(n+1)
    for j in range(k):
        for i in range(1, n+1):
            p[i] = max(p[i-1], d[left[i]-1] + i - left[i] + 1)
        p,d = d,p
    print(d[n])
    return d[n]


while True:
    n, k = 10, 3
    t = []
    for i in range(n):
        t.append(random.randint(1,10))
    ans1 = t1(n, k, t)
    ans2 = t2(n, k, t)
    if ans1 != ans2:
        print(n,k)
        print(" ".join(list(map(str,t))))
        print(ans1,ans2)
        break