'''
第一行輸入兩個數字
n m
n 代表有多少個數字
m 代表連續幾個
第二行 為 k 數列(n個)

輸出
找出k 中 連續m個 最小和的 起始索引值 (索引值1 ~ n )

ex.
7 3
1 2 6 1 1 7 1

可以找出
索引值 3 4 5 和為 6 1 1 == 8 為最小

輸出 3


'''
n,m = map(int,input().split())

k = list(map(int,input().split()))

pre = []
pre.append(0)
c = 0
for i in range(n):
    c += k[i]
    pre.append(c)

minv = 10**9
ans = 0
for i in range(n-m+1):
    # print(i,i+m)
    temp = pre[i+m] - pre[i]
    if temp < minv:
        minv = temp
        ans = i
print(ans+1)