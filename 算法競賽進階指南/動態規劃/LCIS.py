'''
https://www.luogu.com.cn/problem/CF10D


7
2 3 1 6 5 4 6
4
1 3 5 6


4
2 2 1 3
2 1 2 3

    2   2   1   3
2   1   1   1   1
1   
2
3
'''
n1 = int(input())
a = list(map(int,input().split()))

n2 = int(input())
b = list(map(int,input().split()))

dp = [[0]*n1 for i in range(n2)]

for i in range(n2):
    for j in range(n1):
        if a[j] == b[i]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(dp[i])
print(dp[-1][-1])




