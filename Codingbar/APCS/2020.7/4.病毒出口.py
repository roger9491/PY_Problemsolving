'''
https://zerojudge.tw/ShowProblem?problemid=f582
題意
https://drive.google.com/drive/u/0/folders/10hZCMHH0YgsfguVZCHU7EYiG8qJE5f-m
之AP325講義 最後一題




'''
def dfs(node):
    # print("當前",node)
    if node not in dic:
        for i in range(m):
            if data[node][i] == "@":
                dp[node][i] = [0,0,0,0]
            else:
                dp[node][i][string[data[node][i]]] = 0

        # for i in range(1, n+1):
        #     print(i,dp[i])

        return


    for i in dic[node]:
        dfs(i)
    
    for i in range(m):
        if data[node][i] == "@":
            dp[node][i] = [0,0,0,0]
            temp_j = 0
            minv = 0
            for j in range(4):
                for x in dic[node]:
                    
        else:
            for x in dic[node]:
                minv = 10**9
                for j in range(4):
                    if j != trans(data[node][1][i]):
                        minv = min(minv, dp[x][i][j] + 1)
                    else:
                        minv = min(minv, dp[x][i][j])
            dp[node][i][trans(data[node][1][i])] = minv
    # print("當前",node)
    # for i in range(1, n+1):
    #     print(i,dp[i])

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
string = {"A":0,"U":1,"C":2,"G":3}
data = [[] for i in range(n+1)]

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
# print("1",dic)
dfs(root)
# for i in range(1, n+1):
#     print(i,dp[i])
ans = 10**9
for i in range(m):
    ans = min(ans, min(dp[root][i]))
print(ans)
'''a                a           c
[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
 [[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 
 [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

'''