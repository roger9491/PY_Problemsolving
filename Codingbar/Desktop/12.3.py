



'''
4.bfs 搜索所有點

'''
# def bfs(i, j):
#     queue = [[i, j]]    #準備要查誰的附近節點
#     record = [[0]*len(matrix[0]) for i in range(len(matrix))]

#     while queue:
#         node = queue.pop(0)
#         print(matrix[node[0]][node[1]])

#         # 尋找子節點
#         for x in dir:
#             i_next = node[0] + x[0]
#             j_next = node[1] + x[1]
#             # 判斷子節點的座標 在範圍裡
#             if 0 <= i_next < len(matrix) and 0 <= j_next < len(matrix[0]):
#                 if matrix[i_next][j_next] != "x" and record[i_next][j_next] == 0:
#                     queue.append([i_next, j_next])
#                     record[i_next][j_next] = 1

# #       上        下      左     右
# dir = [[-1,0], [1,0], [0,-1], [0,1]]
# matrix = [ ["s", 1 , 2 ,"x"],
#            [ 3 ,"x", 4 , 5 ],
#            [ 6 , 7 , "x" ,"x"],
#            [ 8 , 9 , 10, "e"],]
# bfs(0,0)


# a = [1,2]
# print(*a)






# def bfs(i,j):
#     queue = [[i,j]]
#     record = [[0]*4 for i in range(5)]
#     record[0][0] = 1
#     dire = [[-1,0], [1,0], [0,-1], [0,1]]

#     while queue:
#         node = queue.pop(0)
#         print(matrix[node[0]][node[1]])
#         for x in dire:
#             i = node[0] + x[0]      #周圍的節點座標
#             j = node[1] + x[1]
#             if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):    #判斷座標合理性
#                 if record[i][j] == 0 and matrix[i][j] != "x":
#                     queue.append([i,j])
#                     record[i][j] = 1


# #       上        下      左     右
# # i,j = [-1,0], [1,0], [0,-1], [0,1]
# matrix = [ ["s", 1 , 2 ,"x"],
#            [ 3 ,"x", 4 , 5 ],
#            [ 6 , 7 , 8 ,"x"],
#            [ 9 ,"x", 10, 11],
#            [ 12, 13, 14,'e']]
# bfs(0,0)








'''
最短距離
兩點之間的最短"距離"



'''



# matrix = [["s", 1 , 2 ,"x"],
#            [ 3 ,"x", 4 , 5 ],
#            [ 6 , 7 , 8 ,"x"],
#            [ 9 ,"x", 10, 11],
#            [ 12, 13, 14,'e']]

# def bfs(i,j):
#     queue = [[i,j]]
#     path = [[0]*4 for i in range(5)]
#     path[0][0] = 1
#     ans = 0
#     while queue:
#         size = len(queue)   # 1

#         while size != 0:    # 前一波的節點找完 步數才能加1
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
#         ans += 1    #步數
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

闖關路線 bfs
d094: Q-7-5. 闖關路線
https://judge.tcirc.tw/ShowProblem?problemid=d094
'''


'''
dfs : 深度優先搜尋

真的模仿我們走路情況


解決的問題

(1) 兩點之間有沒有路徑
(2) 走完所有的點


遞迴
    函式 呼叫自己
'''

# def a(c):
#     c += 1
#     print(c)
#     if c > 3:
#         return
#     a(c)
#     print(c)
# a(0)
'''

印出 0 ~ 10 間格為2

0
2
4
6
8
10

'''
# def s(n):
#     print(n)
#     n+=2
#     if n>10:
#         return
#     s(n)
# s(0)



# def a(n):
#     print(n)
#     if n > 99:  #邊界值
#         return
#     a(n+1)
# a(5)


'''
用遞迴
1 + 2 + .. +  100


(1) 邊界值 n == 1 return n
(2) 遞迴關係式
    原本的問題 和 比自己小的問題 之間的關係
a(n): 1+..+ n
a(2): 1+2
a(3): 1 + 2 + 3
a(4): 1 + 2 + 3 + 4
a(4) = a(3) + 4
a(5) = a(4) + 5
a(n) = a(n-1) + n 遞迴關係式


1 + 2 + 3 + 4 + 5   5階
1 + 2 + 3 + 4   4階

f(5): 回傳 5階
f(4): 回傳 4階

f(5) = f(4) + 5
f(4) = f(3) + 4
f(3) = f(2) + 3
f(2) = f(1) + 2
f(1) = 1

f(n) = f(n-1) + n

if n == 1 return 1
'''
# def f(n):   #5
#     if n == 1:
#         return 1
#     return f(n-1) + n
# print(f(5))







# def a(n):
#     if n == 1:    #邊界值
#         return n
#     return a(n-1) + n
# print(a(5))
# def a(n):
#     if n == 1:
#         return n
#     return a(n-1) + n
# print(a(100))

'''
輸入一個數字 n
用遞迴 1+ ..+n
中間要印出過程
最後印出 1+ ..+n 結果

5

1
3
6
10
15
15
'''
# def a(n):
#     if n==1:

#         return n
#     c=a(n-1)+n
#     print(c)
#     return c

# n=int(input())
# a(n)



# def a(n):
#     if n == n1:
#         return n
#     return a(n+1) + n
# n1 = int(input())
# print(a(1))



'''
dfs 深度優先搜索

核心思想 : 模仿人類走路

dict={0:[2,3],2:[10],3:[4,5],5:[6]}
遍歷所有的點
'''

# dict={0:[2,3],2:[10],3:[4,5],5:[6]}
# def a(n):   #a(0)   a(3)
#     print(n)
#     if n not in dict:
#         return
#     else:
#         for i in dict[n]:#2,3
#             a(i)    #a(3)

# a(0)

'''
dfs 深度優先搜索

核心思想 : 模仿人類走路


dict={0:[2,3],2:[10],3:[4,5],5:[6]}
承上題 印出 0 到 葉節點的路徑
'''
# dic = {0:[2,3],2:[10],3:[4,5],5:[6]}

# def f(n):
#     temp.append(n)
#     if n not in dic:
#         print(temp)
#         return
#     else:
#         for i in dic[n]:
#             f(i)
#             del temp[-1]
        
# temp = []
# f(0)
# print(temp)
'''
有向圖

改無向圖
遍歷

dict={0:[2,3],2:[10],3:[4,5],5:[6],2:[10,0]}
'''

# dic = {0:[2,3],2:[0,10],3:[4,5],5:[3,6],10:[2],4:[3],6:[5]}

# def f(n):   #0  2
#     print(n)
#     record.append(n)
#     for i in dic[n]:    #2,3    0,10
#         if i not in record:
#             f(i)    
# record = []
# f(0)



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


# import sys	#必須先匯入sys
# for i in sys.stdin: #無限的輸入
#     n = int(i)
#     for i in range(n):
#         a = sys.stdin.readline().strip()
#         print(a)