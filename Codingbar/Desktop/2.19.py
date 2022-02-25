'''
圖的分類
(1) 有向圖
(2) 無向圖

樹的定義:
(1)edge == n - 1
(2)沒有環路
(3)兩點之間必有唯一一條路徑

圖的儲存方法
1. 鄰接矩陣 Adjacency List
2. 鄰接串列 Adjacency Matrix

1. 
    0   1   2   3   4   5
0   -1  1   1    
1   1           1   1
2   1                   1
3       1
4       1
5           1

matrix = [[0]*6 for i in range(6)]

2.
dic = {0:[1,2],1:[0,3,4],2:[0,5],3[1],4:[1],5:[2]}


'''
# matrix = [[-1]*6 for i in range(6)]
# print(matrix[0][5])
# print(matrix)


'''
dfs
有向圖

'''
# def dfs(node):  #2
#     print(node)
#     if node not in dic:
#         return

#     for i in dic[node]: #3,5
#         dfs(i)

# dic = {1:[2],2:[3,5],3:[4],5:[6,7],7:[8]}
# dfs(1)



# def dfs(node):
#     print(node)

#     if node not in dic: #O(1) 雜湊 HASH
#         return

#     for i in dic[node]:
#         dfs(i)

# dic = {0:[1,2],1:[3,4],2:[5]}

# # if 1 in [1,2,3,4]: #O(n)

# dfs(0)






# def dfs(node):
#     print(node)
#     if node not in dic:
#         return

#     for i in dic[node]:
#         dfs(i)


# dic = {1:[2,3],2:[4,5],3:[6,7]}

# dfs(1)

'''
dfs
無向圖

怎麼辦?
遇到無窮迴圈
原因
走過路沒有紀錄
'''
# def dfs(node):  #2
#     print(node)
#     input()
#     if node not in dic:
#         return

#     for i in dic[node]: #3,5
#         # if i not in record:     #判斷有沒有走過
#             # record.append(i)
#         if record[i] == 0:
#             record[i] = 1
#             dfs(i)
# # record = [0] #記錄走過的地方
# record = [0]*5  #初始直設 0 沒走過
# dic = {0:[1,2],1:[0,3,4],2:[0],3:[1],4:[1]}
# dfs(0)
'''
dfs 講義

'''
def dfs(node):
    print(matrix[node[0]][node[1]])
    for d in dire:
        i_next = node[0] + d[0]
        j_next = node[1] + d[1]
        if 0 <= i_next < 3 and 0 <= j_next < 3:
            if record[i_next][j_next] == 0:
                record[i_next][j_next] = 1
                dfs([i_next,j_next])

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
dire = [[1,0],[0,1],[-1,0],[0,-1]]
record = [[0]*3 for i in range(3)]
record[0][0] = 1
dfs([0,0])
'''
1.dfs 搜索所有點


'''
# from re import L


# def dfs(i,j):
#     print(matrix[i][j])
#     for x in direction:
#         now_i = i + x[0]
#         now_j = j + x[1]
#         if 0 <= now_i < n and 0 <= now_j < n:
#             if path[now_i][now_j] != 1:  #最糟糕的時間複雜度:
#                 path[now_i][now_j] = 1
#                 dfs(now_i,now_j)
#                 # del record[-1]
#                 # path[now_i][now_j] = 0
# n = 3
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9],]
# record = [1]
# path = [[0]*3 for i in range(3)]
# direction = [[1,0],[0,1],[-1,0],[0,-1]]
# dfs(0,0)



'''
獨眼怪走迷宮 1

'''

# def dfs_stack(i,j):
#     stack = [[0,0]]
#     stack2 = [0]
#     path = []

#     while stack:
#         node = stack.pop()
#         if matrix[node[0]][node[1]] in path:
#             break
#         path.append(matrix[node[0]][node[1]])
#         del stack2[-1]
#         for x in dire[::-1]:
#             i_next = node[0] + x[0]
#             j_next = node[1] + x[1]
#             if 0 <= i_next < 3 and 0 <= j_next < 3 and matrix[i_next][j_next] not in path:
#                 stack.append([i_next,j_next])
#                 stack2.append(matrix[i_next][j_next])
#                 # path.append(matrix[i_next][j_next])
#         print(matrix[node[0]][node[1]])
#         print(path)
#         print(stack2)
                
