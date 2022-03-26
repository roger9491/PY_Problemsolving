def f(n):
    # print(n)
    global count
    global ans
    if n == b:
        ans = min(ans, count)
        return

    if count >= ans:
        return
    # print(k)
    for i in [k[n-1],-k[n-1]]:
        # print(n+i)
        next = n + i
        if 1 <= next <= s:
            # print(n+i)
            if path[next] == 0:
                # print(n+i)
                path[next] = 1
                count += 1
                f(next) 
                count -= 1
                path[next] = 0

s, a, b = map(int,input().split())
k = list(map(int,input().split()))
path = [0]*(s+1)
count = 0
ans = 10**9
f(1)
if ans < 10**9:
    print(ans)
else:
    print(-1)