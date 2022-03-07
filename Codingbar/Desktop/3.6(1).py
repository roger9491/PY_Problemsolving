'''
dfs 搜索最短路徑 + 最短路徑距離
matrix3 = [["s", 1 , 2 ,"x"],
           [ 3 ,"x", 4 , 5 ],
           [ 6 , 7 , 8 ,"x"],
           [ 9 ,"x", 10, 11]
           [ 12, 13, 14,'e']]
matrix = [['s',   1, 'x', 'x',   2,   3,   4,   5,   6,   7],
          ['x',   8,   9,  10, 'x', 'x',  11, 'x', 'x',  12],
          ['x', 'x', 'x',  13,  14, 'x',  15, 'x',  16,  17],
          ['x', 'x', 'x', 'x',  18, 'x',  19, 'x',  20, 'x'],
          [ 21,  22,  23,  24,  25,  26,  27, 'x',  28,  29],
          ['x',  30, 'x', 'x', 'x', 'x', 'x', 'x',  31, 'x'],
          ['x',  32, 'x',  33, 'x', 'x',  34,  35,  36, 'x'],
          [ 37,  38,  39,  40,  41,  42,  43, 'x',  44, 'x'],
          ['x',  45, 'x', 'x', 'x', 'x', 'x', 'x',  46, 'x'],
          ['x',  47,  48,  49,  50,  51,  52,  53,  54, 'e']]
'''
# def dfs(i,j):
#     if matrix[i][j] == "e":
#         print(len(temp),temp)
#         ans.append([len(temp),temp.copy()])
#         return

#     for d in dir:
#         next_i = i + d[0]
#         next_j = j + d[1]
#         if 0 <= next_i < 10 and 0 <= next_j < 10:
#             if path[next_i][next_j] == 0 and matrix[next_i][next_j] != "x":
#                 path[next_i][next_j] = 1
#                 temp.append(matrix[next_i][next_j])
#                 dfs(next_i,next_j)
#                 path[next_i][next_j] = 0
#                 del temp[-1]

# matrix = [['s',   1, 'x', 'x',   2,   3,   4,   5,   6,   7],
#           ['x',   8,   9,  10, 'x', 'x',  11, 'x', 'x',  12],
#           ['x', 'x', 'x',  13,  14, 'x',  15, 'x',  16,  17],
#           ['x', 'x', 'x', 'x',  18, 'x',  19, 'x',  20, 'x'],
#           [ 21,  22,  23,  24,  25,  26,  27, 'x',  28,  29],
#           ['x',  30, 'x', 'x', 'x', 'x', 'x', 'x',  31, 'x'],
#           ['x',  32, 'x',  33, 'x', 'x',  34,  35,  36, 'x'],
#           [ 37,  38,  39,  40,  41,  42,  43, 'x',  44, 'x'],
#           ['x',  45, 'x', 'x', 'x', 'x', 'x', 'x',  46, 'x'],
#           ['x',  47,  48,  49,  50,  51,  52,  53,  54, 'e']]

# # matrix = [["s", 1 , 2 ,"x"],
# #            [ 3 ,"x", 4 , 5 ],
# #            [ 6 , 7 , 8 ,"x"],
# #            [ 9 ,"x", 10, 11],
# #            [ 12, 13, 14,'e']]
# path = [[0]*10 for i in range(10)]
# temp = [matrix[0][0]]
# dir = [[1,0],[0,1],[-1,0],[0,-1]]
# ans = []
# path[0][0] = 1
# dfs(0,0)
# ans.sort()
# print(ans)



# def dfs(i,j):
#     # print("索引值",i,j)
#     if matrix[i][j] == "e":
#         print(len(temp),temp)
#         return

#     for x in dir:
#         now_i = i + x[0]
#         now_j = j + x[1]
#         if 0 <= now_i < n[0] and 0 <= now_j < n[1]:
#             # print(matrix1[now_i][now_j])
#             if matrix[now_i][now_j] not in record and matrix[now_i][now_j] != "x":
#                 record.append(matrix[now_i][now_j])    #紀錄
#                 temp.append(matrix[now_i][now_j])
#                 dfs(now_i,now_j)    #走這條路
#                 del record[-1]
#                 del temp[-1]

# matrix = [["s", 1 , 2 ,"x"],
#            [ 3 ,"x", 4 , 5 ],
#            [ 6 , 7 , 8 ,"x"],
#            [ 9 ,"x", 10, 11],
#            [ 12, 13, 14,'e']]
# matrix = [['s',   1, 'x', 'x',   2,   3,   4,   5,   6,   7],
#           ['x',   8,   9,  10, 'x', 'x',  11, 'x', 'x',  12],
#           ['x', 'x', 'x',  13,  14, 'x',  15, 'x',  16,  17],
#           ['x', 'x', 'x', 'x',  18, 'x',  19, 'x',  20, 'x'],
#           [ 21,  22,  23,  24,  25,  26,  27, 'x',  28,  29],
#           ['x',  30, 'x', 'x', 'x', 'x', 'x', 'x',  31, 'x'],
#           ['x',  32, 'x',  33, 'x', 'x',  34,  35,  36, 'x'],
#           [ 37,  38,  39,  40,  41,  42,  43, 'x',  44, 'x'],
#           ['x',  45, 'x', 'x', 'x', 'x', 'x', 'x',  46, 'x'],
#           ['x',  47,  48,  49,  50,  51,  52,  53,  54, 'e']]
# n = [len(matrix), len(matrix[0])]
# record = ["s"]    #用來記錄你走過路
# #       下     右    上     左
# dir = [[1,0],[0,1],[-1,0],[0,-1]]
# temp = [matrix[0][0]]
# dfs(0,0)

