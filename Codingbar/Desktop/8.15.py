'''

bfs:
    給一個起點，他就會遍歷所有你能走到點


最短距離
兩點之間的最短"距離"



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
1+2+3       3
1+2+3+4     4
1+2+3+4+5   5
認定N階段性問題
1 +1
2 1+2
3 1+2+3
N階段 = N-1階段 + N

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

(1) 邊界值 n == 1 return 1
(2) 遞迴關係式
    a(n) = a(n-1) + n
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
#     if n == 1:
#         return n
#     return a(n-1) + n
# n1 = int(input())
# print(a(n1))

# def a(n):
#     print(n)
#     if n == 1:
#         return
#     a(n-1)
#     print(n)
# a(5)

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
# yee = []
# dict={0:[2,3],2:[10],3:[4,5],5:[6]}
# def a(n):
#     print(n)
#     yee.append(n)
#     if n not in dict:
#         print(yee)
#         del yee[-1]
#         return
#     else:
#         for i in dict[n]:
#             a(i)
#         del yee[-1]
# a(0)

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
dict={0:[2,3],2:[10],3:[4,5],5:[6],2:[10,0]}
yee=[]
def a(n):   #a(0)   a(3)
    print(n)
    yee.append(n)
    if n not in dict:
        return
    else:
        for i in dict[n]:#2,3
            if i not in yee:
                a(i)    #a(3)

a(0)
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

""" 
練習題

血緣關係
https://zerojudge.tw/ShowProblem?problemid=b967

樹狀圖分析
https://zerojudge.tw/ShowProblem?problemid=c463
"""

""" 
暴力


"""

""" 
獨眼怪試密碼

n個數字 m種可能
"""

# n, m = map(int,input().split())

# def dfs(n, m, st):
#     if n == 0:
#         t.append(st)
#         return
#     for i in range(m+1):
#         st += str(i)
#         dfs(n-1, m, st)
#         st = st[:-1]

# t = []
# dfs(n,m, "")
# for i in t:
#     print(i)

""" 
分蘋果


"""
# def dfs(index):
#     global minv
#     if index == n:
#         a1 = 0
#         a2 = 0
#         for i in range(n):
#             if t[i] == 0:   
#                 a1 += a[i]
#             else:
#                 a2 += a[i]
#         minv = min(minv, abs(a1-a2))
#         return
#     for i in range(2):
#         t[index] = i
#         dfs(index+1)
# n = int(input())
# a = list(map(int,input().split()))
# t = [-1]*n
# minv = 10**9

# dfs(0)
# print(minv)


"""
剪枝


https://zerojudge.tw/ShowProblem?problemid=b053
"""










