#索引值
def dfs(i,j):
    print(matrix[i][j])
    # print(temp)
    # input()
    for dir in direction:
        i_next = i + dir[0]
        j_next = j + dir[1]
        if n > i_next >= 0 and n > j_next >= 0:
            if matrix[i_next][j_next] not in record:
                record.append(matrix[i_next][j_next])
                temp.append(matrix[i_next][j_next])
                dfs(i_next,j_next)
                print(temp)
                del record[-1]
                del temp[-1]

# n = 3
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9],]
n = 2
matrix = [[1,2],
          [3,4],]
record = [1]
direction = [[1,0],[0,1],[-1,0],[0,-1]]
temp = [1]
dfs(0,0)
