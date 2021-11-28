'''
<<<<<<< HEAD
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
輸入兩個數字 m n
建立這個 m x n 的矩陣 初始值 = (索引值相加) 判斷 
偶數 x  奇數y
印出 這矩陣

3 3
  j  0 1 2  matrix[i][j] = "x"
i 0  x y x
  1  y x y
  2  x y x
  a = [1,2,34]
  a[0] = 1
''' 
#建立
m,n = map(int, input().split(" "))
L = [["0"]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        if (i+j) % 2 == 0:
            L[i][j] = "x"
        else:
            L[i][j] = "y"
for k in range(m):          
    print(" ".join(L[k]))

'''
輸入兩個數字 m n
接著輸入 m 列

判斷 0的個格子 上下左右 總共有多少個1
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




=======
輸入 m  n
建立二維矩陣初始值為x 並印出


'''


'''
輸入 m  n
建立二維矩陣初始值為(索引值相加)偶數(0)為"x" (1)奇數為"y" 並印出 
2 2

x y
y x


'''

'''
輸入 m  n
輸入 m 列代表接下來的值
搜尋0的格子 上下左右總共有多少個1
印出總和
3 4
0 1 1 0
0 0 1 1
1 1 1 1

7
>>>>>>> 0084bee00ea3d01677b3a33935a3b88d4ba41eb8

'''

'''
max()


輸入 n 個數字
0   2   5   12  3   4
    2   5   12  12  12
印出最大
12
temp = 

'''
n = list(map(int,input().split()))
temp = n[0]
for i in range(1,len(n)): # 0 ~ len(n)-1    o(n)
    if temp < n[i]:
        temp = n[i]
