def dfs_stack(i,j):
    stack = [[0,0]]
    path = [1]

    while stack:
        node = stack.pop()
        print(matrix[node[0]][node[1]])
        
        for x in dire:
            i_next = node[0] + x[0]
            j_next = node[1] + x[1]
            if 0 <= i_next < 3 and 0 <= j_next < 3 and matrix[i_next][j_next] not in path:
                stack.append([i_next,j_next])
                path.append(matrix[i_next][j_next])
                
dire = [[1,0],[0,1],[-1,0],[0,-1]]

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

dfs_stack(0,0)
