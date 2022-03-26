'''
01背包問題:
有一個耐重為V的背包，n個物品，每個物品有Wi重量，價值Ci
W:物品list 重量
C:物品list 價值
定義:
    dp[i][j] : i:第i項物品放入，耐重為j的最大價值
狀態轉移:
    dp[i][j] = max(dp[i-1][j], dp[i-1][j-Wi]+Ci)
程式碼:
    for i in range(len(W)):
        for j in range(V):
            if j >= W[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]]+C[i])
            else:
                dp[i][j] = dp[i-1][j]

優化:

空間上: O(V*n) ==> O(V)
我們可以發現 dp[i][j] 是由 dp[i-1][j] 和 dp[i-1][j-W[i]]+C[i] 取最大而來，
若是把空間變1維 dp[i][j] ==> dp[j] ，意義變為j耐重的最大價值，也就是說我們捨棄
儲存前i項的耐重價值，因為由狀態轉移發現我們當前的狀態都是由前一項狀態而來的，
我們在放入新的物品之前，串列本身就是儲存前一項的值，所以沒必要每項都儲存起來。
然而 dp[i-1][j-W[i]]+C[i] 這個轉移式必須用到剩餘重量，為了避免放到重覆的，
我們的耐重迭代必須從大到小迭代。
程式碼:
    for i in range(len(W)):
        for j in range(V,-1,-1):
            if j >= W[i]:
                dp[j] = max(dp[j], dp[j-W[i]]+C[i])
程式碼:
    for i in range(len(W)):
        for j in range(V,w[i]-1,-1):
            dp[j] = max(dp[j], dp[j-W[i]]+C[i])


練習題
https://judge.tcirc.tw/ShowProblem?problemid=d075
'''



'''
完全背包

'''
w = list(map(int,input().split())) #每個食物的飽足度    
p = list(map(int,input().split()))  #每個食物價格
length = len(w)     #有多少種
dp = [[0]*101 for i in range(length)]   #表格
##直覺解法
#錯誤寫法
# for i in range(length):
#     for j in range(101):
#         if j >= w[i]:
#             for x in range(1,j // w[i] + 1):
#                 if j >= x*w[i]:
#                     dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]*x]+p[i]*x)
#                     #這裡的小細節，因為跟上一次比較所以並沒有保存最大值
#                     #它會嘗試的去兌換所有的同一種物品
#                 # print(i,j,dp[i][j],x)
        
#         else:
#             dp[i][j] = dp[i-1][j]
#     print(dp[i])

#正確解法
for i in range(length):
    for j in range(101):
        if j >= w[i]:
            total = 0
            for x in range(1,j // w[i] + 1):
                total = max(total, dp[i-1][j-w[i]*x] + p[i]*x)
            dp[i][j] = max(total, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
    # print(dp[i])

## 原始解法
# for i in range(length):     #迭代每一種食物
#     for j in range(101):    #迭代每一個飽足度
#         if j >= w[i]:       #判斷飽足度能不能負荷食物
#             dp[i][j] = max(dp[i-1][j],dp[i][j-w[i]]+p[i])
#         else:                           #i:為什麼? i-1:食物只能是一個 i:食物無限
#             dp[i][j] = dp[i-1][j]
# dp = [0]*101
## 空間優化
# for i in range(length):
#     for j in range(101):
#         if j >= w[i]:       #判斷飽足度能不能負荷食物
#             dp[j] = max(dp[j],dp[j-w[i]]+p[i])
##找零錢解法
# for i in range(101):
#     for j in range(len(w)):
#         if i >= w[j]:
#             dp[i] = max(dp[i], dp[i-w[j]] + p[j])
# print(dp[-1][-1])

'''
進階練習題
https://codeforces.com/problemset/problem/189/A

'''


