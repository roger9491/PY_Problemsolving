'''
耐重 12
蘋果 重:3 值:4
雞腿 重:10 值:15
漢堡 重:7 值:10
比薩 重:5 值:7
求最大價值?

狀態定義 
當前耐重下的最大價值

狀態轉移

例子
(1) 10
15       10 - 7 = 3 10 + 4
上一次         放漢堡 
(2)12
15          12 - 5 = 7  7 + 10 = 17
上一次
f() : 該重量的最大價值
max(上一次,f(上一次)(當前耐重-當前物品重量)+當前的物品價值)

'''
# item_h = [3, 10, 7, 5]      #重量
# item_v = [4, 15, 10, 7]     #價值

# dp = [0]*(13) 

# for i in range(4):  #迭代物品
#     for j in range(12,-1,-1):     #迭代耐重
#         if j >= item_h[i]:   #當前耐重 >= 當前物品
#            dp[j] = max(dp[j],dp[j - item_h[i]] + item_v[i])
#         else:
#             dp[j] = dp[j]
#     print(dp)













#二維陣列
# item_h = [3, 10, 7, 5]
# item_v = [4, 15, 10, 7]

# dp = [[0]*(13) for i in range(4)]

# for i in range(4):
#     for j in range(13):
#         if j >= item_h[i]:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-item_h[i]] + item_v[i])
#         else:
#             dp[i][j] = dp[i-1][j]
#     print(dp[i])
# print(dp[-1][-1])

#一維陣列
# item_h = [3, 10, 7, 5]
# item_v = [4, 15, 10, 7]

# dp = [0]*(13) 

# for i in range(4):
#     for j in range(12,-1,-1):
#         if j >= item_h[i]:
#             dp[j] = max(dp[j], dp[j-item_h[i]] + item_v[i])
#     print(dp)
# print(dp[-1])

'''
無限背包
'''
# item_h = [3, 10, 7, 5]
# item_v = [4, 15, 10, 7]

# dp = [[0]*(13) for i in range(4)]

# for i in range(4):
#     for j in range(13):
#         if j >= item_h[i]:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-item_h[i]] + item_v[i])
#         else:
#             dp[i][j] = dp[i-1][j]
#     print(dp[i])
# print(dp[-1][-1])

'''
有限背包


狀態轉移

max(dp[i-1][j],max(dp[i-1][j-item[h]*(n)]+item[v]*n,
                    dp[i-1][j-item[h]*(n+1)]+item[v]*(n+1)
                    dp[i-1][j-item[h]*(n+2)]+item[v]*(n+2)))


(1)12 - 7 = 5  10 + 4 = 14



'''
item_h = [3, 10, 7, 5]
item_v = [4, 15, 10, 7]
item_n = [3, 2, 4, 2]      #物品的數量
dp = [[0]*(13) for i in range(4)]

for i in range(4):
    for j in range(13):
        if j >= item_h[i]:
            maxv = -10**9
            for x in range(1,item_n[i] + 1):    # 1 2 3 物品數量
                if j >= item_h[i] * x:
                    maxv = max(maxv, dp[i-1][j - item_h[i]*x] + item_v[i]*x)
            dp[i][j] = max(maxv, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
    print(dp[i])
print(dp[-1][-1])














# item_h = [3, 10, 7, 5]
# item_v = [4, 15, 10, 7]
# item_n = [3,2,4,2]
# dp = [[0]*(13) for i in range(4)]

# for i in range(4):
#     for j in range(13):
#         maxv = -10**9
#         if j >= item_h[i]:
#             for x in range(item_n[i]):
#                 if j >= item_h[i] * (x+1):
#                     maxv = max(maxv,dp[i-1][j], dp[i-1][j-item_h[i]*(x+1)] + item_v[i]*(x+1))
#             dp[i][j] = maxv
#         else:
#             dp[i][j] = dp[i-1][j]
#     print(dp[i])
# print(dp[-1][-1])

# a = list(map(int,input().split()))
# k = len(a)
# dp = [0]*k

# for i in range(k):
#     for j in range(k):
#         if j > i:
#             if a[i] + i >= j:
#                 if dp[j] == 0:
#                     dp[j] = dp[i] + 1
#                 else:
#                     dp[j] = min(dp[j],dp[i]+1)
#     print(dp)
# print(dp[-1])

