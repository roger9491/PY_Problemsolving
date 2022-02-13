'''
使用遞迴 掃描一維矩陣，並印出來
'''
# def rec(index):
#     if index == len(a) or a[index] == "x":
#         return
#     print(a[index])
#     rec(index + 1)

# a = input().split()
# rec(0)


'''
如果是二維呢?
輸入 n 
接下來輸入 n 列 ， 每列 n 個數字

掃描二維矩陣，並印出來 
'''
# def rec2(y,x):
#     if x == n:
#         if y < n - 1:
#             x = 0
#             y += 1
#         else:
#             return
#     print(t[y][x])
#     rec2(y,x+1)
# t = []
# n = int(input())
# for i in range(n):
#     a = input().split()
#     t.append(a)
# rec2(0,0)


# def dfs_stack(x,y):
#     stack = [[x,y]]
#     path = [matrix[x][y]]

#     while stack:
#         now = stack.pop()
#         for d in dire:
#             i_next = now[0] + d[0]
#             j_next = now[1] + d[1]
#             if 0 <= i_next < n and 0 <= j_next < n and matrix[i_next][j_next] not in path:
#                 if matrix[i_next][j_next] == matrix[-1][-1]:
#                     print("run away")
#                     break
#                 stack.append([i_next,j_next])
#                 path.append(matrix[i_next][j_next])





# n = int(input())

# matrix = []
# for i in range(n):
#     e = input().split()
#     matrix.append(e)

# dire = [[1,0],[0,1],[-1,0],[0,-1]]

# dfs_stack(0,0)

'''
DFS 搜索所有點

s


'''
def dfs(i,j):
    print(matrix[i][j])
    if matrix[i][j] == 9:
        return
    for x in direction:
        now_i = i + x[0]
        now_j = j + x[1]
        if 0 <= now_i < n and 0 <= now_j < n:
            # if path[now_i][now_j] != 1:  #最糟糕的時間複雜度:
            #     path[now_i][now_j] = 1
            dfs(now_i,now_j)
                # del record[-1]
                # path[now_i][now_j] = 0
n = 3
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],]
record = [1]
path = [[0]*3 for i in range(3)]
direction = [[1,0],[0,1],[-1,0],[0,-1]]
dfs(0,0)
'''
判斷一個值有沒有在串列 in 
'''
# a = []
# b = "1"
# for i in range(len(a)): #最糟糕的 n 次 O(n)  ->   O(1)
#     if b == a[i]:
#         print("找到")
#         break




# def dfs_stack(i,j):
#     stack = [[0,0]]
#     path = [1]

#     while stack:
#         node = stack.pop()
#         print(matrix[node[0]][node[1]])
        
#         for x in dire:
#             i_next = node[0] + x[0]
#             j_next = node[1] + x[1]
#             if 0 <= i_next < 3 and 0 <= j_next < 3 and matrix[i_next][j_next] not in path:
#                 stack.append([i_next,j_next])
#                 path.append(matrix[i_next][j_next])
                
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
1.dfs 搜索所有點


'''

'''
2.dfs 搜索最短路徑距離

'''
# def dfs(i,j):
#     global count
#     global ans
#     global ans_list
#     print(record2)
#     if matrix3[i][j] == "E":
#         if count <= ans:
#             print("xxx")
#             print(record2)
#             input()
#             ans = count
#             ans_list.append(record2.copy())

#     for x in dire:
#         now_i = i + x[0]
#         now_j = j + x[1]
#         if 0 <= now_i < 4 and 0 <= now_j < 4:
#             if path[now_i][now_j] != 1 and matrix3[now_i][now_j] != "x":
#                 path[now_i][now_j] = 1
#                 count += 1
#                 record2.append([now_i,now_j])
#                 dfs(now_i,now_j)
#                 del record2[-1]
#                 path[now_i][now_j] = 0
#                 count -= 1
'''
1.dfs 搜索所有點

