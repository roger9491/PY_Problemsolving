'''
https://www.luogu.com.cn/problem/P1880

'''

n = int(input())
a = list(map(int, input().split()))
dp = [[10**9]*(n) for i in range(n)]
dp_2 = [[-10**9]*(n) for i in range(n)]

sum_pre = [0]
'''
4
1 3 5 2
1 4 



'''
t = 0
for i in range(n+n-1):
    t += a[i%n]
    sum_pre.append(t)
# print(sum_pre)
ans = 10**9
ans_2 = -10**9
for length in range(n):
    for i in range(n):
        j = (i + length)%n
        # print("i,j",i,j)
        if length == 0:
            i = min(i,j)
            dp[i][i] = 0
            dp_2[i][i] = 0
        else:   #3 0        0 1 dp[3][3] + dp[0][0] + 
            for k in range(length):
                # print(i,j,k)
                if i > j:
                    total = sum_pre[j+n+1] - sum_pre[i]
                    # print(total,sum_pre)
                else:
                    total = sum_pre[j+1] - sum_pre[i]
                dp[i][j] = min(dp[i][j],dp[i][(i+k)%n]+dp[(i+k+1)%n][j] + total)
                dp_2[i][j] = max(dp_2[i][j],dp_2[i][(i+k)%n]+dp_2[(i+k+1)%n][j] + total)  
        # print(dp[i][j],length)
        if length == n - 1:
            ans = min(ans,dp[i][j])
            ans_2 = max(ans_2,dp_2[i][j])
print(ans)
print(ans_2)


'''
3 0
  4 5 9 4
  5-3
  0 1  2 3   4  5 6  
0 4 9 18 22 26 31 40 
3 0
sum_pre[5] - sum_pre[3]
sum_pre[1] - sum_pre[3]
2 3 0 length
0 2
i j                 j = 
        4   -   1                  
sum_pre[i] - sum_pre[j+length]
00  11  22  33 0
  
01  12  23  30 1
11  11  11  11
02  13  20  31 2
27  28  27  28
03  10  21  32 3

8 13 22 = 43
11 16 22
11 16 22
01 23 k =1
4
5 6 5 6
12 17 22
11 11 22 = 44


 


'''
