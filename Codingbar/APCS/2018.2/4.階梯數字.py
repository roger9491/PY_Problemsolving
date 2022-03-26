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

from re import L


n = input()

length = len(n)

dp = [0]*length

for i in range(length):
    for j in range(1,10):
        
