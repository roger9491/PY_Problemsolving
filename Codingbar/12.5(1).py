'''
輸入兩個數字 m n
建立這個 m x n 的矩陣
印出 這矩陣

ex 

3 3

0 0 0
0 0 0
0 0 0

2 4

0 0 0 0
0 0 0 0
'''
# n = list(map(int,input().split()))
# m,n = map(int,input().split())

# matrix = [["0"]*n for i in range(m)]
# print (matrix)
# # 2 4
#     #j
# [['0', '0', '0', '0'], #i
#  ['0', '0', '0', '0']]  
# # matrix[i][j]               matrix[1]
#             # [["0","0"] ,["0","0"] ,["0","0"]]
# for i in range(m):
#     print(" ".join(matrix[i]))

'''
輸入兩個數字 n m
建立這個 n x m 的矩陣 初始值 = (索引值相加) 判斷 
偶數 x  奇數y
印出 這矩陣
d = [[1,1],[1,1],[1,1]]
d = [[x,y,x],[y,x,y],[x,y,x]]
d[0][1]


3 3


  j  0 1 2  matrix[i][j] = "x"
i 0  x y x
  1  y x y
  2  x y x

''' 
#建立
# m,n = map(int, input().split(" "))
# L = [["0"]*n for i in range(m)]

# for i in range(m):
#     for j in range(n):
#         if (i+j) % 2 == 0:
#             L[i][j] = "x"
#         else:
#             L[i][j] = "y"
# for k in range(m):          
#     print(" ".join(L[k]))

'''
輸入第一行兩個數字 n m
接著輸入 n 列

判斷 0的個格子 上下左右 總共有多少個1

3 5
0 1 0 1 0
0 0 0 1 1
1 1 1 0 0

1 2 2 
1 2 2 2 1 = 13

i j 當前索引值
    上      下      左      右
   i-1      i+1     j-1     j+1
a= [-1,0]    [1,0]     [0,-1]    [0,1]
dire = [[-1,0] ,[1,0],[0,-1] , [0,1]]

for a in dire:  #上下左右   若遇到邊界值?
    now_i = i + a[0]
    now_j = j + a[1]
    if 0 <= now_i < n and 0 <= now_j < m:   #符合 條件
        if a[now_i][now_j] == 1:







y x

i j
上  下  左  右 重複 
i-1 i+1 j-1 j+1
j+0 j+0 i+0 i+0
上 y-1  上      下     左    右
dir = [[-1,0],[1,0],[0,-1],[0,1]]
k = [-1,0]
k = [1,0]
i j 
for k in dir:
    #方向
    a = k[0] + i
    b = k[1] + j

    #判斷有沒有超出邊界
    if 0 <= a < m and 0 <= b < n:
印出 數量
ex
2 4
0 1 1 0
1 0 1 1

7

若寫完 week2 邊緣偵測
'''


'''


輸入
第一行輸入 n m  (n)代表 接下來的輸入次數 (m)

    每一次的輸入 



重複輸入 值到輸入 0 為止
    物品名稱

輸出 金額

ex
5 5
a 1 5 a s
b 7 3 s a
c 3 s d a
d 10 s a s
e 55 a s 2



1     0    1
b=[0['a', '1'], 
   1['b', '7'], 
   2['c', '3'], 
   3['d', '10'], 
   4['e', '55']]

c=[[0, 0], 
   [0, 0], 
   [0, 0], 
   [0, 0], 
   [0, 0]]
#上到下 0 ~ 4 i
#左到右 0 ~ 1 j
b[i][j]

二維串列
b[2] = ['c', '3']
b[2][0]

b[4] =  ['e', '55']
b[4][1] = "55"
b[4][1][0] = "5"


c = ['c', '3']
c[0]



'''
# n,m = map(int,input().split())

# matrix = [[0]*m for i in range(n)]  #快速建立二維串列
# #        [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

# matrix[0][0] = 1
# print(matrix)

# a = [0]*5
# a = [[2,3]]*5

# a[0][0] = 1
# print(a)
# e=[]
# a=input()
# a=a.split()
# c=0
# n,m=map(int,a)
# for i in range(n):
#     b=input()
#     b=b.split()
#     e.append(b)
# dire = [[-1,0],[1,0],[0,-1],[0,1]]
# for i in range(n):
#     for j in range(m):
#         for f in dire:
#             now_i=i+f[0]
#             now_j=j+f[1]
#             if 0<=now_i<n and 0<=now_j<m:
#                 if e[i][j]=='0':
#                     if e[now_i][now_j]=='1':
#                         c=c+1   
# print(c)
# def a(n):   #None == 沒有任何的值
#     for i in range(10):
#         for j in range(10):
#             if j == 1 :
#                 return  10
# temp = a(10)
# print(temp)

'''
3
26258
2141
15786


'''
n = int(input())
b = []
d = 0
for i in range(n):
    d = 0 
    a = input()
    while True:
        b = []
        for i in a:
            b.append(i)
        c = "".join(b[::-1])
        a = int(a)+int(c)
        b = []
        a = str(a)
        for i in a:
            b.append(i)
        if b[:]==b[::-1]:
            d+=1
            break
    print(d,a)