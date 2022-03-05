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
def dfs_stack(i,j):
    stack = [[0,0]]     #初始位置
    path = [[0]*n for i in range(n)]   #記錄走過的

    while stack:
        node = stack.pop()
                #當前節點的值       等於  最後一個點的值
        if matrix[node[0]][node[1]] == matrix[-1][-1]:
            print("run away")
            return
        # print(matrix[node[0]][node[1]])
        if matrix[node[0]][node[1]] in path:
            continue
        # path.append(matrix[node[0]][node[1]])
        path[node[0]][node[1]] = 1
        for x in dire:
            i_next = node[0] + x[0]
            j_next = node[1] + x[1]
            # if 0 <= i_next < n and 0 <= j_next < n and matrix[i_next][j_next] not in path:
            if 0 <= i_next < n and 0 <= j_next < n and path[i_next][j_next] == 0:
                if matrix[i_next][j_next] != "x":
                    stack.append([i_next,j_next])


n = int(input())

matrix = []
for i in range(n):
    e = input().split()
    matrix.append(e)

dire = [[1,0],[0,1],[-1,0],[0,-1]]

dfs_stack(0,0)

'''
08. 相鄰領地

'''

def bfs(i,j):
    queue = [[i,j]]
    path[i][j] = 1
    count = 0
    direction = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
    while queue:
        node = queue.pop(0)
        count += 1
        for r in direction:
            i_next = node[0] + r[0]
            j_next = node[1] + r[1]
            if 0 <= i_next < n and 0 <= j_next < m:
                if matrix[i_next][j_next] == 0 and path[i_next][j_next] == 0:
                    queue.append([i_next,j_next])
                    path[i_next][j_next] = 1
    return count


m,n = map(int,input().split())

matrix = []
for i in range(n):
    e = list(map(int,input().split()))
    matrix.append(e)


path = [[0]*m for i in range(n)]
ans = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 and path[i][j] == 0:
            ans.append(bfs(i,j))

ans.sort()
ans = list(map(str,ans))
print(" ".join(ans))

'''
12. 皮卡丘逃亡記
'''

def bfs(i,j):
    queue = [[i,j]]
    path[i][j] = 1
    flag1 = False   #鑰匙
    flag2 = False   #出口
    
    while queue:
        node = queue.pop(0)
        if node[0] == y and node[1] == x:
            flag1 = True
        if node[0] == n-1 and node[1] == n-1:
            flag2 = True

        for r in direction:
            i_next = node[0] + r[0]
            j_next = node[1] + r[1]
            if 0 <= i_next < n and 0 <= j_next < n:
                if matrix[i_next][j_next] == 'o' and path[i_next][j_next] == 0:
                    queue.append([i_next,j_next])
                    path[i_next][j_next] = 1
    if flag1 and flag2:
        return True
    else:
        return False


n = int(input())

matrix = []
for i in range(n):
    e = input()
    matrix.append(e)

x,y = map(int,input().split())

direction = [[1,0],[0,1],[-1,0],[0,-1]]
path = [[0]*n for i in range(n)]

print(bfs(0,0))



'''
練習題
apcs 樹狀圖分析  dfs/dfs_stack
https://zerojudge.tw/ShowProblem?problemid=c463


闖關路線 bfs
d094: Q-7-5. 闖關路線
'''