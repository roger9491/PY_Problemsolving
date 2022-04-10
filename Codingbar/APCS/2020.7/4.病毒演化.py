'''
https://zerojudge.tw/ShowProblem?problemid=f582
題意
https://drive.google.com/drive/u/0/folders/10hZCMHH0YgsfguVZCHU7EYiG8qJE5f-m
之AP325講義 最後一題

10 4
1 1 CAGC
2 1 GUAC
3 1 CAGG
4 2 AUGA
5 3 UGUC
6 5 UGGU
7 3 CAAC
8 1 UACG
9 6 CUCC
10 8 ACUC

10 1
1 1 C
2 1 G
3 1 C
4 2 A
5 3 U
6 5 U
7 3 C
8 1 U
9 6 C
10 8 A

'''
import sys
sys.setrecursionlimit(5000)
def dfs(node):
    for i in dic[node]:
        if i not in dic:
            for j in range(m):
                if data[i][j] == "@":
                        dp[i][j] = [0,0,0,0]
                else:
                    dp[i][j][string[data[i][j]]] = 0
        else:
            dfs(i)
    
    for i in range(m):
        if data[node][i] == "@":
            dp[node][i] = [0,0,0,0]
            for j in range(4):
                for x in dic[node]:
                    minv = 10**9
                    for y in range(4):
                        if y != j:
                            minv = min(minv, dp[x][i][y]+1)
                        else:
                            minv = min(minv, dp[x][i][y])
                    dp[node][i][j] += minv
        else:
            dp[node][i][string[data[node][i]]] = 0
            for x in dic[node]:
                minv = 10**9
                for y in range(4):
                    if y != string[data[node][i]]:
                        minv = min(minv, dp[x][i][y]+1)
                    else:
                        minv = min(minv, dp[x][i][y])
                dp[node][i][string[data[node][i]]] += minv 
    # print(node,dp[node])
n, m = map(int,input().split())

dic = {}
data = [[] for i in range(n+1)]
string = {"A":0, "U":1, "C":2, "G":3}
for i in range(n):
    a = input().split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    data[a[0]] = a[-1]
    if a[0] == a[1]:
        root = a[0]
    else:
        if a[1] in dic:
            dic[a[1]].append(a[0])
        else:
            dic[a[1]] = [a[0]]

dp = [[[10**9]*4 for i in range(m)] for i in range(n+1)]

dfs(root)
ans = 0
for i in range(m):
    ans += min(dp[root][i])

print(ans)
'''a                a           c
[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
 [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 
 [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

'''