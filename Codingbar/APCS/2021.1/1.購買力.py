n,d = map(int,input().split())

ans = 0
c = 0
for i in range(n):
    a = list(map(int,input().split()))
    if max(a) - min(a) >= d:
        ans += sum(a)//3
        c += 1
print(c,ans)