# dire = [[1,0],[0,1],[-1,0],[0,-1]]

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# dfs_stack(0,0)


# def dfs_stack(i, j):
#     queue = [[0, 0]]
#     path[0][0] = 1
#     count = 0
#     while queue:
#         size = len(queue)
#         while size != 0:
#             node = queue.pop(0)
#             if matrix[node[0]][node[1]] == "E":
#                 print(count)
#                 return
#             # if node[0] == 3 and node[1] 30== 3:
#             #     print(count)
#             #     return
#             for x in dire:
#                 i_next = node[0] + x[0]
#                 j_next = node[1] + x[1]
#                 if 0 <= i_next < n and 0 <= j_next < n and path[i_next][j_next] == 0:
#                     if matrix2[i_next][j_next] != "x":
#                         queue.append([i_next, j_next])
#                         path[i_next][j_next] = 1
#             size -= 1
#         count += 1




'''
2.dfs 搜索所有的路徑


'''
def dfs(node):
    print(temp)
    for d in dire:
        i_next = node[0] + d[0]
        j_next = node[1] + d[1]
        if 0 <= i_next < 3 and 0 <= j_next < 3:
            if record[i_next][j_next] == 0:
                record[i_next][j_next] = 1
                temp.append(matrix[i_next][j_next])
                dfs([i_next,j_next])    #dfs(5)
                record[i_next][j_next] = 0
                del temp[-1]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
dire = [[1,0],[0,1],[-1,0],[0,-1]]
record = [[0]*3 for i in range(3)]
record[0][0] = 1
temp = [1]  #紀錄目前走的路線
dfs([0,0])
'''
dfs 搜索最短路徑 + 最短路徑距離
matrix3 = [["s", 1 , 2 ,"x"],
           [ 3 ,"x", 4 , 5 ],
           [ 6 , 7 , 8 ,"x"],
           [ 9 ,"x", 10, 11]
           [ 12, 13, 14,'e']]

最短路徑距離
6
所有最短路徑 
[[s,5,6,7,9,10,e],[s,5,6,8,9,10,e]]
global c 

'''
# dfs搜索最短路徑距離
# matrix3 = [["s", 1 , 1 ,"x"],
#            [ 1 ,"x", 1 , 1 ],
#            [ 1 , 1 ,"x","x"],
#            [ 1 , 1 , 1 , "E"]]

def dfs(i,j):
    print("索引值",i,j)
    if matrix1[i][j] == "e":
        print(matrix1[i][j])
        
        print(len(temp),temp)
    # input()

    for x in dir:
        now_i = i + x[0]
        now_j = j + x[1]
        # print(matrix1[now_i][now_j])
        if 0 <= now_i < 5 and 0 <= now_j < 4:
            # print(matrix1[now_i][now_j])
            if matrix1[now_i][now_j] not in record and matrix1[now_i][now_j] != "x":
                record.append(matrix1[now_i][now_j])    #紀錄
                temp.append(matrix1[now_i][now_j])
                dfs(now_i,now_j)    #走這條路
                del record[-1]
                del temp[-1]

# matrix1 = [['s',   1, 'x', 'x',   2,   3,   4,   5,   6,   7],
#           ['x',   8,   9,  10, 'x', 'x',  11, 'x', 'x',  12],
#           ['x', 'x', 'x',  13,  14, 'x',  15, 'x',  16,  17],
#           ['x', 'x', 'x', 'x',  18, 'x',  19, 'x',  20, 'x'],
#           [ 21,  22,  23,  24,  25,  26,  27, 'x',  28,  29],
#           ['x',  30, 'x', 'x', 'x', 'x', 'x', 'x',  31, 'x'],
#           ['x',  32, 'x',  33, 'x', 'x',  34,  35,  36, 'x'],
#           [ 37,  38,  39,  40,  41,  42,  43, 'x',  44, 'x'],
#           ['x',  45, 'x', 'x', 'x', 'x', 'x', 'x',  46, 'x'],
#           ['x',  47,  48,  49,  50,  51,  52,  53,  54, 'e']]

