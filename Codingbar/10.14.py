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


'''def C(n):
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
print(C(n))'''

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

'''分治法                      貪心     動態規劃
divide and conquer         greedy       dp'''




'''
初始值
f(0) = 0
f(1) = 1
遞迴關稀式
f(n) = f(n-1) + f(n-2), n >= 2
'''
# def number(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return  number(n-2) + number(n-1)
'''
5
n = 5
number(4) +     number(3)
number(3) +     number(2)
 2                  
number(2) +     number(1)
 1                  1
number(1) +     number(0)
 1                  0

'''


a=list(map(int,input().split(",")))

n = int(input())

dp = [0] * (n + 1)

for i in range(1,n + 1):      #i: 當前金額
    minv = 10**9    #用來儲存最少的硬幣數量
    for j in a:     #j :幣值    a = 20,16,12,10,5,1
        if i >= j:  # 當前金額 >= 幣值
            # minv = min(dp[i-j],minv)
            if minv > dp[i-j]:      #what is dp[i-j]? dp[i]:求 i 的兌換硬幣數量 最少
                minv = dp[i-j]
    dp[i] = 1 + minv
    print(i,dp)
print(dp[-1])
'''
20,16,12,10,5,1
12

'''




