a,b = map(int,input().split())

n = int(input())
ans = 0
for i in range(n):
    l = list(map(int,input().split()))
    a_count = 0
    b_count = 0
    for j in l:
        if j == a:
            a_count += 1
        elif j == -a:
            a_count -= 1
        elif j == b:
            b_count += 1
        elif j == -b:
            b_count -= 1
    if a_count > 0 and b_count > 0:
        ans += 1
print(ans)

# print(abs(1) == 1)