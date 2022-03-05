'''
https://judge.tcirc.tw/ShowProblem?problemid=d080

階梯數字
25
    1   2   3   4   5   6   7   8   9
1   1   2   3   4   5   6   7   8   9
2   10  19  27 
3                                                      

dp[i][j] = dp[i][j-1] + (9-i) + 1


11
1 ~ 9
11

22
1 ~ 9
11
12~19
22

33
1 ~ 9
11
12~19
22
23~29
33





'''

n = input()

length = len(n)

dp = [[0]*10 for i in range(length)]
dp[0][-1] = 1
ans = 0
for i in range(length):
    for j in range(1,10):
        if i == 0:
            dp[i][j] = dp[i][j-1] + 1
        elif j == 1:
            dp[i][j] = dp[i-1][-1] + 1
        else:
            dp[i][j] = dp[i][j-1] + (9-j+1) + 1
        
        if i == (length - 1):
            if int((i+1)*str(j)) > int(n):
                if j == 1:
                    i -= 1
                    j = 9
                else:
                    j -= 1
                ans += dp[i][j]
                number = int((i+1)*str(j))
                break
 
    print(dp[i])

# for i in range(length):
#     for j in range(9,0,-1)


111
112 ~　150
150
222

22 ~ 25

print(ans)