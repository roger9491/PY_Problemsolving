'''
零錢問題
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構

    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移


20,16,12,10,5,1
29

3
'''

# a = list(map(int,input().split(",")))
# m = int(input())

# ans = 10**9
# count = 0
# def dfs(n):
#     if n == 0:
#         return 0
#     minv = 10**9
#     for i in a:
#         if n >= i:
#             minv = min(minv, dfs(n - i) + 1)
#     return minv      

# print(dfs(m))

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
1 2 3 4 1               1           1 


''' 
零錢問題    (優化版)
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構

    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移


20,16,12,10,5,1
29

3

'''
# a = list(map(int,input().split(",")))
# m = int(input())

# dp = [-1]*(m + 1)
# ans = 10**9
# count = 0
# def dfs(n):
#     if n == 0:
#         return 0
#     elif dp[n] != -1:
#         return dp[n]
#     minv = 10**9
#     for i in a:
#         if n >= i:
#             minv = min(minv, dfs(n - i) + 1)
#     dp[n] = minv
#     return dp[n]


# dfs(m)
# print(dp[m])


''' 
零錢問題    (遞推版)
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構

    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移


20,16,12,10,5,1
29

3

'''
# a = list(map(int,input().split(",")))
# m = int(input())

# dp = [10**9]*(m + 1)
# ans = 10**9
# count = 0

# dp[0] = 0
# for i in range(m+1):
#     for j in range(len(a)):
#         if a[j] <= i:
#             dp[i] = min(dp[i],dp[i - a[j]] + 1)
# print(dp[m])

'''
搶分比賽


12  耐重
3 10 7 5    重量
4 15 10 7   分數

17
'''

# 暴力
# w = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))


# def dfs(i, j):
#     if i == -1 or j == 0:
#         return 0
    
#     maxv = dfs(i - 1, j)

#     if j >= a[i]:
#         maxv = max(maxv, dfs(i - 1, j - a[i]) + b[i])
#     return maxv


# print(dfs(len(a) - 1, w))

# 記憶優化

# w = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# dp = [[0]*(w+1) for i in range(len(a))]

# def dfs(i, j):
#     if i == -1 or j == 0:
#         return 0
        
#     print(i, j)
#     if dp[i][j] != 0 :
#         return dp[i][j]


    
#     maxv = dfs(i - 1, j)

#     if j >= a[i]:
#         maxv = max(maxv, dfs(i - 1, j - a[i]) + b[i])
#     dp[i][j] = maxv
#     '''
#     ans = max(dfs(i - 1, j), dfs(i - 1, j - a[i]) + b[i])
    
#     '''
#     for i in range(len(a)):
#         print(dp[i])

#     return maxv


# print(dfs(len(a) - 1, w))


'''

重/價   0   1   2   3   4   5   6   7   8   9   10  11  12  
3/4     0   0   0   4   4   4   4   4   4   4   4   4   4      
10/15   0   0   0   4   4   4   4   4   4   4   15  15  15
7/10    0   0   0   4   4   4   4   10  10  10  15  15  15
5/7     0   0   0   4   4   7   7   7   11  11  15
4 15 10 7
    15  

表格初始值 = 0
dp[i][j] = dp[i-1]
dp = [[0]*13 for i in range(4)]

'''
# Limit = int(input())
# Weight = list(map(int,input().split())) #重量
# Scores = list(map(int,input().split())) #分數
# dp = [[0]*(Limit+1) for i in range(len(Weight))]    #表格

# for i in range(len(Weight)):
#     for j in range(1,Limit+1):                      
#         if j >= Weight[i]:  #15         7     +  dp[i][10 - 5]  7
#             dp[i][j] = max(dp[i-1][j], Scores[i]+dp[i-1][j-Weight[i]])
#         else:
#             dp[i][j] = dp[i-1][j]
# print(dp[-1][-1])

'''
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構
        dp[i][j] : 放到第i項物品j耐重的情況下的最大價值
    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移



'''


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




# w = list(map(int,input().split())) #每個食物的飽足度    
# p = list(map(int,input().split()))  #每個食物價格
# length = len(w)     #有多少種
# dp = [[0]*101 for i in range(length)]   #表格
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
# for i in range(length):
#     for j in range(101):
#         if j >= w[i]:
#             total = 0
#             for x in range(1,j // w[i] + 1):
#                 total = max(total, dp[i-1][j-w[i]*x] + p[i]*x)
#             dp[i][j] = max(total, dp[i-1][j])
#         else:
#             dp[i][j] = dp[i-1][j]
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

中文解釋
https://www.luogu.com.cn/problem/CF189A 
'''

'''
有限背包
'''

#(記憶化搜索)
# m = int(input())
# c = list(map(int,input().split()))
# p = list(map(int,input().split())) #每個食物的飽足度    
# w = list(map(int,input().split()))  #每個食物價格
# dp = [[-1]*(m+1) for i in range(len(w))]

# def dfs(i, j):
#     if i == -1:
#         return 0  
#     elif dp[i][j] != -1 :
#         return dp[i][j]

#     maxv = 0
#     for x in range(c[i] + 1):
#         if x == 0:
#             maxv = dfs(i-1, j)
#         else:
#             if j + p[i]*x <= m:
#                 maxv = max(maxv, dfs(i-1, j + p[i]*x) + w[i]*x)
#             else:
#                 break
#     dp[i][j] = maxv
#     return maxv

# print(dfs(len(w) - 1, 0))


# money = int(input())    #金額
# num = list(map(int,input().split()))    #物品數量
# money1 = list(map(int,input().split())) #特價
# money2 = list(map(int,input().split())) #原價
 
# dp = [[0]*(money+1) for i in range(len(num))]   #表格

# for i in range(len(money1)):
#     for j in range(1,money+1):
#         if j >= money1[i]:  #金額能不能買物品
#             maxv = 0    #儲存最大金額
#             for r in range(1,num[i]+1):     #迭代所有的數量
#                 if j >= money1[i]*r :    
#                     # 條件1:金額要大於等於 成本 且 
#                     maxv = max(maxv,dp[i-1][j-money1[i]*r]+money2[i]*r)   #dp[i-1] :記得要減一，原因是如果不減一就會用到
#                 else:
#                     break
#             dp[i][j] = max(dp[i-1][j],maxv)     #當前用過的物品
#         else:
#             dp[i][j] = dp[i-1][j]
   
# print(dp[-1][-1])
'''
money = int(input())
num = list(map(int,input().split()))
money1 = list(map(int,input().split()))
money2 = list(map(int,input().split()))

