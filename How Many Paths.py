def dfs(e):
    ans[e-1] += 1    
    # print(e,record[e-1])
    # input()
    if e not in edge or record[e-1] == 1:
        return
    record[e-1] = 1
    for i in edge[e]:
        if i != e:
            dfs(i)
            record[i-1] = 0


def dfs2(e):
    ans[e-1] = -1    
    if e not in edge:
        return

    for i in edge[e]:
        if i != e:
            dfs2(i)




t = int(input())

for i in range(t):
    s = input()
    n,m = map(int,input().split())
    edge = {}
    for i in range(m):
        e1,e2 = map(int,input().split())
        if e1 in edge:
            edge[e1].append(e2)
        else:
            edge[e1] = [e2]
    ans = [0]*n

    check = []
    for i in edge:
        if i in edge[i]:
            check.append(i)
    # print(edge)
    record = [0]*n
    
    dfs(1)
    
    for i in check:
        if ans[i-1] != 0:
            record2 = [0]*n
            dfs2(i)
    # print(ans)
    for i in edge:
        for e in edge:
            if e != i:
                if i in edge[e]:
                    if e in edge[i]:
                        for x in range(n):
                            if ans[x] != 0:
                                ans[x] = -1
    
    print(ans)