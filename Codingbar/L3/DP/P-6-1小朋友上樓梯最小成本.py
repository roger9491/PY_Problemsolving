'''
https://judge.tcirc.tw/ShowProblem?problemid=d066






'''

# n =int(input())

# a = list(map(int,input().split()))

# dp = [0]*(n)

# for i in range(n):
#     if i == 0:
#         dp[i] = a[i]
#     elif i == 1:
#         dp[i] = a[i]
#     else:
#         dp[i] = a[i] + min(dp[i-2],dp[i-1])
# print(dp[-1])


a=int(input()) #數量
b=input().split() #內容
b=list(map(int,b)) #2 1 1 7 3 2 9 2
# print(b)
L=[0]*(a+1)
L[1]=b[0]

for i in range(2,len(b)+1):
    L[i]=min(L[i-1],L[i-2])+b[i-1]
    #print(L,"LC")
print(L[-1])
