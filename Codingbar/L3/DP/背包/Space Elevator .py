'''
https://www.luogu.com.cn/problem/P6771
多重背包



3
7 40 3
5 23 8
2 52 6

'''

# n = int(input())

# heigh = 0
# data = []
# for i in range(n):
#     a, b, c = map(int,input().split())
#     data.append([b,a,c])
#     heigh = max(heigh, b)

# data.sort()
# # print(data)
# for i in range(n):
#     data[i] = [data[i][1],data[i][0],data[i][2]]
# # print(data)
# dp = [[-10**9]*(heigh+1) for i in range(n)]
# ans = -10**9
# for i in range(n):
#     for j in range(heigh+1):
#         if j <= data[i][1]:
#             temp = -10**9
#             for x in range(1,data[i][2]+1):
#                 if j > data[i][0]*x:
#                     temp = max(temp, dp[i-1][j - data[i][0]*x] + data[i][0]*x)
#                 elif j == data[i][0]*x:
#                     temp = max(temp, data[i][0]*x)
#                 else:
#                     break
#             dp[i][j] = max(temp, dp[i-1][j])
#     # print(dp[i])

# for i in range(heigh,-1,-1):
#     if dp[-1][i] > 0:
#         print(dp[-1][i])
#         break
# else:
#     print(0)


n = int(input())

heigh = 0
data = []
for i in range(n):
    a, b, c = map(int,input().split())
    data.append([a,b,c])

data.sort(key=lambda a:a[1])

# print(data)
dp = [-10**9]*(data[-1][1]+1)
dp[0] = 0
ans = -10**9
for i in range(n):
    for x in range(1,data[i][2]+1):
        if data[i][0] <= data[i][1]:
            for j in range(data[i][1],data[i][0]-1,-1):
                dp[j] = max(dp[j], dp[j - data[i][0]] + data[i][0])

for i in range(data[-1][1],-1,-1):
    if dp[i] > 0:
        print(dp[i])
        break
else:
    print(0)
