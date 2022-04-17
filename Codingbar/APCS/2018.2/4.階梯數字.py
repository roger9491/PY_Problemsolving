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



1 2 3 4 5 6 7 8 9

'''


n = input()

length = len(n)

c = [0]*(length - 1)

c[0] = 9
for i in range(length-1):
    if i == 0:
        c[i] = 9
    else:
        c[i] = c[i-1]
        
