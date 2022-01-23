'''
7 5
0 1 0 2 1 3 2 3 4 5
2 3
0 6 2 4 3 6
0 6 0 3 3 5


'''
def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def merge(x,y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    else:
        par[a] = b


n, m = map(int,input().split())
a = list(map(int,input().split()))

p ,k = map(int,input().split())

par = [0]*(2*n + 1)

for i in range(2*n + 1):
    par[i] = i    

color = [-1]*n
for i in range(0,2*m-1,2):
    if color 
print(par)

for i in range(p):
    a = list(map(int,input().split()))
    for j in range(k):
        print(find(a[i]),find(a[i+1]))
        if find(a[i]) == find(a[i+1]):
            print(i)
            break
        merge(a[i],a[i]+n)
        merge(a[i+1],a[i+1]+n)
        print(par)

