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
import sys
sys.setrecursionlimit(6010)


def dfs(node):
    if node not in dic:
        dp[node][0] = d[node]
        # print(node, dp)
        return
    total = 0
    dp[node][0] += d[node]
    for i in dic[node]:
        dfs(i)
        dp[node][0] += dp[i][1]
        dp[node][1] += max(dp[i][1], dp[i][0])
    # print(node, dp)
    
n = int(input())

d = [0]
for i in range(n):
    a = int(input())
    d.append(a)
dp = [[0]*2 for i in range(n+1)]
dic = {}
leaves = [0]*(n+1)
for i in range(n-1):
    l, k = map(int,input().split())
    if k in dic:
        dic[k].append(l)
    else:
        dic[k] = [l]
    leaves[l] = 1

for i in range(1,n+1):
    if leaves[i] == 0:
        root = i
dfs(root)
print(max(dp[root]))



