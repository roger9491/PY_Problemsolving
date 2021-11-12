N = 210
n = int(input())
st = [0] + [int(i) for i in input().split()] * 2
f1 = [[0]*N for i in range(N)]
f2 = [[0]*N for i in range(N)]
for i in range(1,2*n+1):st[i] += st[i-1];

for len in range(2,n+1):
    for i in range(1,2*n-len+2):
        l,r = i,i+len-1
        f1[l][r] = 2**30  
        for k in range(l,r):
            f1[l][r] = min(f1[l][r],f1[l][k]+f1[k+1][r]+st[r]-st[l-1])
            f2[l][r] = max(f2[l][r],f2[l][k]+f2[k+1][r]+st[r]-st[l-1])

mi = 2**30
ma = 0 
for i in range(1,n+1):
    mi = min(mi,f1[i][i+n-1])
    ma = max(ma,f2[i][i+n-1])

print(mi)
print(ma)