'''
獨眼怪走迷宮2 
dfs
'''

'''
堆疊版 dfs

'''
# def dfs_stack(i, j):
#     stack = [[i,j]]
#     path = []
#     while stack:
#         node = stack.pop()
#         if record[node[0]][node[1]] == 1:
#             continue 
#         record[node[0]][node[1]] = 1
#         print(matrix[node[0]][node[1]])
#         for d in dir:
#             i_next = node[0] + d[0]
#             j_next = node[1] + d[1]
#             if 0 <= i_next < n[0] and 0 <= j_next < n[1]:
#                 if record[i_next][j_next] == 0:
#                     # path.append(matrix[i_next][j_next]) 
#                     stack.append([i_next,j_next])
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# n = [len(matrix), len(matrix[0])]
# record = [[0]*3 for i in range(3)]
# #       下     右    上     左
# dir = [[1,0],[0,1],[-1,0],[0,-1]]
# dfs_stack(0,0)



# print("  ")
# def dfs(node):
#     print(matrix[node[0]][node[1]])
#     for d in dire[::-1]:
#         i_next = node[0] + d[0]
#         j_next = node[1] + d[1]
#         if 0 <= i_next < 3 and 0 <= j_next < 3:
#             if record[i_next][j_next] == 0:
#                 record[i_next][j_next] = 1
#                 dfs([i_next,j_next])

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# dire = [[1,0],[0,1],[-1,0],[0,-1]]
# record = [[0]*3 for i in range(3)]
# record[0][0] = 1
# dfs([0,0])  #node = [0,0]


# def dfs_stack(i,j):
#     record = [1]    #用來記錄你走過路
#     stack = [[i,j]]

#     while stack:
#         node = stack.pop()
#         print(matrix[node[0]][node[1]])
#         for d in dir:
#             next_i = node[0] + d[0]
#             next_j = node[1] + d[1]
#             if 0 <= next_i < n[0] and 0 <= next_j < n[1]  and matrix[next_i][next_j] not in record:
#                 stack.append([next_i,next_j])
#                 record.append(matrix[next_i][next_j])
               
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# n = [len(matrix), len(matrix[0])]
# #       下     右    上     左
# dir = [[1,0],[0,1],[-1,0],[0,-1]]

# dfs_stack(0,0)


# def dfs(node):
#     print(matrix[node[0]][node[1]])
#     for d in dire[::-1]:
#         i_next = node[0] + d[0]
#         j_next = node[1] + d[1]
#         if 0 <= i_next < 3 and 0 <= j_next < 3:
#             if record[i_next][j_next] == 0:
#                 record[i_next][j_next] = 1
#                 dfs([i_next,j_next])

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# dire = [[1,0],[0,1],[-1,0],[0,-1]]
# record = [[0]*3 for i in range(3)]
# record[0][0] = 1
# dfs([0,0])
'''
有發現哪裡怪怪的嗎?
1
2
3
6
9
8
7
5
4

1
2
3
6
5
4
7
8
9

why?
如何修改?
'''
# def dfs_stack(i,j):
#     record = []    #用來記錄你走過路
#     stack = [[i,j]]
#     temp = [matrix[i][j]]
#     while stack:
#         node = stack.pop()
#         del temp[-1]
#         if matrix[node[0]][node[1]] in record:
#             continue
#         record.append(matrix[node[0]][node[1]])
#         print(matrix[node[0]][node[1]])
#         for d in dir:
#             next_i = node[0] + d[0]
#             next_j = node[1] + d[1]
#             if 0 <= next_i < n[0] and 0 <= next_j < n[1]  and matrix[next_i][next_j] not in record:
#                 stack.append([next_i,next_j])
#                 temp.append(matrix[next_i][next_j])
#         # print(temp)
               
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# n = [len(matrix), len(matrix[0])]
# #       下     右    上     左
# dir = [[1,0],[0,1],[-1,0],[0,-1]]

# dfs_stack(0,0)

'''
獨眼怪走迷宮2 
bfs

'''




def bfs(i,j):
    queue = [[i,j]]
    path = [[0]*4 for i in range(5)]
    path[0][0] = 1
    ans = 0
    while queue:
        size = len(queue)

        while size != 0:
            node = queue.pop(0) #s
            
            print(matrix[node[0]][node[1]])
            for d in dire:
                i = node[0] + d[0]
                j = node[1] + d[1]
                if 0 <= i < 5 and 0 <= j < 4 and path[i][j] != 1:
                    if matrix[i][j] != "x":
                        path[i][j] = 1
                        queue.append([i,j])
            size -= 1
        ans += 1
matrix = [["s", 1 , 2 ,"x"],
           [ 3 ,"x", 4 , 5 ],
           [ 6 , 7 , 8 ,"x"],
           [ 9 ,"x", 10, 11],
           [ 12, 13, 14,'e']]
dire = [[1,0],[0,1],[-1,0],[0,-1]]

bfs(0,0)
'''
(1) 走訪所有的點
(2) 判斷兩點之間有沒有路徑
(3) 判斷兩點之間最短距離
缺點: 不好紀錄路徑 
'''




'''
練習題
apcs 樹狀圖分析  dfs/dfs_stack
https://zerojudge.tw/ShowProblem?problemid=c463


闖關路線 bfs
d094: Q-7-5. 闖關路線
https://judge.tcirc.tw/ShowProblem?problemid=d094
'''

from functools import cmp_to_key