'''
c++ L2
動態規劃 01

3
10 40 70
20 50 80
30 60 90


'''
'''
暴力
'''
# def dfs(n, i): 
#     # print(n,i)
#     if n == 0:
#         return t[n][i]
#     return max(dfs(n-1, (i+1)%3), dfs(n-1,(i+2)%3)) + t[n][i]


# n = int(input())
# t = []
# for i in range(n):
#     a, b, j = map(int,input().split())
#     t.append([a,b,j])

# print(max(dfs(n-1, 0), dfs(n-1, 1), dfs(n-1, 2)))

'''
記憶化搜索
'''
# def dfs(n, i): 
#     # print(n,i)
#     if n == 0:
#         return t[n][i]

#     if dp[n][i] != 0:
#         return dp[n][i]
#     dp[n][i] = max(dfs(n-1, (i+1)%3), dfs(n-1,(i+2)%3)) + t[n][i]
#     return dp[n][i]

# n = int(input())
# t = []
# for i in range(n):
#     a, b, j = map(int,input().split())
#     t.append([a,b,j])

# dp = [[0]*3 for i in range(n)]

# print(max(dfs(n-1, 0), dfs(n-1, 1), dfs(n-1, 2)))

'''

'''