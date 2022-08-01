
# while True:
#     try:
#         r, c, m = map(int,input().split())
        
#         matrix = []
#         for i in range(r):
#             a = list(map(int,input().split()))
#             matrix.append(a)

#         c = list(map(int,input().split()))
        

#     except:
#         break
'''
1 8
5
1 8 0
5 6 0
2 7 0
8 1 0
33 22 0

'''



'''
二維矩陣
a = [1,2,'3',4,5,[1,2,3]]   #二維串列

#      r1   r2    r3
a = [[1,4],[2,5],[3,6]]
print(a[0])
print(a[1])

#    c1 c2
a = [[1,4],     #r1
     [2,5],     #r2
     [3,6]]     #r3

a[0][1]
'''


'''
排序串列
a = [5,3,7,1,3,4]
a.sort()
print(a)

None: 空

int():轉整數
int('a')
'''

#定義函式
# def check_even(number):
#     if number % 2 == 0:
#         print(True)
#     else:
#         print(False)


# n = int(input())

# check_even(n)
# if n % 2 == 0:
#     print(True)
# else:
#     print(False)


'''
產生亂數
'''
# import random
# a = random.randint(1,100)
# t = []
# for i in range(4):
#     t.append(random.randint(1,100))
# print(a)
# print(t)




'''
return
(1)回傳值
(2)跳出函式/結束函式

'''

#定義函式
# def check_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#     print(1)    #無意義

# n = int(input())
# c = check_even(n)
# print(c)

'''
global

可以查看外面的a
def f():
    c = 1
    print(a + c)
a = 1
f()

兩個a不相同
def f():
    c = 1
    a = 0
    print(a + c)
a = 1
f()
print(a)

修改函式外的a
def f():
    global a #全域變數
    c = 1
    a = 5
    print(a + c)
a = 1
f()
print(a)
'''

'''
判斷迴文(正看 == 倒看)

輸入一串文字
輸出 是 / 不是



ex
12345
不是

assbssa
迴文

12321
是
'''

#(正看 == 倒看)
# a = input()

# s = ""
# for i in range(len(a)-1,-1,-1):
#     s += a[i]

# if a == s:
#     print('是')
# else:
#     print('不是')

#(鏡面)
# a = input()

# s = ""
# for i in range(len(a)//2):
#     if a[i] != a[-(i+1)]:
#         print('不是')
#         break
# else:
#     print("是")


'''
遞迴

函式執行自己

'''

'''
無窮
'''
# def f():
#     print(1)
#     f()

# f()


'''
停止
'''
# def h():
#     print(1)
#     return 
#     h()
# h()


'''
1 + 2 + 3 + ... + 100

'''

# for
# t = 0
# for i in range(101):
#     t += i
# print(t)

# while

# t = 0
# c = 1
# while c <= 100:
#     t += c
#     c += 1
# print(t)


# 1   2
# 1 + 2
# 遞迴
# 1 + 2 + 3 + 4
# def h(n):
#     if n == 100:
#         return n
#     # print(n)
#     return h(n+1) + n

# c = h(0)
# print(c)

'''
h(0) = h(0+1) + 0           10
        h(1) = h(1+1) + 1   10
               h(2) = h(3) + 2  9
                      h(3) = h(4) + 3  7 
                             h(4) = 4

'''
