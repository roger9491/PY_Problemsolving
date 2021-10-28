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