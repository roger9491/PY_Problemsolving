'''
堆疊 

串列
push
    a.append()

pop
    del a[-1]
    a.pop() 刪除 + 取值


c/c++ 陣列 
先宣告陣列大小

(([])([]))

(([)

配對的時候發生?

'''

# a=input()
# b=[]
# c=[]
# for i in a:
#     if i in '()/{/}[]':
#         b.append(i)
# print(b)
# for j in range(len(b)):
#     if b==[]:
#         break
#     for i in range(len(b)):
#         if i==len(b)-1:
#             break
#         if b[i]+b[i+1] =="()"or b[i]+b[i+1] =="{}"or b[i]+b[i+1] =="[]":
#             del b[i]
#             del b[i+1]
#             break
#     print(j,b)
# if b==[]:
#     print('True')
# else:
#     print("False")

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


def suml(a):
    total = 0
    for i in a:
        total += i
    return total
a = [[1,2,3],[2,3,4],[4,5,6,4,5,1],[1,2]]
a.sort(key=suml)
print(a)

'''
from functools import cmp_to_key

'''

#  from functools import cmp_to_key
# def f(a,b):
#     if int(a+b) < int(b+a):
#         return -1   #交換 a 和 b
#     else:
#         return 1

# n = int(input())

# t = []
# for i in range(n):
#     num = input()
#     t.append(num)

# # for i in range(n):
# #     for j in range(n-1-i):
# #         if int(t[j]+t[j+1]) < int(t[j+1] + t[j]):
# #             temp = t[j]
# #             t[j] = t[j+1]
# #             t[j+1] = temp
# t.sort(reverse=True,key=cmp_to_key(f))

# # 5 5111
# # 5111 521
# # 5215111
# print("".join(t))

'''

作業練習

函數運算式求值
https://zerojudge.tw/ShowProblem?problemid=f640

砍樹
https://judge.tcirc.tw/ShowProblem?problemid=d030

'''