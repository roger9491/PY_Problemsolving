'''
https://www.luogu.com.cn/problem/P1102
P1102 A-B 数对


# '''
# X=list(map(int,input().split()))
# N=X[0]
# C=X[1]
# inf=list(map(int,input().split()))
# dic1={}
# times=0
# for i in inf:
#     if i in dic1:
#         dic1[i]+=1
#     else:
#         dic1[i]=1
# print(dic1)
# for i in dic1:
#     if dic1[i]+C in dic1:
#         times+=dic1[dic1[i]+C]*dic1[i]
#         print(dic1[dic1[i]+C]*dic1[i])
#     else:
#         continue
# print(times)
# n, c = map(int,input().split())

# a = list(map(int,input().split()))

# dic = {}

# for i in a:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# # print(dic)
# ans = 0
# # print(dic)
# for i in dic:
#     if i + c in dic:
#         ans += dic[i]*dic[i+c]
#     # if i - c in dic:
#     #     ans += max(dic[i],dic[i-c])

#     # print(ans)
# print(ans)

'''
queue = []

queue.append(data)
data = queue.pop(0)
'''
# n = int(input())
# a = []
# for i in range (n):
#     a.append(i)
# while True:
#     del a[0]
#     temp = a[0]
#     a.append(temp)
#     temp = 0
#     if len(a)==1:
#         print(a[0])
#         break
#     print(a)
'''
監聽

'''
# queue = []

# while True:
#     n = input()
#     if n == "no":
#         break

#     n = int(n)
#     queue.append(n)

#     while queue[0] < queue[-1] - 86400:
#         del queue[0]

#     print(len(queue))


'''
均攤時間複雜度

每一次insert 花的時間複雜度是多少
O(1)
'''
# def insert(val):    #(1) 0
#     global count
#     if count == len(array):
#         sum = 0
#         for i in range(len(array)): #O(n)
#             sum = sum + array[i]
#         array[0] = sum
#         count = 1
#     array[count] = val
#     count += 1

# n = int(input())   # 4
# array = [0]*n
# #len(array)
# count = 0
# insert(1)   #O(1) 1
# insert(2)   #O(1) 1
# insert(3)   #O(1) 1
# insert(4)   #O(1)
# '
# '
# '
# insert(n)   #O(n)


# insert(0)   #O(1)
# insert(0)   #O(n) 

'''

剑指 Offer 59 - II. 队列的最大值
https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
單調佇列

'''
# class MaxQueue:

#     def __init__(self):
#         self.queue = []
#         self.Monotonic_queue = []
#     def max_value(self) -> int:
#         if self.Monotonic_queue:
#             return self.Monotonic_queue[0]
#         else:
#             return -1
#     def push_back(self, value: int) -> None:
#         while self.Monotonic_queue and self.Monotonic_queue[-1] < value:
#             del self.Monotonic_queue[-1]
#         self.Monotonic_queue.append(value)
#         self.queue.append(value)
#     def pop_front(self) -> int:
#         if self.queue:
#             temp = self.queue.pop(0)
#             if temp == self.Monotonic_queue[0]:
#                 del self.Monotonic_queue[0]
#             return temp
#         else:
#             return -1

import random
t = []
for i in range(5):
    t.append(random.randint(1,20))
print(t)

'''
人行道樹
'''



'''
 函數運算式求值
https://zerojudge.tw/ShowProblem?problemid=f640

砍樹
https://judge.tcirc.tw/ShowProblem?problemid=d030

'''


def t1(x,c,h):
    # x=list(map(int,input().split()))
    high=x[1]
    # c=list(map(int,input().split()))
    # h=list(map(int,input().split()))
    times=0
    highest=0
    treestack=[]
    for i in range(len(h)):
        treestack.append(i)#c[p]-h[p]>=c[p-1] 不用p-1
        if len(treestack)==1:
            if c[treestack[-1]]-h[treestack[-1]]>=0:
                times+=1
                if h[treestack[0]]>highest:
                    highest=h[treestack[0]]
                del treestack[0]
        else: 
            if c[treestack[-1]]-h[treestack[-1]]>=c[treestack[-2]]:
                times+=1
                if h[treestack[-1]]>highest:
                    highest=h[treestack[-1]]
                del treestack[-1]
    treestack2=[]
    #rtreestack=treestack.reverse()
    for j in range(len(treestack)-1,-1,-1):#將剩下的往後倒 不過用反著數
        treestack2.append(treestack[j])
        if len(treestack2)==1:
            if c[treestack2[-1]]+h[treestack2[-1]]<=high:
                times+=1
                if h[treestack2[-1]]>highest:
                    highest=h[treestack2[-1]]
                del treestack2[-1]
        else:
            if c[treestack2[-1]]+h[treestack2[-1]]<=c[treestack2[-2]]:
                times+=1
                if h[treestack2[-1]]>highest:
                    highest=h[treestack2[-1]]
                del treestack2[-1]
    # print(times)
    # print(highest)
    return [times, highest]


def t2(x,c,h):
    n = x[0]
    l = x[1]
    # n,l = map(int,input().split())
    # c = list(map(int,input().split()))
    # h = list(map(int,input().split()))
    '''
    10 30 50
    11 15 5
    '''
    stack = []
    c = [0] + c
    c.append(l)
    h = [0] + h + [0]
    start = 0
    end = c[1]
    ans = 0
    max_h = 0
    for i in range(1,n):
        # print(i,start,ans,stack)

        if c[i] - h[i] >= start:
            ans += 1
            max_h = max(max_h,h[i])
        elif c[i] + h[i] <= c[i+1]:
            ans += 1
            max_h = max(max_h,h[i])
        else:
            # print(i)
            start = c[i]
            stack.append(i)
        while stack:
            if c[stack[-1]] - h[stack[-1]] >= start:
                ans += 1
                max_h = max(max_h,h[stack[-1]])
                del stack[-1]
            elif c[stack[-1]] + h[stack[-1]] <= c[i+1]:
                ans += 1
                max_h = max(max_h,h[stack[-1]])
                start = c[stack[-1]-1]
                del stack[-1]
            else:
                break
    # print(i,start,ans,stack,max_h)
    if c[n] - h[n] >= start:
        ans += 1
        max_h = max(max_h,h[n])
    elif c[n] + h[n] <= l:
        ans += 1
        max_h = max(max_h,h[n])

    # print(ans)
    # print(max_h)
    return [ans, max_h]

import random   #隨機

while True:
    n = 3
    x = [n, 200]

    c = []
    while len(c) != n:
        a = random.randint(0,200)
        if a not in c:
            c.append(a)
    
    h = []
    while len(h) != n:
        a = random.randint(1,60)
        if a not in h:
            h.append(a)
    c.sort()
    if t1(x, c, h) != t2(x, c, h):
        print(x,c,h)
        print(t1(x, c, h))
        print(t2(x, c, h))
        break




'''
6 140
10 30 50 70 100 125
30 15 55 10 55 25

'''