'''
https://zerojudge.tw/ShowProblem?problemid=f582
題意
https://drive.google.com/drive/u/0/folders/10hZCMHH0YgsfguVZCHU7EYiG8qJE5f-m
之AP325講義 最後一題




'''
def dfs(node):
    if node not in dic:
        for i in range(m):
            if data[node][i] == "@":
                    dp[node][i][trans(data[data[i][0]][1][i])] = 0
            else:
                dp[node][i][trans(data[node][i])] = 0

    for i in dic[node]:
        dfs(i)
    
    for i in range(m):
        if data[node][i] == "@":
                dp[node][i][trans(data[data[i][0]][1][i])] = 0
        else:
            dp[node][i][trans(data[node][i])] = 0


def trans(s):
    if s == "A":
        return 0
    elif s == "U":
        return 1
    elif s == "C":
        return 2
    else:
        return 3

n, m = map(int,input().split())

dic = {}
data = [[] for i in range(n+1)]

for i in range(n):
    a = input().split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    data[a[0]].append(a[1::])
    if a[0] == a[1]:
        root = a[0]
    if a[1] in dic:
        dic[a[1]].append(a[0])
    else:
        dic[a[1]] = [a[0]]

dp = [[[10**9]*4 for i in range(m)] for i in range(n+1)]
print(dp)
dfs(root)
'''a                a           c
[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
 [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 
 [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

'''