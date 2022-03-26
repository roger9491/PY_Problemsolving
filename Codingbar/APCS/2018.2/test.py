n,k = map(int,input().split())
l = list(map(int,input().split()))

ms = [0]
mxs = [0]
mx = []
for i in range(n):
    mx.append(l[i]*i)
    mxs.append(mxs[i]+mx[i])
    ms.append(ms[i]+l[i])

ans = 0
def cut(s,t,kn):
    global k,ans
    xc = (mxs[t+1]-mxs[s]) / (ms[t+1]-ms[s])
    if str(xc)[-2:] == '.5':
        xc = int(xc)
    else:
        xc = round(xc)

    ans += l[xc]

    if kn < k:
        if xc-1-s > 1:
            cut(s,xc-1,kn+1)
        if t-xc-1 > 1:
            cut(xc+1,t,kn+1)

cut(0,n-1,1)
print(ans)