'''
前綴和 複習

點石成金 優化?
'''



'''
0 1 2 3 4 5
8 5 3 1 2 4

sum = []    #儲存索引值以前的總和
sum[5] = 19
sum[2] = 13
sum[5] - sum[2] = 19 - 13 = 6
sum[1] = 8
sum[0] = 0

再用前綴和之前 需要 預處裡  O(n)
O(n)


'''

'''
前綴和 進階練習

https://zerojudge.tw/ShowProblem?problemid=f638
'''


'''
記憶化搜索


費氏數列    遞迴版
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)
'''
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return f(n-1) + f(n-2)

# n = int(input())
# print(f(n))


'''
費氏數列    記憶化搜索
'''
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif l[n] != -1:
#         return l[n]
#     l[n] = f(n-1) + f(n-2)
#     return  l[n]

# n = int(input())
# l = [-1]*(n+1)

# print(f(n))


'''
來進階一點的題目

走樓梯 如用暴力法解決?

'''

#第一種方法
# def f(n):
#     global ans
#     if n == target:
#         ans += 1
#         return
#     if n + 1 <= target:   
#         f(n+1)
#     if n + 2 <= target: 
#         f(n+2)    

# target = int(input())
# ans = 0
# f(0)
# print(ans)

#第二種方法

# def f(n):
#     global ans
#     if n == 0:
#         ans += 1
#         return
#     for d in [1,2]:
#         if n - d >= 0:
#             f(n-d)

# target = int(input())
# ans = 0
# f(target)
# print(ans)

'''
分析寫法

優化
'''
# def f(n):
#     global ans
#     # print(n,l[n])
#     if n == 0:
#         return 1
#     elif l[n] != -1:
#         return l[n]
#     count = 0
#     for d in [1,2]:
#         if n - d >= 0:
#             count += f(n-d)
#     l[n] = count
#     return l[n]
# target = int(input())
# ans = 0
# l = [-1]*(target+1)
# f(target)
# print(l[-1])

'''
也可寫成 費式數列
'''



'''
DP Dynamic programming 動態規劃
他是一種算法思想 常見的算法思想 : 分治 貪心 窮舉
核心思想: 通過把原問題分解為相對簡單的子問題的方式求解複雜問題的方法。

我們先來看 能用動態規劃解決問題的條件
最佳子結構
    每個階段的最優解是由之前的某個或某些狀態而來的
重疊子問題
    不同階段的最優解含有重複的之前狀態的最優解
無後效性
    當前的狀態是由之前的狀態的最優解得來，而不管從何而來。
    最短路步數是無後效性的，但是最短路徑就有後效性
    
# 所以我們會發現用動態規劃解決的題目通常會用串列來記錄

實作方式:
    遞推
    記憶化搜索

回頭來看看之前寫的記憶化搜索，想想看如何轉成遞推?
費式數列 遞推

那回到小朋友走樓梯
    如何用動態規劃的方式思考? 如何用動態規劃解決?
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構
        
    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移

https://leetcode.com/problems/climbing-stairs/submissions/
https://leetcode-cn.com/problems/climbing-stairs/submissions/
'''





'''
零錢問題
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構

    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移

'''



'''
題目練習
https://judge.tcirc.tw/ShowProblem?problemid=d066

'''










'''
01 背包
https://judge.tcirc.tw/ShowProblem?problemid=d075
'''

'''
分組背包
https://www.luogu.com.cn/problem/P1757
3 5
2
1 2
2 4
1
3 4
1
4 5 

8

'''

m,n = map(int,input().split())

item = {}
for i in range(n):
    a = list(map(int,input().split()))
    if a[2] not in item:
        item[a[2]] = [[a[0],a[1]]]
    else:
        item[a[2]].append([a[0],a[1]])
# print(item)
# dp = [[0]*(m + 1) for i in range(len(item))]
# print(len(dp))
index = 0
# for i in item:
#     for j in range(m + 1):
#         maxv = -10**9
#         w = 0
#         for x in item[i]:
#             if j >= x[0]:
#                 if maxv < x[1]:
#                     maxv = x[1]
#                     w = x[0]
#         dp[index][j] = max(dp[index-1][j],dp[index-1][j-w] + maxv)
#     # print(dp[index])
#     index += 1
dp = [0]*(m + 1)
for i in item:
    for j in range(m,-1,-1):
        maxv = -10**9
        w = 0
        for x in item[i]:
            if j >= x[0]:
                if maxv < x[1]:
                    maxv = x[1]
                    w = x[0]
        dp[j] = max(dp[j],dp[j-w] + maxv)
    # print(dp[index])
# print(dp)
print(dp[-1])



'''
https://codeforces.com/problemset/problem/294/B
背包問題
恰好裝滿的01背包

5
1 12
1 3
2 15
2 5
2 1
'''
# n1 = int(input())

# v = []
# w = []
# total_v = 0
# total_w = 0
# for i in range(n1):
#     a,b = map(int,input().split())
#     v.append(a)
#     w.append(b)
#     total_v += a
#     total_w += b

# dp = [[-10**9]*(total_v + 1) for i in range(n1)]

# for i in range(n1):
#     for j in range(total_v + 1):
#         if j == v[i]:
#             dp[i][j] = max(dp[i-1][j],w[i])
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j - v[i]] + w[i])
#         # elif j > v[i]:
#         #     dp[i][j] = max(dp[i-1][j], dp[i-1][j - v[i]] + w[i])
#         # else:
#         #     dp[i][j] = dp[i-1][j]
#     # print(dp[i])

# for i in range(1,total_v + 1):
#     if i >= total_w - dp[-1][i]:
#         print(i)
#         break