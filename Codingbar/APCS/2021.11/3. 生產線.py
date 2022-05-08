n, m = map(int,input().split())

dif = [0]*(n+2)
for i in range(m):
    l, r, w = map(int,input().split())
    dif[l] += w
    dif[r+1] -= w
a = list(map(int,input().split()))
pre = []
totoal = 0
for i in range(1,n+1):
    totoal += dif[i]
    pre.append(totoal)

# print(pre)
pre.sort(reverse=True)
a.sort()
# print(pre)
ans = 0
for i in range(n):
    ans += pre[i]*a[i]

print(ans)