'''
輸入 一個數字

質數 True / 不是質數 false

'''
# number=int(input())
# total=0
# for i in range(1,number+1):
#     if number%i==0:
#         total=total+1
#     else:
#         pass
# if total==2:
#     print("True")
# else:
#     print("False")

#簡化
# number=int(input())
# total=0
# for i in range(2,number):
#     if number%i==0:
#         total=total+1
#         print("False")
#         break

# if total == 0:
#     print("True")


'''
質數的定義 只能被 1 和 自己整除
首相 2  末項 number - 1
利用break 特性
'''
# number=int(input())

# for i in range(2,number):
#     if number%i == 0:
#         print("False")
#         break
# else:   #for 迴圈執行完整
#     print("True")

'''
實作 string[首:末:間]
ex string[]
輸入
首項
末項
間格

輸出

ex
2
6
2

35


先備知識
印出字串裡的所有字
一行一行的印
a = "12"
b = "34"
c = a + b
a = a + string
'''
# string="1234567"
# f=int(input())
# l=int(input())
# d=int(input())
# a=""
# for i in range(f,l,d):
#     a=a+string[i]
# print(a)
# string = "12345"
# a = "abc"
#重複的事情
#len(字串):回傳字串的長度
# for i in range(len(string)):
#     print(string[i])
# for i in range(len(string)):
#     a=a+string[i]
#     print(a)
#a = "abc12345"

'''
實作 split()
'''
string = "121131"
print(string.split("1"))