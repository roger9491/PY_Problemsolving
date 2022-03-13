'''
https://codeforces.com/contest/1647/problem/0

'''
t = int(input())
for i in range(t):
    n = int(input())

    count1 = n // 3
    count2 = n % 3
    if count2 == 2:
        print("2"+"12"*count1)
    else:
        print("1"*count2 + "21"*count1)