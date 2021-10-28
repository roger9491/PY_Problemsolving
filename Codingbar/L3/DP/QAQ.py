'''
http://codeforces.com/problemset/problem/894/A
"Q""A"Q"AQYSYIOIWIN",
"Q""A"QA"Q"YSYIOIWIN", 
"Q"AQ"A""Q"YSYIOIWIN", 
QA"Q""A""Q"YSYIOIWIN".

Q  0/0
A  0/1
Q  1/1
A  1/3
Q  4/3
Y  4/3
S  4/3
qaq 1

qaqa 3

qaqaq 4
qaq 1 +3
q  aq
  qaq
qa  q


qaq = a




'''

string = input()
dp = [0]*(len(string))
q = 0
qa = 0
for i in range(len(string)):
    if string[i] == 'Q':
        dp[i] = dp[i-1] + qa
        q += 1
    elif string[i] == 'A':
        dp[i] = dp[i-1]
        qa += q
    else:
        dp[i] = dp[i-1]
print(dp[-1])

