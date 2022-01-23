'''
兩個數組的交集 (1)
https://leetcode-cn.com/problems/intersection-of-two-arrays/

'''


'''
兩個數組的交集 (2)
https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/submissions/

'''




'''
並查集

一個維護集合的資料結構 ， 適用在判斷元素關係，主要為兩種操作
(1) 查詢    查詢該元素的父親
(2) 合併    合併元素為同一個家族





'''
#首先 需要先初始化元素




#查詢
# def find(x):
#     # print(x)
#     # input()

#     if x == par[x]:
#         return x 
#     else:
#         return find(par[x])

# def find(x):
#     # print(x)
#     # input()
#     while x != par[x]:
#         x = par[x]
#     return x

def find(x):
    # print(x)
    # input()
    temp = x
    while x != par[x]:
        x = par[x]

    while temp != par[temp]:
        y = par[temp]
        par[temp] = x
        temp = y
    return x

#合併
def merge(a,b):
    x = find(a)
    y = find(b)
    if x == y:
        return
    else:
        par[x] = y

n, m, p = map(int,input().split())


par = [0]*(n+1) 
for i in range(n+1):
    par[i] = i

for i in range(m):
    a, b = map(int,input().split())
    # print(par)
    merge(a,b)

for i in range(p):
    a,b = map(int,input().split())
    
    ans1 = find(a)

    ans2 = find(b)

    if ans1 == ans2:
        print("Yes")
    else:
        print("No")






# def init(n):
#     for i in range(n):
#         par[i] = i 
#         rank[i] = 0


# def find(x):
#     if par[x] == x:
#         return x 
#     else:
#         par[x] = find(par[x])
#         return par[x]
        
# def unite(x,y):
#     x = find(x)
#     y = find(y)
#     if x == y:
#         return

#     if rank[x] < rank[y]:
#         par[x] = y
#     else:
#         par[y] = x 
#         if rank[x] == rank[y]:
#             rank[x] += 1


# n = 7
# par = [0]*n
# rank = [0]*n
# init(n)
# unite(0,1)
# unite(1,4)
# unite(5,3)
# unite(5,6)
# print(rank)
# print(par)

'''

https://www.luogu.com.cn/problem/P1551

6 5 3
1 2
1 5
3 4
5 2
1 3
1 4
2 3
5 6
'''
# def find(x):
#     if x == par[x]:
#         return x
#     else:
#         par[x] = find(par[x])
#         return par[x]
# '''
# f(2) => par[x] = f(1)



# '''
# def merge(a,b):
#     x = find(a)
#     y = find(b)

#     if x == y:
#         return 
#     else:
#         par[x] = y 



# n, m, p = map(int,input().split())


# par = [0]*(n+1) 
# for i in range(n+1):
#     par[i] = i

# for i in range(m):
#     a, b = map(int,input().split())

#     merge(a,b)

# for i in range(p):
#     a,b = map(int,input().split())

#     ans1 = find(a)

#     ans2 = find(b)

#     if ans1 == ans2:
#         print("Yes")
#     else:
#         print("No")


'''
畢業旅行
https://zerojudge.tw/ShowProblem?problemid=d831

'''
# def find(x):
#     if x == par[x]:
#         return x
#     else:
#         par[x] = find(par[x])
#         return par[x]

# def merge(a,b):
#     x = find(a)
#     y = find(b)

#     if x == y:
#         return 
#     else:
#         par[x] = y 
#         # print(par)
#         # print(x,y)
#         par2[y] += par2[x]
#         par2[x] = 0

# while True:
#     try:
#         n,m = map(int,input().split())

#         par = [0]*(n+1)
#         par2 = [1]*(n+1)
#         for i in range(n+1):
#             par[i] = i

#         for i in range(m):
#             a,b = map(int,input().split())
#             merge(a,b)
#         print(max(par2))
#     except:
#         break
'''
是否為樹
https://zerojudge.tw/ShowProblem?problemid=b517


4
6,8  5,3  5,2  6,4  5,6  1,2  2,0
8,1  1,3  6,2  8,10  7,5  1,4  7,8  7,6  8,0
3,8  6,8  6,4  5,3  5,6  8,2  2,0
1,0  4,3  1,2

'''

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def merge(a,b):
    x = find(a)
    y = find(b)

    if x == y:
        return 
    else:
        par[x] = y 


n = int(input())
for i in range(n):
    a = input().split()
    par = [0]*81
    for i in range(81):
        par[i] = i
    temp = []
    for j in a:
        a,b = list(map(int,j.split(",")))
        if find(a) == find(b):
            print("F")
            break
        merge(a,b)
        temp.append(a)
        temp.append(b)
    else:
        temp = set(temp)
        c = 0
        for i in temp:
            if par[i] == i:
                c += 1
        if c > 1:
            print("F")
        else:
            print("T")

