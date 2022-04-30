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
# nums = [10,9,2,5,3,7,101,18]
# n = len(nums)
# dp = [0]*(n)
# for i in range(n):
#     dp[i] = 1
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j]+1)


#     print(dp)
'''
樹型dp

apcs 樹狀圖分析
https://zerojudge.tw/ShowProblem?problemid=c463
'''
# def dfs(node):
 
#     if node not in parent:
#         return 0

#     temp = 0
#     for i in parent[node]:
#         temp =max(temp,dfs(i))  
#     dp[node] = temp + 1
#     # print(node,dp)
#     return dp[node]

# n = int(input())

# parent = {}
# node = [0]*(n+1)
# for i in range(n):
#     a = list(map(int,input().split()))
#     if a[0] != 0:
#         parent[i+1] = a[1:]
#         for j in range(a[0]):
#             node[a[j+1]] = 1

# #find root
# for i in range(1,n+1):
#     if node[i] != 1:
#         root = i
#         break

# dp = [0]*(n+1)
# print(root)
# dfs(root)
# print(sum(dp))

'''
https://www.luogu.com.cn/problem/P1352

樹型dp

7
1
1
1
1
1
1
1
1 3
2 3
6 4
7 4
4 5
3 5

5
0 當前
1 前一街
'''
# import sys
# sys.setrecursionlimit(6010)


# def dfs(node):
#     if node not in dic:
#         dp[node][0] = d[node]
#         # print(node, dp)
#         return
#     total = 0
#     dp[node][0] += d[node]
#     for i in dic[node]:
#         dfs(i)
#         dp[node][0] += dp[i][1]
#         dp[node][1] += max(dp[i][1], dp[i][0])
#     # print(node, dp)
    
# n = int(input())

# d = [0]
# for i in range(n):
#     a = int(input())
#     d.append(a)
# dp = [[0]*2 for i in range(n+1)]
# dic = {}
# leaves = [0]*(n+1)
# for i in range(n-1):
#     l, k = map(int,input().split())
#     if k in dic:
#         dic[k].append(l)
#     else:
#         dic[k] = [l]
#     leaves[l] = 1

# for i in range(1,n+1):
#     if leaves[i] == 0:
#         root = i
# dfs(root)
# print(max(dp[root]))

'''
分治法
divide-and-conquer
分解：將原問題分解成形式相同的子問題。
解決：子問題小到可以直接解決就解決，否則用遞迴的方式解決子問題。
合併：將子問題的解合併，成為原問題的解。

問題:
如何排序數列?
小到大

快速排序法
核心: 小 | 大
'''

# def quicksort(i, j):
#     if i >= j:
#         return 
#     else:
#         print("pivot",i)
#         left = i
#         right = j
#         print(left,right)
#         pivot = i
#         print("pivot",pivot)
#         i += 1
#         while i < j:
#             if nums[i] > nums[pivot] and nums[j] < nums[pivot]: 
#                 nums[i], nums[j] = nums[j], nums[i]

#             if nums[i] <= nums[pivot]:
#                 i += 1
#             if nums[j] >= nums[pivot]:
#                 j -= 1
#         if nums[i] > nums[pivot]:
#             i -= 1
#         nums[i], nums[pivot] = nums[pivot], nums[i]
#         pivot = i 



#     print(nums)
#     quicksort(left, pivot-1)
#     quicksort(pivot+1, right)
#     return nums



# nums = [1,454,234,12,6,234,321456,65412,342]
# print(quicksort(0, len(nums)-1))


# def quick_sort(nums):
#     n = len(nums)

#     def quick(left, right):
#         if left >= right:
#             return nums
#         pivot = left
#         i = left
#         j = right
#         while i < j:
#             while i < j and nums[j] > nums[pivot]:
#                 j -= 1
#             while i < j and nums[i] <= nums[pivot]:
#                 i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#         nums[pivot], nums[j] = nums[j], nums[pivot]
#         quick(left, j - 1)
#         quick(j + 1, right)
#         return nums

#     return quick(0, n - 1)


'''
合併排序法

3 
3 4 5 
1 2 3 

2 
20 10 
1 1 
'''



n = int(input())
w = list(map(int,input().split()))
f = list(map(int,input().split()))
data = []

for i in range(n):
    if f[i] == 0:
        data.append([10**9,i,w[i],f[i]])
    else:
        data.append([w[i]/f[i],i,w[i],f[i]])
data.sort(reverse=True)
# print(data)
temp = sum(w)
ans = 0
for i in range(n):
    temp -= data[i][2]
    ans += temp*data[i][3]

print(ans)