'''
https://codeforces.com/contest/1647/problem/B

'''


t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    matrix = []
    for i in range(n):
        s = input()
        matrix.append(s)

    for i in range(n):
        if i == 0:
            temp = matrix[0]
        else:
            for i in range(m):
                if 


