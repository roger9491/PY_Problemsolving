
# def isprime(x):
#     for i in range(2,x):
#         if (x%i)==0:
#             return 2
#     else:
#         return 1
# #最長路徑為k
# def run(x):
#     global k,total
#     lit.append(x)
#     #print(lit)
#     if len(lit)==k:
#         #print(1)
#         if isprime(sum(lit))==1:
#             #print(lit)
#             total+=1
#         else:
#             pass
#         return
#     record[x]=1
#     for i in dic[x]:
#         if record[i]!=1:
#             run(i)
#             del lit[-1]
# p=list(map(int,input().split()))
# k=p[1]
# n=p[0]
# inf=list(map(int,input().split()))
# dic={}
# record={}
# lit=[]
# for i in range(len(inf)):
#     n=inf.copy()
#     del n[i]
#     dic[inf[i]]=n
#     record[inf[i]]=0
# total=0
# for i in range(len(inf)):
#     run(inf[i])
# print(total)


'''
獨眼怪走迷宮2 
dfs
'''

'''
遞迴 的原理
stack
遞迴 就是藉由呼叫自己來解決問題
你的原問題和子問題性質是一樣的

'''
# def f(n): #2  
#     print(n)
#     record.append(n)
#     total = 0
#     for i in dic[n]:    #3 4
#         if i not in record:
#             total += f(i)    #3
#     ans

# record = []
# f(0)
# def dfs(i,j):
#     stack = [[i,j]]
#     path = [matrix[i][j]]
    
#     while stack:
#         now = stack.pop()
#         if matrix[now[0]][now[1]] in path:
#             continue
#         path.append(matrix[now[0]][now[1]])

#         for d in dire:
#             i_next = now[0] + d[0]
#             j_next = now[1] + d[1]
#             if 0 <= i_next < 3 and 0 <= j_next < 3:
#                 if matrix[i_next][j_next] not in path:
#                     stack.append([i_next,j_next])
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# dire = [[1,0],[0,1],[-1,0],[0,-1]]

# dfs(0,0)
# print()
# def f(a):
#     print(a)
#     if a == 10000:
#         return
#     f(a+1)
# f(0)


# def dfs(n):
#     print(matrix[n[0]][n[1]])
#     #迭代子節點
#     for d in dire[::-1]:
#         i = n[0] + d[0]
#         j = n[1] + d[1]
#         if 0 <= i < 3 and 0 <= j < 3:
#             if record[i][j] == 0:
#                 #確定要走這個點
#                 record[i][j] = 1
#                 dfs([i,j])
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]] 
# record = [[0]*3 for i in range(3)]
# record[0][0] = 1
# dire = [[1,0],[0,1],[-1,0],[0,-1]]
# dfs([0,0])


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
bfs 廣度優先搜索

核心思想 : 擴散


dict={0:[2,3],2:[10],3:[4,5],5:[6]}
承上題 印出 0 到 葉節點的路徑
'''
dic = {0:[2,3],2:[1,10],3:[4,5],5:[6],10:[9,11]}

record = []
for i in dic[0]:
    record.append(i)
while len(record)!=0:
    print(record)
    for i in dic[record[0]]:
        record.append(i)
    print(record[0])
    record.pop(0)












'''
獨眼怪走迷宮2 
bfs

'''




# def bfs(i,j):
#     queue = [[i,j]]
#     path = [[0]*4 for i in range(5)]
#     path[0][0] = 1
#     ans = 0
#     while queue:
#         size = len(queue)

#         while size != 0:
#             node = queue.pop(0) #s
            
#             print(matrix[node[0]][node[1]])
#             for d in dire:
#                 i = node[0] + d[0]
#                 j = node[1] + d[1]
#                 if 0 <= i < 5 and 0 <= j < 4 and path[i][j] != 1:
#                     if matrix[i][j] != "x":
#                         path[i][j] = 1
#                         queue.append([i,j])
#             size -= 1
#         ans += 1
# matrix = [["s", 1 , 2 ,"x"],
#            [ 3 ,"x", 4 , 5 ],
#            [ 6 , 7 , 8 ,"x"],
#            [ 9 ,"x", 10, 11],
#            [ 12, 13, 14,'e']]
# dire = [[1,0],[0,1],[-1,0],[0,-1]]

# bfs(0,0)
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