for i in range(len(money1)):
    for j in range(num[i]-1):
        money1.append(money1[i])
        money2.append(money2[i])

length = len(money1)
dp = [[0]*(money+1) for i in range(length)]

for i in range(length):
    for j in range(1,money+1):
        if j >= money1[i]: 
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-money1[i]]+money2[i])
        else:
            dp[i][j] = dp[i-1][j]
	#print(dp[j])

print(dp[-1][-1])
'''


'''
進階練習題
python  64分即可 可以想想看滿分解 
https://www.luogu.com.cn/problem/P6771

恰好01
https://codeforces.com/problemset/problem/294/B
https://www.luogu.com.cn/problem/CF294B
'''


'''
LCS
Longest Common Subsequence

'''

# s1 = input()
# s2 = input()
'''
    b   s   b   i   n   i   n   m
j   0   0   0   0   0   0   0   0
m   0   0   0   0   0   0   0   1
j   0   0   0   0   0   0   0   1
k   0   0   0   0   0   0   0   1
b   1   1   1
k
j
k
v

    T   A   T   G   C   A
A   0   1   1   1   1   1
T   1   1   2   2   2   2
C   1   1   2   2   3   3
A   1   2   2   2   3   4
G   1   2   2   3   3   4
A   1   2   2   3   3   4
T

T A T
A T T

'''

# 記憶化搜索

# def dfs(s1, s2, i, j):
#     # print(i, j)
#     if i == len(s1) or j == len(s2):
#         return 0
#     elif dp[i][j] != -1:
#         return dp[i][j]
    
#     maxv = 0
#     if s1[i] == s2[j]:
#         maxv = max(maxv, dfs(s1, s2, i + 1, j + 1) + 1)

#     maxv = max(maxv, dfs(s1, s2, i + 1, j))
#     maxv = max(maxv, dfs(s1, s2, i, j + 1)) 
#     dp[i][j] = maxv
#     return maxv

# s1 = input()
# s2 = input()
# dp = [[-1]*len(s2) for i in range(len(s1))]
# print(dfs(s1, s2, 0 , 0))



# s1 = input()
# s2 = input()

# dp = [[0]*(len(s1)+1) for i in range(len(s2)+1)]

# for i in range(1,len(s2)+1):
#     for j in range(1,len(s1)+1):
#         if s1[j-1] == s2[i-1]:
#             dp[i][j] = max(dp[i][j-1],dp[i-1][j-1]+1)   #因為 當前一樣 上一次的前一個肯定沒有當前的+1
#         else:
#             dp[i][j] = max(dp[i][j-1],dp[i-1][j])
#             # dp[i][j] = dp[i][j-1]
# print(dp[-1][-1])

'''
https://leetcode-cn.com/problems/longest-increasing-subsequence/submissions/
LIS
Longest Increasing Subsequence

2, 1, 4, 3, 6, 7, 5

    2   1   4   3   6   7   5
2   1   0   0   0   0   0   0 
1   1   1   0   0   0   0   0
4   1   1   2   0   0   0   0
3   1   1   2   2   0   0   0
6   1   1   2   2   3   0   0
7   1   1   2   2   3   4   0
5   1   1   2   2   3   4

    10  9   2   5   3   7   101 18
10  1   0   0   0   0   0   0   0
9   1   1   0   0   0   0   0   0
2   1   1   1   1   0   0   0   0
5   1   1   1   2   0   0   0   0
3   1   1   1   2   
7   
101    
18

    4   10  4   3   8   9
4   1
10  1   2 
4   1   2   1     
3   1   2   1   1
8   1   2   1   1   2
9   1   2   1   1   2   3

狀態定義:
    dp[i]: 以索引值i結尾的最長上升長度

狀態轉移

    1 ~ i-1 :j
    if n[i] > n[j]:
        dp[i] = max(dp[j]+1)

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

# m,n = map(int,input().split())

# item = {}
# for i in range(n):
#     a = list(map(int,input().split()))
#     if a[2] not in item:
#         item[a[2]] = [[a[0],a[1]]]
#     else:
#         item[a[2]].append([a[0],a[1]])
# print(item)
# dp = [[0]*(m + 1) for i in range(len(item))]
# print(len(dp))
# index = 0
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
# dp = [0]*(m + 1)
# for i in item:
#     for j in range(m,-1,-1):
#         maxv = -10**9
#         w = 0
#         for x in item[i]:
#             if j >= x[0]:
#                 if maxv < x[1]:
#                     maxv = x[1]
#                     w = x[0]
#         dp[j] = max(dp[j],dp[j-w] + maxv)
#     # print(dp[index])
# # print(dp)
# print(dp[-1])



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


