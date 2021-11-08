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
# # print(item)
# # dp = [[0]*(m + 1) for i in range(len(item))]
# # print(len(dp))
# index = 0
# # for i in item:
# #     for j in range(m + 1):
# #         maxv = -10**9
# #         w = 0
# #         for x in item[i]:
# #             if j >= x[0]:
# #                 if maxv < x[1]:
# #                     maxv = x[1]
# #                     w = x[0]
# #         dp[index][j] = max(dp[index-1][j],dp[index-1][j-w] + maxv)
# #     # print(dp[index])
# #     index += 1
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
LIS
Longest Increasing Subsequence

2, 1, 4, 3, 6, 7, 5

    0   2   1   4   3   6   7   5
2   0   1   1   1   1   1   1   1
1   0   1   1   1   1   1   1   1
4   0   1   2   2   2   2   2   2
3   0   1   2   2   2   2   2   2
6   0   1   2   3   3   3   3   3    
7   0   1   2   3   4   4   4   4
5   0   1   2   3   4   4   4   4

    10  9   2   5   3   7   101 18
10  1   0   0   0   0   0   0   0
9   1   1   0   0   0   0   0   0
2   1   1   1   0   0   0   0   0
5   1   1   1   2   0   0   0   0
3   1   1   1   2   2   0   0   0
7   1   1   1   2   2   3   0   0
101 1   1   1   2   2   3   4   0
18  1   1   1   2   2   3   4   4


    0   1   0   3   2   3
0   1   0   0   0   0   0
1   1   2   0   0   0   0
0   1   2   2   0   0   0
3   1   2   2   3   0   0
2   1   2   2   3   3   0
3   1   2   2   3   3   4

    1   3   6   7   9   4   10  5   6
1   1   0   0   0   0   0   0   0   0
3   1   2   0   0   0   0   0   0   0
6   1   2   3   0   0   0   0   0   0
7   1   2   3   4   0   0   0   0   0
9   1   2   3   4   5   0   0   0   0
4   1   2   3   4   5   3   0   0   0
10  
5
6

狀態定義:
    dp[i]: 為當前索引值內的最長遞增子序列

狀態轉移
    dp[i]: 為當前索引值內的最長遞增子序列
    所以我們只關心 索引值內的
        從索引值內找最長
        索引值一樣 就和1比誰最大
    
'''
# nums = [7,7,7,7,7,7,7]
# n = len(nums)
# dp = [0]*(n)
# for i in range(n):
#     for j in range(n):
#         if i > j:
#             if nums[i] > nums[j]:
#                 dp[i] = max(1,dp[i],dp[j]+1)
#             else:
#                 dp[i] = max(dp[i],1)
#         else:
#             dp[i] = max(dp[i],1)

#     print(dp)
# print(max(dp))
# nums = [7,7,7,7,7,7,7]
# n = len(nums)
# dp = [0]*(n)
# for i in range(n):
#     for j in range(n):
#         if nums[i] > nums[j]:
#             dp[i] = max(1,dp[i],dp[j]+1)
#         else:
#             dp[i] = max(dp[i],1)
#     print(dp)
# print(max(dp))
# nums = [7,7,7,7,7,7,7]
# n = len(nums)
# dp = [0]*(n)
# for i in range(n):
#     for j in range(i+1):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i],dp[j]+1)
#         else:
#             dp[i] = max(dp[i],1)
    

#     print(dp)
# print(max(dp))
# nums = [7,7,7,7,7,7,7]
# n = len(nums)
# dp = [0]*(n)
# for i in range(n):
#     for j in range(n):
#         if i > j:
#             if nums[i] > nums[j]:
#                 dp[i] = max(dp[i],dp[j]+1)
#         else:
#             dp[i] = max(dp[i],1)

#     # print(dp)
# return max(dp)


def dfs(i,j):
    print("i,j",matrix[i][j])
    # input()
    for dir in direction:
        i_next = i + dir[0]
        j_next = j + dir[1]
        if n > i_next >= 0 and n > j_next >= 0:
            if matrix[i_next][j_next] not in record:
                # print(i_next,j_next,dir)
                record.append(matrix[i_next][j_next])
                dfs(i_next,j_next)
                del record[-1]
    print("回去",matrix[i][j])
n = 3
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],]
record = [1]
direction = [[1,0],[0,1],[-1,0],[0,-1]]
dfs(0,0)


# def dfs_stack(i,j):
#     stack = [[0,0]]
#     path = [1]

#     while stack:
#         node = stack.pop()
#         print(matrix[node[0]][node[1]])
        
#         for x in dire:
#             i_next = node[0] + x[0]
#             j_next = node[1] + x[1]
#             if 0 <= i_next < 3 and 0 <= j_next < 3 and matrix[i_next][j_next] not in path:
#                 stack.append([i_next,j_next])
#                 path.append(matrix[i_next][j_next])
                
# dire = [[1,0],[0,1],[-1,0],[0,-1]]

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# dfs_stack(0,0)