
'''
泡沫排序法/氣泡排序法

原  15  7   3   17  10  
1.  7   15  3   17  10
2.  7   3   15  17  10
3.  7   3   15  17  10
4.  7   3   15  10  17
1.  3   7   15  10  17
2.  3   7   15  10  17
3.  3   7   10  15  17
4.  3   7   10  15  17

今天至少要掃幾遍才能保證長度為n的數列一定會排好?
    n-1     

5 4 2 1
4 5 2 1
4 2 5 1
4 2 1 5      

j j+1
3 4

初階版的泡沫排序法
時間複雜度: n**2 
'''# 0  1  2   3  4
a = [5, 4, 3 , 2, 1]    #len(a)
for i in range(len(a)-1):   #掃n-1遍
    for j in range(len(a)-1):   #n-1 => n**2 
        if a[j] > a[j+1]:
            tmp = a[j]
            a[j] = a[j+1]
            a[j+1] = tmp
'''
優化

時間複雜度: n**2
'''
a = [5, 4, 3 , 2, 1]    #len(a)
for i in range(len(a)-1):   #掃n-1遍  0 1 2 3 
    for j in range(len(a)-1-i):   #n-1 => n**2 
        if a[j] > a[j+1]:           # 0 3  - 0
            tmp = a[j]              # 0 2  - 1
            a[j] = a[j+1]           # 0 1   - 2
            a[j+1] = tmp

'''
實作的時候，盡量用現成的函式

排序
串列.sort() :   改變原串列
sorted(串列):   不會改變原串列
不一樣
a = [5,3,2,1]
# b = sorted(a)
a.sort()
print(a)
'''
a = [5,3,2,1]
# b = sorted(a)
a.sort()
print(a)

'''
字元串列的排序
原理:
    每一個字元在電腦裡都有數字所對應 ascii
    如何知道字元所對應的數值
    (1) 上網查 
    (2) ord() 十進位

'''
a = ["e", "d", "c", "b", "a"]
a.sort()

a = ["e", "d", "c", "b", "a"]
print(ord(a[0]))

'''
數對排序
先比第一個，比不出來比第二個
以次類推

'''
a = [[1,2],[2,3],[2,-1]]
a.sort()
print(a)

'''
字串排序

'''
# a = ["zfg","abe","abc"]
# a.sort()
# print(a)

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

要求:   (上網查)
    自己產生隨機資料
    設計 15 ~ 20 長度的測驗資料 數字介於 1 ~ 100
    每一種長度的測驗資料 產生1次 
    並測驗自己的程式碼正確性
    (sort(), sorted())

最終要求
    1.請在同一個串列
    2.不能用任何的函式or關鍵字 ex insert, append, min, max, .index()
    核心點 
        盡量用原始的語法解決
'''
# x宏
ans=[]
a=list(map(int,input().split()))
ans.append(a[0])
del a[0]
while True:
    if len(a)==0:
        break
    for j in range(len(ans)):
        if ans[j]>a[0]:
            ans.insert(j,a[0])
    del a[0]
print(ans)

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