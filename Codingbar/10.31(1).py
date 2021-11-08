'''
輸入一個整數
判斷是不是質數

True/False


'''
# a=int(input())
# b=0
# for i in range(a):
#     if a%(i+1)==0:
#         b=b+1
# if b>2 or b==1:
#     print(False)
# elif b==2:
#     print(True)

# number = int(input())
# for i in range (2,number):
#     if number % i == 0:
#         print("false")
#         break
# else:
#     print("True")


'''

輸入 n

'''
# n = int(input())
# print(n)
# while n != 1:
#     if n %2 == 1:
#         n = 3*n +1
#     else:
#         n = n/2
#     print(int(n))
# range():不會產生到末項本身
# str() 轉換文字
#文字相加
# for i in range(1,11):   #1~10
#     for a in range(10,-1,-1):   #10~0
#         if i==a:
#             print(i)

# i = 1
# j = 10
# while i<=10:
#     i+=1
#     while j>=0:
#         j-=1
#         if i == j:
#             print(i)
# for i in range(1,10):
#     print(i)

# b=str()
# for i in range(1,11):
#     for a in range(10,-1,-1):
#         if i==a:
#             b=b+str(i)
# print(b)
c = ""
for i in range(1,11):
    for a in range(10,-1,-1):
        if i==a:
            c = c+str(i)
print(c)

# 文字相加 str()

