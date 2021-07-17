def dfs_stack(i, j):
    queue = [[0, 0]]
    path[0][0] = 1
    count = 0
    while queue:
        size = len(queue)
        while size != 0:
            node = queue.pop(0)
            # if matrix[node[0]][node[1]] == "E":
            #     print(count)
            #     return
            if node[0] == 3 and node[1] == 3:
                print(count)
                return
            for x in dire:
                i_next = node[0] + x[0]
                j_next = node[1] + x[1]
                if 0 <= i_next < n and 0 <= j_next < n and path[i_next][j_next] == 0:
                    if matrix2[i_next][j_next] != "x":
                        queue.append([i_next, j_next])
                        path[i_next][j_next] = 1
            size -= 1
        count += 1


n = 4   #6

matrix = [["s", 1, 1, "x", 1, 1],
          [1, "x", 1, "x", 1, "x"],
          [1, 1, "x", 1, 1, 1],
          ["x", 1, 1, 1, "x", 1],
          [1, 1, "x", 1, "x", 1],
          [1, "x", 1, 1, "x", "E"]]

matrix2 = [["s", 1 , 1 ,"x"],
           [ 1 ,"x", 1 , 1 ],
           [ 1 , 1 ,"x","x"],
           [ 1 , 1 , 1 , 1 ]]

path = [[0]*6 for i in range(6)]
print(path)

dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]

dfs_stack(0, 0)