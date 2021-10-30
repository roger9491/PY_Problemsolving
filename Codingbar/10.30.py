'''
https://zerojudge.tw/ShowProblem?problemid=b181
b181: 2. 網路設計


'''
# def kruskal(graph):
#     edge_set = []
    
#     for i in range(len(t)):



# def find(edge_set,)


# n,m = map(int,input().split())
# matrix = [[-1]*(n+1) for i in range(n+1)]
# graph = []
# for i in range(m):
#     a = input().split()
#     t = [int(a[2]),a[0],a[1]]
#     graph.append(t)
# graph.sort()
# print(graph)











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





'''
LIS
Longest Increasing Subsequence
'''



'''
TSP
'''





# matrix = [[10**9]*10 for i in range(10)]

# #測試數據
# edges =  [[0, 1, 3], [1, 2, 5], [2, 3, 5], [3, 4, 3], [4, 0, 7], [4, 1, 6], [0, 3, 4], [2, 0, 4]]
# for u, v, l in edges:
#     matrix[u][v] = l

# dp = [[10**9]*5 for i in range(1<<5)]
# dp[0][0] = 0
# #1 << 5 => 32 => 100000 
# for s in range(1,(1 << 5)):    #遍歷狀態
#     for u in range(5):
#         for v in range(5):
#             if (s >> v) & 1 == 0:
#                 continue
#             dp[s][v] = min(dp[s][v], dp[s - (1 << v)][u] + matrix[u][v])
#     print(bin(s))
#     print(dp[s])
# print(dp[(1 << 5) - 1][0])
# #dp[s][v]表示的是：从0出发，经过s中所有点，到达v点的最短开销

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
#索引值
def dfs(i,j):
    print(matrix[i][j])
    # input()
    for dir in direction:
        i_next = i + dir[0]
        j_next = j + dir[1]
        if n > i_next >= 0 and n > j_next >= 0:
            if matrix[i_next][j_next] not in record:
                record.append(matrix[i_next][j_next])
                dfs(i_next,j_next)
                # del record[-1]

n = 3
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],]
record = [1]
direction = [[1,0],[0,1],[-1,0],[0,-1]]
dfs(0,0)
