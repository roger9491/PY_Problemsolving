n = int(input())
a = list(map(int,input().split()))

p = [0]
minlist = []
for i in range(n):
    p.append(p[i]+a[i])
    minlist.append((a[i],i))
    
minlist.sort()

def fmin(i,j):
 while True:
  data,index = minlist.pop(0)
  if i <= index <= j:
   return index

def fsum(i,j):
    return p[j+1]-p[i]

l,r = 0,n-1
while l < r:
    m = fmin(l,r)
    lefts = fsum(l,m-1)
    rights = fsum(m+1,r)
    if lefts > rights: r = m-1
    else: l = m+1

print(a[l])