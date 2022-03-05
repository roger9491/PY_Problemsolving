'''
4
7 0
1 1
2 12
3 12

0
1
3
1

'''

t = int(input())

for i in range(t):
    n, s = map(int,input().split())

    target = n**2


    ans = s // target
    if ans > n + 1:
        ans = n
    print(ans)