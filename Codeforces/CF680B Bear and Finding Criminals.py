n,a = map(int,input().split())

c = list(map(int,input().split()))

ans = 0
for i in range(1,n):
    if a + i <= n and a - i >= 1:
        if c[a+i-1] and c[a-i-1]:
            ans += 2
    elif a + i <= n:
        if c[a+i-1]:
            ans += 1
    elif a - i >= 1:
        if c[a-i-1]:
            ans += 1

if c[a-1]:
    ans += 1
print(ans)
