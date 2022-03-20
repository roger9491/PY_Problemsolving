# def bfs(i,j):
#     queue = [[i,j]]
#     path = [[0]*4 for i in range(5)]   #記錄走過   座標 索引值
#     path[i][j] = 1
#     while queue:
#         node = queue.pop(0)
#         print(matrix[node[0]][node[1]])
#         for d in dire:
#             i = node[0] + d[0]
#             j = node[1] + d[1]
#             if 0 <= i < 5 and 0 <= j < 4:
#                 if matrix[i][j] != "x" and path[i][j] == 0:
#                     path[i][j] = 1
#                     queue.append([i,j])

# matrix =  [["s", 1 , 2 ,"x"],
#            [ 3 ,"x", 4 , 5 ],
#            [ 6 , 7 , 8 ,"x"],
#            [ 9 ,"x", 10, 11],
#            [ 12, 13, 14,'e']]
# dire = [[1,0],[0,1],[-1,0],[0,-1]]
# bfs(0,0)












'''
from functools import cmp_to_key

'''
def suml(a):
    total = 0
    for i in a:
        total += i
    return total
a = [[1,2,3],[2,3,4],[4,5,6,4,5,1],[1,2]]
a.sort(key=suml)
print(a)


'''
or
'''

# a.sort(key = sum)

# n = int(input())

# for i in range(n):
    