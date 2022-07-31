'''
不能用index
a = [1,25,3,8,1,4,73,5,7]
輸入一個目標

輸出該目標的索引值
如果不存在輸出-1




'''

# a = input().split() 

# for i in range(len(a)): #n
#     for i in range(i,len(a)): #n
#         print(a[i])

'''
時間複雜度
1 + 1 + n + 1 + 1= n + 4
一律考慮最壞的情形
O(n + 4) =>   O(n)  捨去常數
O(2n) =>      O(n)  捨去常數
O(n**2) =>    O(n**2)
O(n**2 + n) => O(n**2)  因為n很大時 +n 可以忽略

a = input().split() 

for i in range(len(a)): #n
    for i in range(i,len(a)): #n
        print(a[i])
O(n**2)

a = [1,2,3,4,5,6,7]
print(a.index(8))   #O(n)



補充知識
為什麼要學時間複雜度 (time complexity) ?
因為 考試的時候 裁判機 會限制時間

一般來說 指令次數會限制在 10**6 ~ 10**7
超出這個限制就會TLE

EX 
for i in range(len(a)): #n
    for i in range(i,len(a)): #n
        print(a[i])
O(n**2)     n:串列的長度
n: 最大多少 符合 10**6 ~ 10**7
n**2 <= 10**6 
n <= 10**3
(10**3)**2 = > 10**6
n: 盡量低於 10**3 保證不會TLE

'''

'''
a = [1,2,3,4,5,6,5,1,3,5]
輸入一個數字

印出數字在a的個數
'''


# a,b=list(map(int,input().split()))
# n=int(input())
# flag=0
# for i in range(n):
#     item=list(map(int,input().split()))
#     del item[-1]
#     if (a in item) and (b in item):
#         time1=0
#         time2=0
#         for j in range(len(item)):
#             if item[j]==a:
#                 time1+=1
#             elif item[j]==-a:
#                 time1-=1
#             elif item[j]==b:
#                 time2+=1
#             else:
#                 time2-=1
#         if (time1>0) and (time2>0):
#             flag+=1
    
# print(flag)


import random
s = "1"*13
t = ""
for i in range(20):
    t += str(random.randint(0,9))
    if random.randint(0,1):
        t += s
print(t)
print(s)
print(t.split(s))