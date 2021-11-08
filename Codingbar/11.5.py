'''
複習
a = "1-1-1-1"
a.split("-"):   分割字串 => 串列

迭代串列
a = [1,2,3,4,5]
(1) for i in a:
        print(i)    (python有的方式)   (不一定每個語言都有)
(2) for i in range(len(a)): #重要
        print(a[i])     (主要是借用索引值取值的方)
(3) while 方式
a=[1,2,3,4,5]

b=0
while b<len(a):
    print(a[b])
    b=b+1 
'''
# a=[1,2,3,4,5]

# b=0
# while b<len(a):
#     print(a[b])
#     b=b+1 

'''
用while 0 印到 10
'''
# a=0
# while a<=10:
#     print(a)
#     a=a+1 


'''
輸入一個數字
用while迴圈 從 0 印到 你輸入的數字

while 條件式:

'''

# a=0
# b=int(input())
# while a<=b:
#     print(a)
#     a=a+1 




'''
重複輸入數字 直到0結束
再輸入 一個數字 x

印出 一個串列 (裡面沒有x)

過濾方式


print(串列)
'''
# word=[]
# while True:
#     data=input()
#     if data=="0":
#         break
#     word.append(data)
# delete=input()
# ans=[]
# for i in word:
#     if delete!=i:
#         ans.append(i)

# print(ans)



'''
實作.join()
'''


'''
字串的切片取值
s = "123456"
print(s[1:4])   =>  "234"

串列的切片串列
a = [1,2,3,4,5,6]
a[首項:末項:間隔]
print(a[0:1])
print(a[0])
'''
# a = [1,2,3,4,5,6]
# print(a[0:1])   #串列   串列的切片取串列
# print(a[0])     #值 索引值取值


'''
輸入一行數字 每個之間用空格隔開
輸入 首相
    末項
    間隔

印出 範圍的串列

1 2 3 4 5 6 7

2
5
2

[3,5]
'''
# number = input()
# a=number.split()
# f=int(input())
# l=int(input())
# d=int(input())
# ans=[]
# for i in range(f,l,d):
#     b=a[i]
#     ans.append(b)
# print(ans)

'''
a = [1,2,3,4,5,6]
印出 4 的 索引值

'''
# number=[1,2,3,4,5,6]
# b=len(number)
# a=0
# for i in range(len(number)):    #括號內的先做
#     if number[i]==4:
#         print(i)
#         break
'''
list.index(要尋找的內容)
串列
'''
# number=[1,2,3,5,6]
# print(number.index(4))