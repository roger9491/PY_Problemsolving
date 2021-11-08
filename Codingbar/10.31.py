'''
min()   #找最小
max()   #找最大
sum()   #串列的數字總和
二維陣列


購物車
購買力

第二題
骰子    思維
機器人路徑 模擬
人口遷移
魔王 
流量 難
'''

# a = [2,5,6,8,9]
# print(max(a))
# print(min(a))
# c = 6
# d = 7
# print(max(c,d,max(a)))
'''
建立二維陣列

1 2 3
4 5 6
7 8 9

'''
    # j
#      #0 1 2   
# a = [[1,2,3]    #0  i
#     ,[4,5,6]    #1
#     ,[7,8,9]]   #2

# # a[0] = [1,2,3]
# # a[2][1] = 8
# # a[i][j] =

# matrix = []
# for i in range(4):
#     a = list(map(int,input().split()))
#     matrix.append(a)
# print(matrix)
# #第一種情況 預先知道3 x 3  ， i的數量 x j的數量 4 x 3
# matrix_copy = [[0]*3 for i in range(4)]
#             # [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
# print(matrix_copy)

# #第二種情況
# matrix_copy = matrix.copy()
# print(matrix_copy)

# for i in range(4):   #迭代 i
#     for j in range(3):  #迭代j
#         print(matrix[i][j])


'''
輸入 二維矩陣
檢查是否是質數 做記號 1
印出來
輸入 四行
n,m = i的數量,j的數量
1 2 3
4 5 6
7 8 9
10 11 12


0 0 1
0 0 0
0 0 0
0 0 0

print(串列)
'''

# record = [[0]*3 for i in range(4)]

# matrix = []
# for i in range(4):
#     a = list(map(int,input().split()))
#     matrix.append(a)


# for i in range(4):
#     for j in range(3):
#         if i == 0 and j == 0 or i == 0 and j == 1:
#             pass
#         else:
#             for k in range(2,matrix[i][j]):
#                 if matrix[i][j] % k == 0:
#                     break
#             else:
#                 record[i][j] = 1
# print(record)


'''
輸入 二維矩陣


第一種情況 預先知道3 x 3  ， i的數量 x j的數量 4 x 3
印出 相鄰的 1 有多少個
相鄰 : 上下左右

第一行 n m      n x m   5 4
接下來輸入n 行


輸出 相鄰的 1 有多少個
ex
輸入
2 3
0 1 0 input() "0 1 0" => ["1","0","1"]
1 0 1



輸出
7

'''
# size = input().split()
# for i in range(int(size[0])):
#     a = input()
#     print(a)
#map(型態,串列)
        # 下          右        上          左  
# dire = [["1","0"],["0","1"],["-1","0"],["0","-1"]]
# size = input().split(" ")
# L = []*int(size[1])
# for i in range(int(size[0])):
#     put = input().split(" ")    #串列
#     L[i].append(put)


'''
[[1,0,1],[0,1,0]]
a = []
1 0 1
[1,0,1]
a.append(put)
a.append([1,0,1])


'''



# dire = [[1,0],[0,1],[-1,0],[0,-1]]
# dire[0] = [1,0]
# dire[1] = [0,1]
# # n m
# # i j   0 ~ n - 1 , 0 ~  m-1
# for x in dire: 
#     now_x = i + x[0]
#     now_y = j + x[1]
#     if 0 <= now_x < n and 0 <= now_y < m:

# for x in dire:
#     print(x)
#     print(x[0],x[1])



# n = list(map(int,input().split()))
# num = []
# for i in range(int(n[0])):
#     a = list(map(int,input().split()))
#     num.append(a)
# # 0 1 0
# # 1 0 1
# #
# # 下          右        上          左  
# #2 3
# # 0 1 0
# # 1 0 1 
# dire = [[1,0],[0,1],[-1,0],[0,-1]]
# for i in range(int(n[0])):  # 0 1 
#     for j in range(int(n[1])):  # 0 1 2
#         for x in dire: 
#             now_x = i + x[0]
#             now_y = j + x[1]
#             if 0 <= now_x < n and 0 <= now_y < m:
#                 pass
'''
i = 0 
j = 0 
x = [1,0]
nx = 1
ny = 0







'''


dire = [[1,0],[0,1],[-1,0],[0,-1]]
L = []
c = 0
size = input().split(" ")
for i in range(int(size[0])):
    put = input().split(" ")
    put = list(map(int,put))
    L.append(put)

for i in range(int(size[0])):
    for j in range(int(size[1])):
        for x in dire: 
            now_x = i + x[0]
            now_y = j + x[1]
            if 0 <= now_x < int(size[0]) and 0 <= now_y < int(size[1]):
                c += 1
            else:
                pass      
print(c)                         