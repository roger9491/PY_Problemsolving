'''
輸入 首項
末項
間隔


印出範圍字串

ex
2
7
2

357
[首相:末項:間隔]
s[2:7:2]
文字相加
s[index]
'''
# s = "12345678"
# a = int(input())
# b = int(input())
# c = int(input())
# print(s[a:b:c])
# count = ""

# for i in range(a,b,c):  #range(首相,末項,間隔)
#     print(i)
#     count += s[i]

# print(count)



# s = input() #['1','2']
# t = []

# t = ['1','2']

'''

被分割的字串.split(分割的基準字串)
西瓜刀
"a+b+c+d" => ['a','b','c','d']


1 2 3 4 5 6

輸入 數列 每一個數字空格分開
87 1 3 5 2 1 343 
[::-1] a[]
輸出 
[87,1,3,5,2,1,343]



[1,2,5,3,1,87]
串列.append(data)
'''
# a = "a+b+c++".split("+")
# print(a)

# a = input()
# a = a.split()
# b = []      #負責產生數字 索引值
# for i in range(len(a)-1,-1,-1): #6 5 4 3 2 1 0
#     print(i)
#     b.append(a[i])
# print(b)
# #87 1 3 5 2 1 334
# a=input()
# a=a.split()     #中間
# for i in range(len(a)//2): # 0 ~ 2
#     if i > len(a)//2:
#         break
#     b=a[len(a)-i-1]
#     a[len(a)-i-1]=a[i]
#     a[i]=b
# print(a)
'''
輸入 數列 每一個數字空格分開


輸出總和
sum(串列)
# int(串列)

串列 每一個資料轉型態
map(型態, 串列)
list()轉成串列
'''
# a = input().split()
# a = map(int,a)
# a = list(a)
# print(a)

# a = list(map(int,input().split()))
# print(a)

'''
輸入字串
Abcd
輸出 一行一行印每一個字
A
b
c
d
'''

'''
if a in b:  
(1) a 字串/字元 b 串列/字串
(2) a 任何型態 b 串列
實作 if 字元 in 字串
輸入 
字串
字元

輸出
yes no
'''



'''
輸入
字串
if a in b:
印出字串裡的數字

acasasdd123121233fgssdaasd
123121233
'''



'''
輸入
字串

印出字串裡的數字


aa11bb22cc44dd


11
22
44

'''
# a=input()
# b=''
# for i in range(len(a)):
#     if a[i] in "1234567890":
#         b=b+a[i]
#     else:
#         if b!='':
#             print(b)
#             b=''

a = input()
total = ""
b = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(a)):
    if a[i] not in b:
        total+=a[i]
    else:
        if total != "":
            print(total)
        total = ""
'''

輸入
字串

印出字串裡的數字

1231c123fg12asd12asd1231
1
123
12
12
'''
# a=input()
# b=''
# a=a+"a"
# for i in range(len(a)):
#     if a[i] in "1234567890":
#         b=b+a[i]
#     else:
#         if b!='':
#             print(b)
#             b=''

a = input()
total = ""
a += "dkaniv"
b = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(a)):
    if a[i] not in b:
        total+=a[i]
    else:
        if total != "":
            print(total)
        total = ""