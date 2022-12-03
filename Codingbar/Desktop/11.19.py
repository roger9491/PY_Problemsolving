a=list(map(int,input().split()))
b=int(input())

d=[]
e=[]
g=0
f=0
d.append(a[0])

for i in range(1,len(a)):
    f=a[i]-a[i-1]
    d.append(f)

for j in range(b):
    c=list(map(int,input().split()))

    d[c[1]] +=c [0]
    if c[2] != len(d) - 1:
        d[c[2]+1] -= c[0]


for h in range(len(a)):
    g=g+d[h]
    e.append(g)

print(e)


'''
from functools import cmp_to_key

'''

# from functools import cmp_to_key
# def f(a,b):
#     if a > b:
#         return 1   #交換 a 和 b
#     else:
#         return -1

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

# t = [[1,2],[2],[3,4,5]]
# t.sort(key=len)
# print(t)
'''

砍樹
https://judge.tcirc.tw/ShowProblem?problemid=d030

物品堆疊
https://zerojudge.tw/ShowProblem?problemid=c471

'''