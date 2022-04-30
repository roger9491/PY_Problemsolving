'''
https://zerojudge.tw/ShowProblem?problemid=c471

from functools import cmp_to_key

sorted(kids, key=cmp_to_key(cmp))

ex2
總:5
次:5

        底  頂
2/2     6   6      
3/3     6   6

ex2
總:12
次:6

        底  頂
3/1     9   15
4/2     16  16
5/3     21  

2 
20 10 
1 1 
'''

from functools import cmp_to_key
def cmp(x, y):
    if x[0]*y[1] > y[0]*x[1]:
        return -1
    else:
        return 0

n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

t = []
for i in range(n):
    t.append([a[i],b[i]])

t = sorted(t, key=cmp_to_key(cmp))
print(t)
temp = sum(a)
ans = 0
for i in range(n):
    temp -= t[i][0]
    ans += temp*t[i][1]

print(ans)
