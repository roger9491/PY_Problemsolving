
def dfs_stack(x,y):
    stack = [[x,y]]
    path = []

    while stack:
        now = stack.pop()
        if matrix[now[0]][now[1]] in path:
            continue
        path.append(matrix[now[0]][now[1]])
        # print(matrix[now[0]][now[1]])
        if now[0] == n - 1 and  now[1] == n -1:
            print("run away")
            break

        for d in dire:
            i_next = now[0] + d[0]
            j_next = now[1] + d[1]
            if 0 <= i_next < n and 0 <= j_next < n and matrix[i_next][j_next] not in path:
                stack.append([i_next,j_next])
                # path.append(matrix[i_next][j_next])


n = int(input())

matrix = []
for i in range(n):
    e = input().split()
    matrix.append(e)

dire = [[1,0],[0,1],[-1,0],[0,-1]]

dfs_stack(0,0)