def subarr(a, le, ri):
    if le >= ri:
        return 0
    if le+1 == ri:
        return max(a[le], 0)
    mid = (le + ri) // 2
    largest = max(subarr(a, le, mid), subarr(a, mid, ri))

    sum = 0
    lmax = 0 
    rmax = 0
    for i in range(mid-1, le-1, -1):
        sum += a[i]
        lmax = max(lmax, sum)
    sum = 0
    for i in range(mid, ri):
        sum += a[i]
        rmax = max(rmax, sum)

    return max(largest, lmax+rmax)
n = int(input())
a = list(map(int,input().split()))
print(subarr(a, 0, len(a)-1))