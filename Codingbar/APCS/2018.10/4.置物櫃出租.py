'''
https://judge.tcirc.tw/ShowProblem?problemid=d075

演算法: dp (01背包)


ex1
3 10 6  n, m, s
4 4 1   f

5

5 20 14
8 2 7 2 1 

15
'''

# n, m, s = map(int,input().split())

# f = list(map(int,input().split()))

# count = m - s
# ans = sum(f)
# dp = [0]*(count+1)

# if ans <= count:
#     print(0)
# else:
#     for i in range(n):
#         if f[i] > count:
#             pass
#         else:
#             for j in range(count,0,-1):
#                 if j >= f[i]:
#                     dp[j] = max(dp[j-f[i]] + f[i], dp[j])
#                 else:
#                     break
#             # print(dp)


#     print(ans-dp[-1])

n, m, s = map(int,input().split())

f = list(map(int,input().split()))

count = m - s
ans = sum(f)
dp = [0]*(count+1)

if ans <= count:
    print(0)
else:
    for i in range(n):
        if f[i] > count:
            pass
        else:
            for j in range(count,max(count-sum(f),f[i] ),-1):
                if j >= f[i]:
                    dp[j] = max(dp[j-f[i]] + f[i], dp[j])
                else:
                    break
            # print(dp)


    print(ans-dp[-1])
