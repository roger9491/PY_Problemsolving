'''
bfs 廣度優先搜索

核心思想 : 擴散


dict={0:[2,3],2:[10],3:[4,5],5:[6],8:[9]}

'''
# dic : 字典 {key:value}
# if a in dic:


# dic={0:[2,3],2:[10],3:[4,5],5:[6],8:[9]}

# queue = [0] #看誰的周圍

# while queue:    #當所有的點看完時，queue就空了
#     node = queue.pop(0)     #刪除索引值0，並傳出
#     print(node)

#     if node in dic:
#         for i in dic[node]:
#             queue.append(i)

# dic = {0:[2,3],2:[1,10],3:[4,5],5:[6],10:[9,11]}
# a = [0]
# while True:
#     if len(a) == 0:
#         break
#     if a[0] in dic:
#         for i in dic[a[0]]:
#             a.append(i)
#     v = a.pop(0)
#     print(v)





# dic = {0:[2,3],2:[1,10],3:[4,5],5:[6],10:[9,11]}

# queue = [0]

# while queue:
#     node = queue.pop(0)
#     print(node)

#     if node in dic:
#         for i in dic[node]:
#             queue.append(i)

'''

輸入 n，代表接下來n個輸入
輸入 兩個數字 代表節點相連

輸出
所有0能連通的節點

ex
9
0 2
0 3
2 1
2 10
10 9
10 11
3 4
3 5
5 6
'''

# n = int(input())
# dic = {}
# for i in range(n):
#     c = list(map(int,input().split()))
#     a = c[0]
#     b = c[1]
#     if a in dic:
#         dic[a].append(b)
#     else:
#         dic[a] = [b]
    
#     if b in dic:
#         dic[b].append(a)
#     else:
#         dic[b] = [a]

# a = [0]
# x = []
# while True:
#     if len(a) == 0:
#         break
#     if a[0] in dic:
#         for i in dic[a[0]]:
#             if i not in x:  #判斷i有沒有走過
#                 a.append(i)
#     v = a.pop(0)
#     print(v)
#     x.append(v)

'''
優化判斷 i 有沒有走過
利用索引值取值的方式
索引值:節點
值: 有 沒有
'''
# n = int(input())
# dic = {}
# for i in range(n):
#     c = list(map(int,input().split()))
#     a = c[0]
#     b = c[1]
#     if a in dic:
#         dic[a].append(b)
#     else:
#         dic[a] = [b]
    
#     if b in dic:
#         dic[b].append(a)
#     else:
#         dic[b] = [a]

# a = [0]
# x = [0]*12
# while True:
#     if len(a) == 0:
#         break
#     if a[0] in dic:
#         for i in dic[a[0]]:
#             if x[i] == 0:  #判斷i有沒有走過
#                 a.append(i)
#                 x[i] = 1
#     v = a.pop(0)
#     print(v)


# n = int(input())

# record = [0]*13
# dic = {}
# for i in range(n):
#     a, b = map(int,input().split())
#     if a in dic:
#         dic[a].append(b)
#     else:
#         dic[a] = [b]
#     if b in dic:
#         dic[b].append(a)
#     else:
#         dic[b] = [a]

# queue = [0]
# record[0] = 1
# while queue:
#     node = queue.pop(0)
#     print(node)

#     if node in dic:
#         for i in dic[node]:
#             if record[i] == 0:
#                 queue.append(i)
#                 record[i] = 1


'''
4.bfs 搜索所有點

'''
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



matrix = [["s", 1 , 2 ,"x"],
           [ 3 ,"x", 4 , 5 ],
           [ 6 , 7 , 8 ,"x"],
           [ 9 ,"x", 10, 11],
           [ 12, 13, 14,'e']]

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
'''

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


5
a(5) = a(4) + 5
a(4) = a(3) + 4
a(3) = a(2) + 3
a(2) = a(1) + 2
        1
a(1) = a(2) + 1
a(2) = a(3) + 2
'''
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





