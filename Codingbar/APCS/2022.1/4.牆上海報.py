'''
h084: 4. 牆上海報
https://zerojudge.tw/ShowProblem?problemid=h084

10 3
5 3 7 5 1 7 5 3 8 4
2 2 1
'''

n,k = map(int,input().split())

h = list(map(int,input().split()))

w = list(map(int,input().split()))

l = min(h)
r = max(h)

ans = 0
while l <= r:
    mid = (l+r) // 2

    index = 0 
    c = 0
    flag = False
    for i in h:
        if i >= mid:
            c += 1
            if c >= w[index]:
                c -= w[index]
                index += 1
            if index == k:
                flag = True
                break
        else:
            c = 0
    if flag:
        ans = max(ans, mid)
    if flag:
        l = mid + 1
    else:
        r = mid - 1 
print(ans)

