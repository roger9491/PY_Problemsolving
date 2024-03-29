'''

函式


ex 
s = "123"
print(len(s))   

建立函式

你想要把值丟給函式，必須要有參數
如果你想要函式有回傳值，必須要有return 


#定義
def len1(s1):
    c = 0
    for i in s1:
        c += 1
    return c
'''

#定義
# def len1(s1):
#     c = 0
#     for i in s1:
#         c += 1
#     return c
    

'''
遞迴

函式執行自己

'''
'''
無窮
'''
# def f():
#     print(1)
#     f()     #函式執行自己

# f()     #執行函式

'''
停止

return 結束的是當前的函式
'''
# def h():
#     print(1)
#     h()
#     return 
# h()

'''
函式執行自己
如果某一個問題，每一個階段的問題解法規則都是一樣的
就可以用遞迴解決

印出 1 ~ 程式crash
1
2
3
4
5
.
.
.
.
.
函式執行自己，要加 1
參數：參數可以把值傳進函式

'''
# def h(n):
#     print(n)
#     # n = n + 1
#     # h(n)
#     h(n+1)
#     return 
# h(1)




'''
印出 1 ~ 100
1
2
3
4
5
.
.
.
.
.
函式執行自己，要加 1
參數：參數可以把值傳進函式

'''
# def h(n):
#     # if n == 101:
#     #     return
#     print(n)
#     if n == 100:
#         return
#     # n = n + 1
#     # h(n)
#     h(n+1)

# h(1)

'''
1 + 2 + 3 + ... + 100
1   2   3   4   5   6   7   8  8個階段
前面階段的總和 + 當前階段的數字
1
    1 + 2
        3 + 3
            6 + 4
                10 + 5


(1) for
(2) while
total = 0   #累加的結果
c = 1   #要加的值
while c <= 100:
    total += c
    c += 1
print(total)
(3) 遞迴
1   2   3   4   5   6   7   8  8個階段
前面階段的總和 + 當前階段的數字
1
    1 + 2
        3 + 3
            6 + 4
                10 + 5

1 + 2 + 3 + + 4 + 5 + .. +100


ex 
1 + 1 + 1 + .. + 1  100個加1
1 2 3 4 5 6 7 8
'''
# def f(n,total):
#     total += 1
#     if n == 100:
#         print(total)
#         return
#     else:
#         n += 1
#         f(n,total)

# f(1,0)
'''
print版本
1 + 2 + 3 + + 4 + 5 + .. +100

'''
# def f(n,total):
#     total += n
#     if n == 100:
#         print(total)
#         return
#     else:
#         n += 1
#         f(n,total)

# f(1,0)
'''
1 + 2 + 3 + + 4 + 5 + .. +100
如何讓你的函式回傳結果

None: 空 ， 沒有

'''
# def h(n,total):
#     total=total+n
#     n=n+1
#     if n==101:
#         return total
#     h(n,total)

# print(h(1,0))

'''
1 + 2 + 3 + 4 + 5

'''
# def h(n,total):
#     if n==6:
#         return total
#     return h(n+1,total+n)
# print(h(1,0))

'''
1 + 2 + 3 ..  + 100


'''

# def h(n,total):
#     if n==101:
#         return total
#     return h(n+1,total+n)
# print(h(1,0))


'''
1*2*3*...*n

'''
# def h(n,total):
#     if n==101:
#         return total
#     return h(n+1,total+n)
# print(h(1,0))

'''
遞迴速寫
如果某一個問題，每一個階段的問題解法規則都是一樣的
ex.
1 + 2 + 3 ..  + 100

f(n): n 階段的結果
f(100): 5050
1 + 2 + 3 +...+ 50
f(50) = 1 + 2 + 3 +...+ 50

f(n) = f(n-1) + n
邊界 1

遞迴關係式
f(n) = f(n-1) + n

邊界
f(1) = 1
'''
# def f(n):
#     if n == 1:
#         return 1
#     return f(n-1) + n
# print(f(100))
'''
階層
1*2*3*..*n
5! 5*4!
n! n*(n-1)!
4!=4*3!
n! n*(n-1)!
f(n) = f(n-1)*n
f(100) = 1*2*3*..*100 
f(99) = 1*2*3*..*99

遞迴關係式
f(n) = f(n-1) * n

邊界
f(1) = 1
'''
# def f(n):
#     if n == 1:
#         return 1
#     return f(n-1) * n
# print(f(100))
    
