'''
測驗 (1)
選擇排序
題目:
    數列分成 1.已排序 2.未排序
    從未排序找出最小放入已排序的

測驗 (2)
插入排序
題目:
    數列分成 1.已排序 2.未排序
    逐一從未排序資料一筆一筆的放入已排序的正確位置


要求:
    自己產生隨機資料
    設計 15 ~ 20 長度的測驗資料 數字介於 1 ~ 100
    每一種長度的測驗資料 產生1次 
    並測驗自己的程式碼正確性
    
'''
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