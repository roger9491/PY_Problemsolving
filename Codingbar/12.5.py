'''
while Ture:
    try:


    except:
        break





'''
# while 1:
#     try:
#         r,c,m=map(int,input().split())

#         l=[]
#         for i in range(r):
#             l.append(input().split())

#         work=list(map(int,input().split()))

#         temp=[]
#         ans=[]
#         for i in range(m):
#             if work[i]==0:
#                 for j in range(len(l[0])):
#                     for k in range(len(l)):
#                         temp.append(l[len(l)-k-1][j])
#                     ans.append(temp)
#                     temp=[]
#                 l=ans
#                 ans=[]
#             elif work[i]==1:
#                 l.reverse()

#         print(len(l),len(l[0]))
#         for i in range(len(l)):
#             print(" ".join(l[i]))
#     except:
#         break
'''

s      e
|------| a
    s       e
    |-------| b
a[s] <= b[s]
|------|
|----------|
a = [[1,2],[5,7],[1,3]]
a.sort()
a = [[1,2],[1,3],[5,7]] #數對排序
'''

'''
輸入兩個數字 m n
接著輸入 m 行

判斷 每一個格子 上下左右 有多少個1

印出  每一個格子的 1 數量
ex
2 4
0 1 1 0 
1 0 1 1 
t = [[0 1 1 0 ],
     [1 0 1 1 ]]
i j 右 => i j+1 [0,1]
    上  => i-1 j   [0,1]

dire = [[0,1],[0,1],[-1,0],[0,-1]]

#檢驗
2 1 2 2
0 3 2 1

'''

# m,n = map(int,input().split())

# t = []
# for i in range(m):
#     e = input().split()
#     t.append(e)

# matrix = [[0]*n for i in range(m)]

#         #上   #下    #左    #右
# Dir = [[0,1],[0,-1],[-1,0],[1,0]]

# for i in range(m):
#     for j in range(n):
#         c = 0
#         for way in Dir:
#             x = i + way[0]
#             y = j + way[1]
#             if 0 <= x < m and 0 <= y < n:
#                 if t[x][y] == "1":
#                     c += 1
#         matrix[i][j] = c    #

# for i in range(m):
#     print(matrix[i])
                

'''
遞迴
a(1)

a(2)
a(3)
a(4) 
a(5)
'''

# def a(n):
#     if n == 1:
#         return 1
#     return (a(n-1) + n)
# print(a(5))

'''

[] 右端點 代表stack 口
加入 
stack.append()

取出資料
方法一
temp = stack[-1]
del stack[-1]
方法 二
temp = stack.pop()

show
print(stack)

f(x) = 2x – 3
g(x, y) = 2x +y – 7
h(x, y, z) = 3x – 2y + z

h f 5 g 3 4 3
stack = [h 7 3 3 ]


'''
# stack = []

# while True:
#     n = int(input())
#     if n == 1:  #push
#         data = input()
#         stack.append(data)
#     elif n == 2:    #pop
#         if stack:
#             temp = stack.pop()
#             print(temp)
#     elif n == 3:    #show
#         print(stack)
#     else:
#         break


# def a(n):
#     if n == 1:
#         return
#     print(n)
#     return a(n-1)
# a(1000)

'''

queue = []

queue.append(data)
temp = queue.pop(0)
f f f 2

stack = [f]


印出數字

a 2 4 1 34 as

a
2
4
1
34
as

map() : 轉型態
s = input().split()



6 140
          1      1
10 30 50 70 100 125
30 25 10 10 55 25



temp = stack.pop()

貪心

'''



'''


s = input().split()




'''
s = input().split()
print(s)