'''
# def dfs(i,j):
#     print("索引值",i,j)
#     print(matrix1[i][j])
#     print(record)
#     # input()

#     for x in dir:
#         now_i = i + x[0]
#         now_j = j + x[1]
#         if 0 <= now_i < 3 and 0 <= now_j < 3:
#             if matrix1[now_i][now_j] not in record:
#                 record.append(matrix1[now_i][now_j])    #紀錄
#                 dfs(now_i,now_j)    #走這條路

# matrix1 = [[1,2,3],
#            [4,5,6],
#            [7,8,9],]
# record = [1]    #用來記錄你走過路
# #       下     右    上     左
# dir = [[1,0],[0,1],[-1,0],[0,-1]]
# dfs(0,0)


'''
3.dfs 搜索所有的路徑


'''
# def dfs(i,j):
#     print("索引值",i,j)
#     print(matrix1[i][j])
#     print(record)
#     # input()

#     for x in dir:
#         now_i = i + x[0]
#         now_j = j + x[1]
#         if 0 <= now_i < 3 and 0 <= now_j < 3:
#             if matrix1[now_i][now_j] not in record:
#                 record.append(matrix1[now_i][now_j])    #紀錄
#                 dfs(now_i,now_j)    #走這條路
#                 del record[-1]

# matrix1 = [[1,2,3],
#            [4,5,6],
#            [7,8,9],]
# record = [1]    #用來記錄你走過路
# #       下     右    上     左
# dir = [[1,0],[0,1],[-1,0],[0,-1]]
# dfs(0,0)
'''
dfs 搜索最短路徑 + 最短路徑距離
matrix3 = [["s", 1 , 1 ,"x"],
           [ 1 ,"x", 1 , 1 ],
           [ 1 , 1 ,"x","x"],
           [ 1 , 1 , 1 , "E"]]

最短路徑距離
6
所有最短路徑 
[[s,5,6,7,9,10,e],[s,5,6,8,9,10,e]]
global c 

'''
#dfs搜索最短路徑距離
# matrix3 = [["s", 1 , 1 ,"x"],
#            [ 1 ,"x", 1 , 1 ],
#            [ 1 , 1 ,"x","x"],
#            [ 1 , 1 , 1 , "E"]]

# def dfs(i,j):
#     # print("索引值",i,j)
#     # print(matrix3[i][j])
#     # print(record)
#     O=matrix3[i][j] #original 
#     for x in dir:
#         now_i = i + x[0]
#         now_j = j + x[1]
#         if 0 <= now_i < len(matrix3) and 0 <= now_j < len(matrix3):
#             if matrix3[now_i][now_j]=="E":
#                 print("ANS")
#                 ans_list.append([len(record),record.copy()])
#                 print(ans_list)
#                 return
#             if matrix3[now_i][now_j]!="x":
#                 if [now_i,now_j] not in record:
#                     record.append([now_i,now_j])    #紀錄
#                     dfs(now_i,now_j)    #走這條路
#                     del record[-1]
                    

# record = [[0,0]]    #用來記錄你走過路
# #       下     右    上     左
# dir = [[1,0],[0,1],[-1,0],[0,-1]]
# ans_list = []

# dfs(0,0)
# print("aa",ans_list)
# ans_list.sort()
# temp = 10**9
# for x in ans_list:
#     if x[0] <= temp:
#         temp = x[0]
#         print("temp",temp)
#         print("list",x[1])
#     else:
#         break

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
# def bfs(i,j):
#     queue = [[i,j]]
#     ans = 10**9
#     ans_list = []
#     count = 0
#     while queue:
#         size = len(queue)
#         while size != 0:
#             node = queue.pop(0)
#             print(node,count,size)
#             print(queue)
#             if matrix3[node[0]][node[1]] == "E":
#                 ans = count
#                 print("ans",ans)
            
#             for x in dire:
#                 now_i = node[0] + x[0]
#                 now_j = node[1] + x[1]
#                 if 0 <= now_i < 4 and 0 <= now_j < 4:
#                     if path[now_i][now_j] != 1 and matrix3[now_i][now_j] != "x":
#                         path[now_i][now_j] = 1
#                         queue.append([now_i,now_j])
#             size -= 1
#         count += 1




# matrix1 = [[1,2,3],
#           [4,5,6],
#           [7,8,9],]
# record = [1]


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