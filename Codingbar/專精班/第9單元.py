'''
建立一個 1 ~ 10整數的串列
輸出總和
'''
# a = [1,2,3,4,5,6,7,8,9,10]
# # for i in range(10):
# #     print(i,a[i])

# t = 0
# t = a[0] + a[1] + a[2] + .. a[9]

# t = t + a[0]
# t = t + a[1]
# '
# '
# '
# t = t + a[9]



'''
印出 1 ~ 100
能被2整除但不能被3整除 或是 可以被6整除 的數字
'''
# for i in range(1,101):
#     if (i % 2 == 0 and i % 3 != 0) or (i % 6 == 0):
#         print(i)







""" 
是第幾天呢？
2000
12
31

366
"""
# m = 0
# k = int(input())
# j = int(input())
# l = int(input())
# d = j - 1
# days = [31,28,31,30,31,30,31,31,30,31,30,31]
# for p in range(d):
#     m += days[p]
# m += l
# if k % 4 != 0:
#     m += 1
# print(m)




# month_day = [31,28,31,30,31,30,31,31,30,31,30,31]
# year = int(input())
# month = int(input())
# day = int(input())

# ans = 0
# for i in range(month-1):
#     ans += month_day[i]
# ans += day

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     if month > 2:
#         ans += 1

# print(ans)
"""

輸入一個整數 n
使這個n 每回合 - 2 看能扣幾次
**注意扣完不能是負數**
while
輸出扣幾次 

ex
4

2

ex
5

2
"""
n=int(input())
total=0
while(n>0):
    n=n-2
    total=total+1
print(total)
"""
3n + 1

3

7
"""
# n = int(input())
# c = 0
# while n != 1:
#     c += 1
#     if n % 2 == 0:
#         n /= 2 
#     else:
#         n = 3*n + 1
# print(c)

