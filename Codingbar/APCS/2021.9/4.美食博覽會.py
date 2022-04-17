'''
https://zerojudge.tw/ShowProblem?problemid=g278

5 1
1 2 1 3 1

3


10 3
1 7 1 3 1 4 4 2 7 4
1 1   1   1   1         
    2       2   2
        3         3
'''

n, k = map(int,input().split())

a = list(map(int,input().split()))

#字典版
# dic = {}
# left = 0
# temp = {}
# for j in range(n):
#     # print(j,temp,dic,left)
#     if a[j] in temp and left <= temp[a[j]]: 
#         left = temp[a[j]] + 1
#         dic[j] = left
#         temp[a[j]] = j
#     else:
#         temp[a[j]] = j
#         dic[j] = left

#雙指針
prev = [0]*(n+1)
dic = [0]*(n+1)
for i in range(n):
    dic[i] = max(dic[i-1], prev[a[i]] + 1)
    prev[a[i]] = i

dp = [[0]*(n+1) for i in range(k+1)]
# print(dic)
for i in range(k):
    for j in range(n):
        if j >= i:
            dp[i][j] = max(dp[i][j-1], dp[i-1][dic[j]-1] + j - dic[j] + 1)
        else:
            dp[i][j] = dp[i-1][j]
    # print(dp[i])
            
print(dp[-2][-2])
