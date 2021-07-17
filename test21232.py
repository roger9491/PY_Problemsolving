def dfs():
    global flag
    path = []
    stack = [[0,0]]
    while stack:
        new = stack.pop()
        for x in dire:
            i_next = x[0] + new[0]
            j_next = x[1] + new[1]
            if n > i_next >= 0 and n > j_next >= 0:
                if i_next == n - 1 and j_next == n-1:
                    flag = True
                    return
                if m[i_next][j_next] != 'x' and m[i_next][j_next] not in path:
                    stack.append([i_next,j_next])
                    path.append(m[i_next][j_next])




n = int(input())

m = []
for i in range(n):
    s = input().split()
    m.append(s)

flag = False

record = [[0]*n for i in range(n)]

dire = [[1,0],[0,1],[-1,0],[0,-1]]

if m[-1][-1] != 'x':
    dfs()

if flag:
    print("run away")