matrix1 = [["s", 1 , 2 ,"x"],
           [ 3 ,"x", 4 , 5 ],
           [ 6 , 7 , 8 ,"x"],
           [ 9 ,"x", 10, 11],
           [ 12, 13, 14,'e']]
record = ["s"]    #用來記錄你走過路
#       下     右    上     左
dir = [[1,0],[0,1],[-1,0],[0,-1]]
temp = [matrix1[0][0]]
dfs(0,0)


'''
4.bfs 搜索所有點
'''
# def bfs(i,j):
#     queue = [[0,0]]
#     path = [[0]*4 for i in range(4)]
#     path[0][0] = 1
#     while queue:    
#         node = queue.pop(0) #=> #temp = queue[0]， del queue[0]
#         print(node)
#         for x in dire:
#             now_i = node[0] + x[0]
#             now_j = node[1] + x[1]
#             if 0 <= now_i < 4 and 0 <= now_j < 4:
#                 if matrix3[now_i][now_j] != "x":
#                     if path[now_i][now_j] != 1:
#                         path[now_i][now_j] = 1
#                         queue.append([now_i,now_j])

# matrix3 = [["s", 1 , 1 ,"x"],
#            [ 1 ,"x", 1 , 1 ],
#            [ 1 , 1 ,"x","x"],
#            [ 1 , 1 , 1 , "E"]]
# dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# bfs(0,0)

'''
相鄰領地
DFS/BFS
'''


'''
皮卡丘逃亡記
DFS/BFS
'''

'''
5.bfs 搜索最短路徑距離

'''
# def bfs(i,j):
#     queue = [[0,0]]
#     path = [[0]*4 for i in range(4)]
#     path[0][0] = 1
#     count = 0   #距離
#     while queue:    
#         size = len(queue)   #當前的要找的點的數目
#         print("s",size)
#         while size != 0:
#             node = queue.pop(0) #=> #temp = queue[0]， del queue[0]
#             if matrix3[node[0]][node[1]] == "E":
#                 print(count)
#             print(node)
#             for x in dire:  #node的所有點 [2,3 ,4,5]
#                 now_i = node[0] + x[0]
#                 now_j = node[1] + x[1]
#                 if 0 <= now_i < 4 and 0 <= now_j < 4:
#                     if matrix3[now_i][now_j] != "x":
#                         if path[now_i][now_j] != 1:
#                             path[now_i][now_j] = 1
#                             queue.append([now_i,now_j])
#             size -= 1
#         count += 1
#     # print(count)
# matrix3 = [["s", 1 , 1 ,"x"],
#            [ 1 ,"x", 1 , 1 ],
#            [ 1 , 1 ,"x","x"],
#            [ 1 , 1 , 1 , "E"]]
# dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]
# bfs(0,0)


'''
1. 路徑
    dfs
2. 兩點之間有沒有路徑 最短路徑距離 
     dfs/bfs            bfs

'''



# matrix2 = [["s", 1, 1, "x", 1, 1],
#           [1, "x", 1, "x", 1, "x"],
#           [1, 1, "x", 1, 1, 1],
#           ["x", 1, 1, 1, "x", 1],
#           [1, 1, "x", 1, "x", 1],
#           [1, "x", 1, 1, "x", "E"]]

# matrix3 = [["s", 1 , 1 ,"x"],
#            [ 1 ,"x", 1 , 1 ],
#            [ 1 , 1 ,"x","x"],
#            [ 1 , 1 , 1 , "E"]]

# path = [[0]*4 for i in range(4)]
# path2 = [[0]*6 for i in range(6)]


# dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# count = 0
# path[0][0] = 1
# ans = 10**9
# record2 = [[0,0]]
# ans_list = []
# bfs(0,0)
# print(record2)
# print(ans_list,ans)

