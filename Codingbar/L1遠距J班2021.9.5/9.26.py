'''
string = "1234567"
string[3] 索引值取值

string[首相:末項:間隔] #末項不會取到
string[4:-1]
string[:4]
string[4:]
'''
# string = "1234567"
# print(string[1:4])
# for i in range(5):   #預設起始位置 0 
#    print(i)
# a = "123"
# b = "345"
# s = a + b
# print(s)

# s = ""
# for i in range(5):
#    s = s + str(i)
# print(s)

'''
複習 文字相加
重複輸入文字，累加到一個變數，輸入no 結束，印出這個變數

ap
pple
no

appple

'''



'''
x = ""
for i in range()

print(x)
01234

實作切片取值
建立字串 s = "123456789"
輸入 
字串
起始
末項
間隔

輸出 值

ex
123456789
3
7
1

4567
'''

# n=input().split()
# a=int(input())
# b=int(input())
# c=int(input())
# for i in range(a,b,c):
#    l=''
#    l+=n[i]
# print(l)


print("011m1".split("1"))






# num = input().split(",")
# s = input()

# t = ['個','十','百','千','萬','十萬','百萬','千萬','億']

# for i in range(len(t)):
#     if t[i] == s:
#         print(i,-(i//3+1),-(i%3+1),num)
#         print(num[-(i//3+1)][-(i%3+1)])
#         break

'''
輸入一串數字 有兩個逗號 每三個數字有一個逗號 請先用.split()分割
123,888,333
輸入數字 印出數字上的數字
ex 
123,888,333
123
888
333


3 8


8 3
7 3
6 8

['123', '888', '333']
123888333
012345678
'''
# s = input().split(",")

# print(s[1][1])

# print(s[2][1])
# (7//3) == 2
# (7%3) == 1

# 6 
# s[2][0]
# print(s[2][1])

'''
輸入一個數字 判斷質數 True質數 False 

'''

# a = int(input())
# i = 2
# while a > i:
#     if a % i == 0:
#         print(False)
#         break
#     i += 1

# if a == i:
#     print(True)


# for i in range(5):
#    print(i)
#    break
# else:
#    print("123")

# for i in range(5):
#    print(i)
#    if i == 5:
#       break
# else: #for迴圈裡的 break 有執行 就不會執行else
#    print("123")

'''
產生
(1) range(5) 產生 0 1 2 3 4
(2) i = 0 0 儲存到 i
(3) print(i)
(4) 判斷 i == 5 產生布林值 False 
(5) i = 1
(6) print(i)
(7) 判斷 i == 5 產生布林值 False
(8) i = 2
9 print(i)
10 判斷 i == 5 產生布林值 False
11 i = 2

'''