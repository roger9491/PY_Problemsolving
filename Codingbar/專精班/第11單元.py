'''
質數: 因數只有 他自己 和 1
不是質數: 因數不只有 他自己 和 1
         1 ~ 自己
         2 ~ 自己 - 1


'''

'''
輸入 英文字串
若是字串裡有 a和s
且a在s前面出現
印出True
否 False

ex 
(1)
aksdlkoew
True
(2)
asda kk
True
(3)
ahfgh
False
(4)
sad kk
False
'''

# string = input()
# flag = False

# for i in range(len(string)):
#     if string[i] == "a":
#         flag = True
#     elif string[i] == "s":
#         if flag:
#             print(True)
#             break
# else:
#     print(False)


"""
英打比賽


123 word 123arduino
1a1 QQ I don't know.
0


2
6
"""


# lower_letter = "abcdefghijklmnopqrstuvwxyz"
# upper_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# while True:
#     string = input()

#     if string == "0":
#         break
    
#     flag = False
#     ans = 0
#     for i in range(len(string)):
#         if string[i] not in lower_letter+upper_letter:
#             if flag:
#                 ans += 1
#                 flag = False
#         else:
#             flag = True
    
#     if flag:
#         ans += 1
    
#     print(ans)

'''
郵件檢驗


1.是否只包含一個@
2.網域是否正確含有.

名稱不要有 大寫 和 特殊符號
'''

# symbols = "!@#$%^&*()_+-=/{}[]\|;:/?,.<>"
# chars_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# email = input()

# if "@" not in email:
#     print(False)
# else:
#     #如何確認 @ 只有一個?
#     #如何分成 兩個部分?
#     c = 0
#     for i in email:
#         if i == "@":
#             c += 1
#     if c > 1:
#         print(False)
#     else:
#         account = ""
#         domain =  ""
#         flag = 0
#         for i in email:
#             if i == "@":
#                 flag = 1
#             else:
#                 if flag == 0:
#                     account += i
#                 elif flag:
#                     domain += i
#         if "." not in domain:
#             print(False)
#         else:
#             flag1 = 0
#             flag2 = 0
#             for i in account:
#                 if i in symbols:
#                     flag1 += 1
#                 elif i in chars_b:
#                     flag2 += 1
#             if flag1 or flag2:
#                 print(False)
#             else:
#                 print(True)

'''
密碼強度檢驗

airabbi
False
'''


# symbols = "!@#$%^&*()_+-=/{}[]\|;:/?,.<>"
# chars = "abcdefghijklmnopqrstuvwxyz"
# chars_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# nums = "0123456789"
# word = symbols + chars + chars_b + nums
# password = input()

# if len(password) >= 8:
#     flag = 0
#     for i in password:
#         if i not in word:
#             break
#     else:
#         flag = 1
    
#     if flag:
#         flag1 = 0
#         flag2 = 0
#         flag3 = 0

#         for i in password:
#             if i in nums:
#                 flag1 = 1
#             elif i in chars + chars_b:
#                 flag2 = 1
#             elif i in symbols:
#                 flag3 = 1

#         if flag1 and flag2 and flag3:
#             if password[0] in chars_b:
#                 print("高")
#             else:
#                 print("中")

#         else:
#             print("低")
#     else:
#         print(False)
# else:
#     print(False)
'''
密碼須皆由 數字 或 字母 或 特殊符號 組成

輸入字串
'''





'''
布林表 練習
50
2
7
9
9
40
2
30
50
no


2 2
7 1
9 2
30 1
40 1
50 2
'''
# matrix = [0]*10000
# while True:
#     n = input()

#     if n == "no":
#         break
    
#     matrix[int(n)] += 1


# for i in range(10000):
#     if matrix[i] > 0:
#         print(i, matrix[i])


'''
速解
ascii
ord()   轉ascii
chr()   轉文字

英文拼字表


1 xor 0 = 1
0 xor 1 = 1
1 xor 1 = 0
0 xor 0 = 0


1 ~ 26

5
abcde

'''
# string = input()
# boolean_table = [False for i in range(26)]

# for i in string:
#     if boolean_table[ord(i) - 97] == False:
#         boolean_table[ord(i) - 97] = True
#     elif boolean_table[ord(i) - 97] == True:
#         print(True)
#         break
# else:
#     print(False)



# a = [1,2,3,4,12,5,23,12,3123,124]
# t = 0
# for i in range(len(a)):
#     t += a[i]
# print(t)


# a = [1,2,3,4,12,5,23,12,3123,124]
# #不要用max()
# maxv = -10**9
# for i in range(len(a)):
#     if a[i] > maxv:
#         maxv = a[i]


# print(maxv)

# a.sort()    #小~大
# print(a)


'''
輸入兩行數字 
輸出最大公因數
'''