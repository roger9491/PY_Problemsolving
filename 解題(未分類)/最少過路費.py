import sys 
sys.setrecursionlimit(1000000)

def dfs(node,value,length):
    global weight
    global minv
    weight += value
    path.append(node)
    if not edges[node] or node in visted:
        if int(path[-1]) == int(first[0]) - 1 :
            if len(path)-1 <= length:
                minv = min(minv,weight)
        return

    visted.append(node)
    for i in edges[node]:
        dfs(i[0],i[1],length)
        weight -= i[1]
        del path[-1]
    del visted[-1]
        
        

first = list(map(int,input().split(" ")))
visted = []
weight = 0
edges = {}
for i in range(first[0]):
    edges[i] = []


for i in range(int(first[1])):
    try:
        e = list(map(int,input().split(" ")))
        if e[0] in edges:
            edges[e[0]].append((e[1],e[2]))
    except:
        break
minv = 10 **7
path = []

dfs(0,0,first[2])


if minv == 10**7:
    print('impossible')
else:
    print(minv)
    