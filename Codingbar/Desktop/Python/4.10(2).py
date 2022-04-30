# n = int(input())
# num = [1,2,3,4,5,6,7,8,9]
# count = []
# flag = True
# while True:
#     if n == 1:
#         break
#     for i in range(9,1,-1):
#         if n%i==0:
#             count.append(i)
#             n = n/i
#             break
#     else:
#         break
#     print(count)
# count.sort()
# count = list(map(str,count))
# if count == []:
#     print(-1)
# else:
#     print("".join(count))



#10**6~10**7

#  from functools import cmp_to_key
# def f(a,b):
#     if int(a+b) < int(b+a):
#         return -1   #交換 a 和 b
#     else:
#         return 1

# n = int(input())

# t = []
# for i in range(n):
#     num = input()
#     t.append(num)

# # for i in range(n):
# #     for j in range(n-1-i):
# #         if int(t[j]+t[j+1]) < int(t[j+1] + t[j]):
# #             temp = t[j]
# #             t[j] = t[j+1]
# #             t[j+1] = temp
# t.sort(reverse=True,key=cmp_to_key(f))

# # 5 5111
# # 5111 521
# # 5215111
# print("".join(t))

'''
[1,2,3] [4,5,6]
[[1,4],[2,5],[3,6]]


'''