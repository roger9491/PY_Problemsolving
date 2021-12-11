'''
輸入兩個數字 m n
接著輸入 m 行

判斷 0的個格子 上下左右 總共有多少個1

印出 數量
ex
2 4
0 1 1 0 
1 0 1 1 
[[0, 1, 1, 0], [1, 0, 1, 1]]
    matrix[0][0] ~ matrix[3]   matrix[1]
7
'''
# count = 0
# matrix = []
# m, n = map(int, input().split())
# for i in range(m):
#     matrix.append(list(map(int,input().split())))
# for i in range(m):
#     for j in range(n):
#         print(matrix[i][j])





'''
輸入兩個數字 m n
接著輸入 m 列

判斷 每一個格子 上下左右 有多少個1

輸出每一個格子上下左右 多少個1

ex
input
2 4
0 1 1 0
1 0 1 1

output
2 1 2 2
0 3 2 1


'''



'''
輸入 一行 數字 空格隔開

把最大值放在最後一項
輸出 串列


ex
temp = -9999
9 8 7 6 5 4 
(1)
8 7 6 5 4 9

(2)
7 6 5 4 8 9

for i in rang






'''
# l=list(map(int,input().split()))
# l.reverse()
# l.sort(reverse=True)    #改變遠本的串列
# print(l)
# t = []
# for i in range(len(l)-1,-1,-1):
#     t.append(l[i])


'''
輸入一行數字 

5 1 7 3 7 2

2 7 3 7 1 5



'''


#-------------------------

# n = 0
# while n < 10:
#     n += 1
#     print(n)

# a= [ 1,2,3,4,5,6,7]

# n = 0
# while n < 10:
#     n += 1
#     print(a[n])


#-------------------------

# n = 11
# while 1 < n < 12:
#     n -= 1
#     print(n)

#-------------------------
# a= [ 1,2,3,4,5,6,7]
# n = 11
# while 1 < n < 12:
#     n -= 1
#     print(n)
clas,messay,avg=map(int,input().split())
t=[]

for i in range(clas):
    n=list(map(int,input().split()))
    t.append([n[1],n[0]])
t.sort()
al=0
for i in range(len(t)):
    al+=t[i][1]
count=0
while 1:
    if al/clas>=avg:
        print(count)
        break
    for i in range(len(t)):
        if t[i][1]<messay:
            count+=t[i][0]
            t[i][1]+=1
            break
    al+=1
