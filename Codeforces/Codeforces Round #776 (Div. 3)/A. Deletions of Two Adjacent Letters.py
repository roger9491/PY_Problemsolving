'''
https://codeforces.com/contest/1650/problem/0


5
abcde
c
abcde
b
x
y
aaaaaaaaaaaaaaa
a
contest
t

YES
NO
NO
YES
YES
'''
t = int(input())
for i in range(t):
    s = input()
    c = input()

    temp = []
    length = len(s)
    c_len = len(c)
    for i in range(length - c_len + 1):
        if c in s[i:i+c_len]:
            temp.append([i,i+c_len-1])
    
    for i in range(len(temp)):
        if temp[i][0] % 2 == 0 and (length - 1 - temp[i][1]) % 2 == 0:
            print("YES")    
            break
    else:
        print("NO")

