'''
重複輸入
輸入no停止
輸入存到串列



輸入一個數字n，輸出n在串列的個數

# 重複輸入數字n
# 輸出n 在串列的個數
# 直到輸入no停止

印出串列的長度
ex
1
1
2
2
no
1
2
2
2
no
4


'''
# c = []
# while True:
#     a = input("")
#     if a == "no":
#         break
#     else:
#         c.append(int(a))
# b = int(input())
# t = 0
# for i in range(len(c)):
#     if b == c[i]:
#         t += 1
# print(t)




"""
投票統計

"""

# t = []
# while True:
#     n = input()
#     if n == "no":
#         break
#     t.append(n)

# for i in range(len(t)):
#     if t.count(t[i]) > len(t) // 2:
#         print(t[i])
#         break


'''
隱藏謊言前置

輸入 1 + n 列，
第一列輸入 n 
接下來輸入n個數
加到串列裡

印出串列

ex
5
1
2
3
4
5

[1,2,3,4,5]


'''
# n=int(input())
# m=[]
# for i in range(n+1):
#     i=int(input())
#     m.append(i)
# print(m)



'''
重複輸入長度為2字串 英文配數字  a2 a6 a7
若是字串的數字能被2整除就印出來
輸入no結束


ex.

a2
a6
c7
no

a2
a6


'''

# while True:
#     n=input()
#     if n == "no":
#         break
#     elif int(n[1])%2==0:
#         print(n)
# while True:
#     g = input()
#     if g == 'no':
#         break
#     if int(g[1]) % 2 == 0:
#         print(g)

'''
a = ["a4","b3",c6]
輸入一行字串 長度為2字串 英文配數字
印出 數字一樣的字串

ex
x3

x3 b3

if a in b:
        串列

c5


'''
# a = ["a4","b3",'c6']
# a[0][1]
# a[0] = "a4"
# a[1]
# b = "a4"
# b[1]
# n = input()
# for i in range(len(a)):
#     if int(n[2]) == int(a[2])
#     print(n,a)


'''
成雙成對
s6
c6
s9
h3
d9
c4
no

s6 c6
s9 d9
['h3', 'c4']
'''

# t = []
# while True:
#     n = input()
    
#     if n == "no":
#         break
    
#     for i in range(len(t)):
#         if t[i][1] == n[1]:
#             print(t[i],n)
#             del t[i]
#             break
#     else:
#         t.append(n)
# print(t)


# word="apple"
# i=0
# while i<len(word):
#     print(word[i])


'''

輸入一個字串
判斷有幾個母音
aeiou
輸出 幾個母音


ex
a p p p p a i o i a s d l e 

2
if a in b:
'''

# s = input()
# c = 0

# for i in s:
#     if i in "aeiou":
#         c += 1
    # if i == "a" or "e" == i or "o" 

# for i in range(len(s)): s[i]

# n=input()   #1234
#             #0123
# # print(n[0])
# for i in range(len(n)): #n[i]
#     if n[i] == '4':
#         print(4)