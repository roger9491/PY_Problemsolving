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
最遠距離

n個的點的樹，點的編號為1~n
問你q次 從s出發 距離s最遠的距離多少

輸入
第一行 n, q
接下來 n - 1 行，每行 a, b
接下來 q 行， 代表起點s

輸出 
最遠距離

input
8 3
5 6
1 5
4 6
7 1
3 5
8 6
2 8
5
3
2

output
3
4
5
'''

# def dfs(n):
#     global ans
#     global c
#     ans = max(ans, c)

#     for i in v[n]:
#         if record[i] == 0:
#             c += 1
#             record[i] = 1
#             dfs(i)
#             c -= 1

# n, q = map(int,input().split())

# v = {}
# for i in range(n-1):
#     a, b = map(int,input().split())
#     if a in v:
#         v[a].append(b)
#     else:
#         v[a] = [b]
    
#     if b in v:
#         v[b].append(a)
#     else:
#         v[b] = [a]

# for i in range(q):
#     s = int(input())
#     record = [0]*(n + 1) 
#     record[s] = 1
#     ans = 0
#     c = 0
#     dfs(s)
#     print(ans)






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

'''
獨眼怪走迷宮1
'''