'''
來進階一點的題目

走樓梯 如用暴力法解決?

核心思想 真的走過一遍

輸入
第幾層

輸出
走法數量


複習上週講到的走樓梯

'''

#第一種
#實際走過一遍
# def f(count):
#     global ans 
#     if count == n:
#         ans += 1
#     for d in [1,2]:
#         if count + d <= n:
#             f(count + d)
# n = int(input())
# count = 0
# ans = 0
# f(0)
# print(ans)

#第二種

# def f(count):
#     global ans 
#     if count == 0:
#         ans += 1
#     for d in [1,2]:
#         if count - d >= 0:
#             f(count - d)
# n = int(input())
# count = 0
# ans = 0
# f(n)
# print(ans)

'''
分析寫法

優化
'''
# def f(count):   #count : 當前走到第幾層
#     if count == 0:  #走到底部 算一條路
#         return 1

#     if mem[count] != -1:
#         return mem[count]
#     total = 0
#     for d in [1,2]: #
#         if count - d >= 0:
#             total += f(count - d)
#     mem[count] = total
#     return mem[count] 
# n = int(input())
# count = 0
# ans = 0
# mem = [-1]*(n+1)
# f(n)
# print(mem[-1])

# def f(count):
#     global ans 
#     if count == 0:
#         return 1
#     elif mem[count] != 0:
#         return mem[count]

#     total = 0
#     for d in [1,2]:
#         if count - d >= 0:
#             total += f(count - d)
#     mem[count] = total
#     return mem[count]

# n = int(input())
# count = 0
# mem = [0]*(n+1)

# f(n)
# print(mem[-1])





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
        dp[n]: 第n曾有幾種走法
    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移
        dp[5] = dp[4] + dp[3]
        dp[n] = dp[n-1] + dp[n-2]
https://leetcode.com/problems/climbing-stairs/submissions/
https://leetcode-cn.com/problems/climbing-stairs/submissions/
'''
'''
嘗試用遞推的方式解決
     迴圈
'''

 



''' 
零錢問題
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構

    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移

'''



'''
題目練習
https://judge.tcirc.tw/ShowProblem?problemid=d066

https://judge.tcirc.tw/ShowProblem?problemid=d069

'''
# a=int(input()) #數量
# b=input().split() #內容
# b=list(map(int,b)) #2 1 1 7 3 2 9 2
# # print(b)
# L=[0]*(a+1)
# L[1]=b[0]

# for i in range(2,len(b)+1):
#     L[i]=min(L[i-1],L[i-2])+b[i-1]
#     #print(L,"LC")
# print(L[-1])
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

'''

'''
有限背包
'''


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
python 可能只能過 64
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


'''
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
nums = [10,9,2,5,3,7,101,18]
n = len(nums)
dp = [0]*(n)
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)


    print(dp)


