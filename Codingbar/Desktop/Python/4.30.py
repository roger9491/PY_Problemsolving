'''
基礎班-> 專精 -> L1 -> L2 -> L3

輸出
print()


型態
    文字
    ""
    ''
    數字
        整數
        浮點數 小數點
        a = 1
        a = 1.0
    布林值
        True False

數字運算
n1 = int(input())
n2 = int(input())
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)    #浮點數
print(n1**n2)
print(n1%n2)
print(n1//n2)

文字運算
+
*

布林值運算
and         or      not
和，並
True and False => False
1     *    0   == 0

變數
name = "鍋貼"
number = 123


輸入
a = input() #文字型態

= : 把右邊的東西儲存在左邊
==: 判斷是不是一樣 
條件控制
輸入一個整數
判斷是否為偶數
是 印True
否 印False


迴圈
印出 0 ~ 9
for i in range():



range(末項):    0 ~ 末項-1
range(首相,末項):   首相~末項-1
range(首相,末項,間隔)   ex range(1,8,2): 1,3,5,7


while 布林值:   True 就會重複執行  

誰產生布林值: 條件判斷式

字串
a = "12345"
a[2]
a = "12345"
for i in a:
    print(i)

串列
a = []
ex a = [1,2,3,4,5]
a[索引值]
a.append(1)
del a[索引值]
a = [1,2,3,4,5]
for i in range(len(a)):
    print(a[i])

'''
a = [1,2,3,4,5]
for i in range(len(a)):
    print(a[i])











'''
雞兔同籠

暴力版

30  隻數
72  腳數

24 6
雞 兔子
'''
# t = int(input())
# f = int(input())

# for i in range(1,31): 
#     r = f - 2*i
#     # print(r)
#     if r % 4 == 0:
#         if  t - i == r // 4:
#             print(i,t-i)
#             break
# else:
#     print("無解")
'''
速解
'''

# t = int(input())
# f = int(input())

# if f/2 - t >= 0 and int(f/2 - t) == f/2 - t:
#     print(int(t - f/2 + t),int(f/2 - t))
# else:
#     print("wrong")