
'''
測驗 (2)
插入排序
題目:
    數列分成 1.已排序 2.未排序
    逐一從未排序資料一筆一筆的放入已排序的正確位置

    3 1 5 2 
1 3 5

(2) 
1  5  7  9      6
小 ~　大
遇到第一個比自己小的時候，你應該要放在他的右邊




1   5   9   11      4
小 ~ 大
1   5   9    4   11
1   5   4    9   11
1   4   5    9   11
算法: 你應該要放在第一個比你小的後面
4   2   5   1   3
2   4   5   1   3
2   4   5   1   3
1   2   4   5   3
3   1   2   4   5
'''

# a=[4,2,5,1,3]
# for i in range(len(a)): #未排序 a[i] 準備要放入已排序的值
#     for j in range(i,0,-1):  #放入已排序的過程
#         if a[j] > a[j-1]:
#             break
#         else:
#             tmp = a[j]
#             a[j] = a[j-1]
#             a[j-1] = tmp
# print(a)


# import random

# def InsertionSort(arr):
#     index = 1
#     for i in range(1,len(arr)):
#         for j in range(i,0,-1):
#             if arr[j] < arr[j-1]:
#                 tmp = arr[j]
#                 arr[j] = arr[j-1]
#                 arr[j-1] = tmp
#             else:
#                 break
#     return arr
# def SelectionSort(arr):
#     for i in range(len(arr)):
#         minv = 10**9
#         index = -1
#         for j in range(i, len(arr)):
#             if minv > arr[j]:
#                 minv = arr[j]
#                 index = j
#         tmp = arr[i]
#         arr[i] = minv
#         arr[index] = tmp
#     return arr

# for i in range(15, 21):
#     arr = []
#     for j in range(i):
#         arr.append(random.randint(1,100))
#     arr1 = InsertionSort(arr)
#     arr2 = SelectionSort(arr)
#     arr3 = sorted(arr)
#     if arr1 == arr3:
#         print("InsertionSort 正確")
#     else:
#         print("InsertionSort 錯誤")
#         break
#     if arr2 == arr3:
#         print("SelectionSort 正確")
#     else:
#         print("SelectionSort 錯誤")
#         break
'''
練習題
https://codeforces.com/problemset/problem/39/H

ex1
input
10
output
1  2  3  4  5  6  7  8  9
2  4  6  8 10 12 14 16 18
3  6  9 12 15 18 21 24 27
4  8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81

ex2
input
3
output
1  2
2 11
'''
# def transNum(n):
#     s = ""
#     while n != 0:
#         s = str(n%k) + s
#         n = n // k
#     return s

# k = int(input())

# matrix = [[0]*(k-1) for i in range(k-1)]

# for i in range(k-1):
#     for j in range(k-1):
#         matrix[i][j] = transNum((i+1)*(j+1))
# for i in matrix:
#     print(" ".join(i))
'''
二維串列

一維串列
a = [1,2,3,5]

二維串列
a = [[1,3,4,5,],[2,3,5,],[2,65]]
'''
# #讀
# a = [1, 2, 3, 5]
# print(a[2])
# #改
# a[2] = 9

# #加入
# a.append(23)


# 讀
# a = [[12,3,4], [4,5,6,7], [4,6,1], [7,8,9]]
# print(a[2])
# print(a[2][2])

# 改
# a[1][2] = 99
# print(a)

# 加入
# a.append([2,3])
# print(a)

# 建立
'''
m個字串列
n個子串列裡的值個數

m = 4
n = 3

matrix = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]

'''
# # 原始做法
# m, n = map(int,input().split())
# matrix = []
# for i in range(m):
#     tmp = []
#     for j in range(n):
#         tmp.append(1)
#     matrix.append(tmp)
# print(matrix)
    
# # 簡潔的做法 一定要記
# m, n = map(int,input().split())

# matrix = [[0]*n for i in range(m)]
# #         [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
# print(matrix)
'''
矩陣

    [[1,1,1],
     [1,1,1],]
'''

'''
輸入兩個數字 m n
建立這個 m x n 的矩陣
輸入 m*n 數字
印出 矩陣

ex 
input
2 2
1
2
3
4

1 2
3 4

input
3 3
1 2 3   input.split()
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

input
2 4
1 7 8 9
6 7 4 1

1 7 8 9
6 7 4 1
'''
# m, n = map(int,input().split())

# matrix = []
# for i in range(m):
#     a = input().split()
#     matrix.append(a)

# for i in range(m):
#     print(" ".join(matrix[i]))



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


m = 4, n = 3
0+0
    [[x,y,x],
     [,,],
     [,,],
     [,,]]

ex
3 3

x y x
y x y
x y x



字串.join(串列(一維))
    合併串列
ex.
['5','3']
 
"x".join(['5','3'])
5x3
" ".join(['5','3'])
5 3
''' 

m, n = map(int,input().split())

matrix = []
matrix = [[0]*n for i in range(m)]
for i in range(m):
    if i % 2 == 0:
        for i in range(m):
            if i % 2 == 0:
                matrix.append('x')
            else:
                matrix.append('y')
    else:
        for i in range(m):
            if i % 2 == 0:
                matrix.append('y')
            else:
                matrix.append('x')
print(matrix)
for i in range(m):
    print(' '.join(matrix[i]))

# 建立
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
輸入兩個數字 m n, row: m, col: n
接著輸入 m row

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


'''