'''
https://zerojudge.tw/ShowProblem?problemid=g278

5 1
1 2 1 3 1

3


10 3
1 7 1 3 1 4 4 2 7 4
'''

n, k = map(int,input().split())

a = list(map(int,input().split()))

dic = {}

count = 0
ans = 0
for i in range(n):
    if a[i] in dic:
        count = (i - dic[a[i]])
        ans = max(count, ans)
    else:
        count += 1
        dic[a[i]] = i
        ans = max(count, ans)
print(a[i],ans)
