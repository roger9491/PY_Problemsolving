n,m = map(int,input().split())
heada = list(map(int,input().split()))
grp = [i for i in range(n)]
color = [-1]*n

def boss(x):
    if grp[x] == x: return x
    root = boss(grp[x])
    grp[x] = root
    return root

def unite(a,b):
    aboss = boss(a)
    bboss = boss(b)
    grp[aboss] = bboss

def setcolor(a,b):
    if color[a] != -1 and color[b] != -1:
        if color[a] == color[b]:
            if boss(a) == boss(b):
                return False
            else:
                t = boss(a)
                for i in range(n):
                    if boss(i) == t:
                        color[i] = int(not color[i])
    elif color[a] == color[b] == -1:
        color[a],color[b] = 0,1
    elif color[a] == -1:
        color[a] = int(not color[b])
    else:
        color[b] = int(not color[a])

    return True

for i in range(m):
    a,b = heada[2*i],heada[2*i+1]
    setcolor(a,b)
    unite(a,b)
    

p,k = map(int,input().split())
count_ = 0
for i in range(1,p+1):
    pa = list(map(int,input().split()))
    nowcolor = color.copy()
    nowgrp = grp.copy()
    for j in range(k):
        a,b = pa[2*j],pa[2*j+1] 
        if not setcolor(a,b):
            print(i)
            color = list(nowcolor)
            grp = list(nowgrp)
            count_ += 1
            break
        unite(a,b)

    if count_ >= 3:
        break