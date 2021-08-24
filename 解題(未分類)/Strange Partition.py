t = int(input())
for i in range(t):
    n,x = list(map(int,input().split()))
    a = list(map(int,input().split()))
    minv = 0
    maxv = 0
    minv = sum(a)
    if minv % x == 0:
        minv = minv  // x
    else:
        minv = int(minv / x)+ 1

    for i in a:
        if i % x == 0:
            maxv += (i // x)
        else:
            maxv += (int(i/x)+1)
    print(minv,maxv)