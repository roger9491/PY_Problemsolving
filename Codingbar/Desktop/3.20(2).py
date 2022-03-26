'''


'''
# dict={}
# repeat=[]
# for i in range(12):
#     a=list(map(int,input().split()))
#     if a[0]not in dict :
#         dict[a[0]]=list()
#         dict[a[0]].append(a[1])
#     else:
#         dict[a[0]].append(a[1])
#     if a[1]not in dict:
#         dict[a[1]]=list()
#         dict[a[1]].append(a[0])
#     else:
#         dict[a[1]].append(a[0])

# def a(n):
#     if n not in dict:
#         return
#     else:
#         print(n)
#         repeat.append(n)
#         for i in dict[n]:
#             if i in repeat:
#                 continue
#             else:
#                 a(i)
# a(0)


# def dfs(n):
#     print(matrix[n[0]][n[1]])
#     #迭代子節點
#     for d in dire:
#         i = n[0] + d[0]
#         j = n[1] + d[1]
#         if 0 <= i < 3 and 0 <= j < 3:
#             if record[i][j] == 0:
#                 #確定要走這個點
#                 record[i][j] = 1
#                 dfs([i,j])
# # matrix = [[0,1,2],
# #           [3,4,5],
# #           [6,7,8]] 
# matrix = [["s", 1 , 2 ,"x"],
#            [ 3 ,"x", 4 , 5 ],
#            [ 6 , 7 , 8 ,"x"],
#            [ 9 ,"x", 10, 11],
#            [ 12, 13, 14,'e']]
# # record = [0]*9
# # record[0] = 1
# record = [[0]*3 for i in range(3)]
# record[0][0] = 1
# dire = [[1,0],[0,1],[-1,0],[0,-1]]
# dfs([0,0])





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
dfs

python link-list

'''


'''
2.dfs 搜索所有的路徑


'''
def dfs(node):
    print(temp)
    # print(matrix[node[0]][node[1]])
    for d in dire:
        i_next = node[0] + d[0]
        j_next = node[1] + d[1]
        if 0 <= i_next < 3 and 0 <= j_next < 3:
            if record[i_next][j_next] == 0:
                record[i_next][j_next] = 1
                temp.append(matrix[i_next][j_next])
                dfs([i_next,j_next])    #dfs(5)
                # record[i_next][j_next] = 0
                # del temp[-1]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# matrix  = [["s", 1 , 2 ,"x"],
#            [ 3 ,"x", 4 , 5 ],
#            [ 6 , 7 , 8 ,"x"],
#            [ 9 ,"x", 10, 11],
#            [ 12, 13, 14,'e']]
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
           [ 9 ,"x", 10, 11],
           [ 12, 13, 14,'e']]


最短路徑距離
6
所有最短路徑 
[[s,5,6,7,9,10,e],[s,5,6,8,9,10,e]]
global c 

'''
# def f(n):
#     print(n)
#     n += 1
#     f(n)
# f(0)


'''

遞迴原理
用stack來實現

'''
def f(n):
    print(n)
    if n == 5:
        return
    n += 1
    f(n)
    print("x")
f(0)




# dfs搜索最短路徑距離
# matrix3 = [["s", 1 , 1 ,"x"],
#            [ 1 ,"x", 1 , 1 ],
#            [ 1 , 1 ,"x","x"],
#            [ 1 , 1 , 1 , "E"]]

# def dfs(i,j):
#     print("索引值",i,j)
#     if matrix1[i][j] == "e":
#         print(matrix1[i][j])
        
#         print(len(temp),temp)
#     # input()

#     for x in dir:
#         now_i = i + x[0]
#         now_j = j + x[1]
#         # print(matrix1[now_i][now_j])
#         if 0 <= now_i < 5 and 0 <= now_j < 4:
#             # print(matrix1[now_i][now_j])
#             if matrix1[now_i][now_j] not in record and matrix1[now_i][now_j] != "x":
#                 record.append(matrix1[now_i][now_j])    #紀錄
#                 temp.append(matrix1[now_i][now_j])
#                 dfs(now_i,now_j)    #走這條路
#                 del record[-1]
#                 del temp[-1]

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

# matrix1 = [["s", 1 , 2 ,"x"],
#            [ 3 ,"x", 4 , 5 ],
#            [ 6 , 7 , 8 ,"x"],
#            [ 9 ,"x", 10, 11],
#            [ 12, 13, 14,'e']]
# record = ["s"]    #用來記錄你走過路
# #       下     右    上     左
# dir = [[1,0],[0,1],[-1,0],[0,-1]]
# temp = [matrix1[0][0]]
# dfs(0,0)


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

