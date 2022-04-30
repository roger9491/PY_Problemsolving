'''
dict    
建立空字典  a = {} 
新增資料    a[key] = value 
查詢        a[key]    key取值   O(1)
刪除        del a[key]
判斷存在    if key in  O(1)

注意 key 不能重複的
'''

# a = {}

# a["宇軒"] = 180
# print(a["宇軒"])
# del a["宇軒"]
# if "宇軒" in a:
#    a["宇軒"] += 1
# else:
#     a["宇軒"] = 1
# print(a)




'''
兩個數組的交集 (1)
https://leetcode-cn.com/problems/intersection-of-two-arrays/

不能用 SET()
用dict的方式去做

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
'''
#O(n*m)
# nums1 = [1,2,2,1]   #n
# nums2 = [2,2]       #m

# ans=[]
# for i in range(len(nums1)): #n
#     if nums1[i] in nums2:   #m
#         ans.append(nums1[i])

# trueans=[]

# for i in range(len(ans)):
#     if ans[i] not in trueans:
#         trueans.append(ans[i])
# print(trueans)

#O(n+m)

# nums1 = [1,2,2,1]   #n
# nums2 = [2,2]       #m

# dict = {}
# for i in nums1:
#     dict[i] = 1
# print(dict)
# ans = []
# for i in nums2:
#     if i in dict:   #O(1)   key 判斷 索引值有沒有存在
#         dict[i] = 2

# for i in dict:
#     if dict[i] == 2:
#         ans.append(i)
# print(ans)
'''
兩個數組的交集 (2)
https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/submissions/
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
'''




'''

並查集

一個維護集合的資料結構 ， 適用在判斷元素關係，主要為兩種操作
(1) 查詢    查詢該元素的祖先
(2) 合併    合併元素為同一個家族





'''
#首先 需要先初始化元素

from heapq import merge


par = [0]* 5
for i in range(5):
    par[i] = i

#遞迴
# def find(x):
#     if x == par[x]:
#         return x
#     else:
#         return find(par[x])

#迭代
# def find(x):
#     while x != par[x]:         #過濾
#         x = par[x]
#     # x == par[x]
#     return x
# # par = [0,1,1,2,3]
# # find(4)

# def merge(x,y):
#     a = find(x) #找到x的祖先
#     b = find(y) #找到 y 的祖先
#     if a == b:
#         return
#     else:
#         par[a] = b
#         #par[b] = a

#路徑壓縮

#遞迴
# def find(x):
#     if x == par[x]:
#         return x
#     else:
#         par[x] =  find(par[x])  #找祖先
#         return par[x]
# par = [0,1,1,2,3]
# find(4)
# print(par)
'''
find(4) => par[4] = find(3) return 1
                        1
find(3) => par[3] = find(2) return par[3]   1
                        1
find(2) => par[2] = find(1) return 1
                    1
'''
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

# def find(x):
#     # print(x)
#     # input()
#     temp = x
#     while x != par[x]:
#         x = par[x]

#     while temp != par[temp]:
#         y = par[temp]
#         par[temp] = x
#         temp = y
#     return x

# #合併
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
#     # print(par)
#     merge(a,b)

# for i in range(p):
#     a,b = map(int,input().split())
    
#     ans1 = find(a)

#     ans2 = find(b)

#     if ans1 == ans2:
#         print("Yes")
#     else:
#         print("No")






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


# n = int(input())
# for i in range(n):
#     a = input().split()
#     par = [0]*81
#     for i in range(81):
#         par[i] = i
#     temp = []
#     for j in a:
#         a,b = list(map(int,j.split(",")))
#         if find(a) == find(b):
#             print("F")
#             break
#         merge(a,b)
#         temp.append(a)
#         temp.append(b)
#     else:
#         temp = set(temp)
#         c = 0
#         for i in temp:
#             if par[i] == i:
#                 c += 1
#         if c > 1:
#             print("F")
#         else:
#             print("T")

def find(a):
    if a == par[a]:
        return a
    else:
        par[a] = find(par[a])
        return par[a]

def merge(a,b):
    x = find(a)
    y = find(b)
    if x == y:
        return
    else:
        par[x] = y


n, p, m = map(int,input().split())

par = [0] * (n+1)

for i in range(n+1):
    par[i] = i


for i in range(p):
    a,b = map(int,input().split())
    merge(a,b)

for i in range(m):
    a,b = map(int,input().split())
    if find(a) == find(b):
        print("Yes")
    else:
        print("No")
