'''
快速冪
x**y % p
2 5

1 2 4

19
10011
16 2 1

10010

'''
def exp(x, y, p):
    # print(x, y, p)
    if y == 0:
        return 1
    if y % 2 != 0:
        return (exp(x, y-1, p)*x)%p
    
    t = exp(x, y/2, p)
    return (t*t)%p

# def exp2(x, y, p):
#     i = 1
#     t = 1
#     while y != 0:
#         if y % 2 != 0:
#             # print("xx",t,i,x)
#             t = (t * (x**i)) % p
#             # print(t)
#             y -= 1
#             y /= 2
#             i *= 2
#         else:
#             y /= 2
#             i = i * 2
#         # print(y,t,i)
#     return t 




while True:
    try:
        x = int(input())
        y = int(input())
        p = int(input())
        print(exp(x, y, p))
    except:
        break

# print(exp(x, y, p))









