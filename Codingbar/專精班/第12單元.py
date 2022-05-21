'''
最大公因數

10
45

5
'''

# a = int(input())
# b = int(input())

# while a % b != 0:
#     c = a % b
#     a = b 
#     b = c
# print(b)


'''
化簡分數
96
18

16/3
'''
n1 = int(input())
n2 = int(input())

a = n1 
b = n2 

while a % b != 0:
    c = a % b
    a = b 
    b = c

print(n1//b,"/",n2//b)