n, m = map(int,input().split())

t = []
for i in range(n):
    a,b = map(int,input().split())
    t.append([b,a])
t.sort()
ans = 0
temp = []
for i in range(n):
    if i == 0:
        ans += m 
    else:
        i = 0
        j = len(temp) - 1
        while i < j:
            pass
