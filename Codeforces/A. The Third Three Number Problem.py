'''
https://codeforces.com/contest/1699/problem/A


011
001
010


ex
5
4           100     011 011 001   a : 010   b:000 c: 000       011 xor 011 + 011 xor 001 + 011 xor 001
1
12
2046
194723326

3 3 1
-1
2 4 6
69 420 666
12345678 87654321 100000000

'''
t = int(input())

for i in range(t):
    n = int(input())
    if(n%2 == 0):
        print(n//2,0,0)
    else:
        print(-1)