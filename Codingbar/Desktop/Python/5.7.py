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
'''

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

def mergesort(i, j):
    if i == j:
        return i
    else:
        mid = (i + j) // 2
        mergesort(i, mid)
        mergesort(mid+1,j)
    # print(i,j)
    temp = []
    mid = (i + j) // 2
    s = i
    e = j
    j = mid + 1
    while i <= mid or j <= e:
        # print(i,j)
        if (j > e or nums[i] <= nums[j]) and i <= mid:
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1

    # print(temp)
    # print(nums)
    # print(i,j)
    nums[s:e+1] = temp
    # print(nums)
    return nums

nums = [1,454,234,12,6,234,321456,65412,342]
print(mergesort(0, len(nums)-1))

'''
補充
    差分
    需求 頻繁修改區間的值

    https://zerojudge.tw/ShowProblem?problemid=g597


    https://pydoing.blogspot.com/2011/01/python-bitwise.html
    位元運算
    https://judge.tcirc.tw/ShowProblem?problemid=d016
'''
