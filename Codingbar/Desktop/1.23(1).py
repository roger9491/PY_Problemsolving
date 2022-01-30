'''
輸入一個整數


判斷是否為質數 yes no


質數: 除了一和自己以外都不能整除

檢驗方式: 除了一和自己，n % 所有數字(除了一和自己) != 0:
                        如果上面所說的條件成立 print("yes")質數(所有的數字跑完)
                        如果上面所說的條件不成立 print("no") (只要有任何一個)
'''

# n = int(input())
# for i in range(2,n):#234
#     if n % i == 0:
#         print("no")
#         break
# else:   #for 迴圈必須沒有被中斷
#     print("yes")

#for ... else:
# text = "Leetcode is cool"
# text = list(text.split())
# ans = ""
# a = []
# for i in range(len(text)):
#     a.append(len(text[i]))
# a.sort()
# for i in range(len(text)):
#     for j in range(len(text)):
#         if a[i]==len(text[j]):
#             if i==0:
#                 text[i]=text[i][0].upper()+text[i][1:]
#             else:
#                 text[i]=text[i].lower()
#             ans+=text[i]
#             ans+=" "
#             break
# print(ans)

'''
range(首相,末項,-1)
range(首相,-1,-1)
       
'''

# a = [4,2,3,3,2]
# index = 2
# #
'''

灌溉田地

'''
# n = int(input())
# count = 1
# b = list(map(int,input().split()))
# c = []
# for j in range(n):
#     for i in range(j-1,0,-1):
#         if i==j-1:
#             if b[j]>=b[i]:
#                 count+=1
#             else:
#                 break
#         else:
#             if b[i]>=b[i-1]:
#                 count+=1
#             else:
#                 break
#     for i in range(j+1,n-1):
#         if i == j+1:
#             if b[j]>=b[i]:
#                 count+=1
#             else:
#                 break
#         else:
#             if b[i]>=b[i+1]:
#                 count+=1
#             else:
#                 break
#     print(j,count)
#     c.append(count)
#     count = 0
# print(max(c))

# a = [[],1,2]
# a.remove([])
# print(a)
'''
5
1 2 1 2 1

'''


# target = int(input())
# a=[]
# ans = []
# count = 0
# for i in range(1,target):
#     count = 0
#     a = []
#     # print(i)
#     for j in range(i,target):
#         count+=j
#         a.append(j)
#         if count==target:
#             # print(a)
#             ans.append(a)
#             break
#         elif count>target:
#             break
# print(ans)
#過濾


# a = [1,2,3]
# ans = []
# ans.append(a)
# print(ans)
# a[0] = 7
# print(ans)

'''
排列組合
a b c d


'''
# import  itertools
# from ntpath import join

# a = ['a','b','c','d']

# list1 = list(itertools.permutations(a,2))
# print(list1)
# for i in list1:
#     print(list(i))

# #串列 => 字串
# a = ["roger","apple"]   #roger apple
# print(" ".join(a))

# text = "Leetcode is cool"
# text = list(text.split())
# ans = ""
# a = []
# for i in range(len(text)):
#     a.append(len(text[i]))
# a.sort()
# for i in range(len(text)):
#     for j in range(len(text)):
#         if a[i]==len(text[j]):
#             if i==0:
#                 text[i]=text[i][0].upper()+text[i][1:]
#             else:
#                 text[i]=text[i].lower()
#             ans+=text[i]
#             ans+=" "
#             break
# print(ans)


a = 1
b = a 
b = (a+4)*4/2 - 10
c = int(input())

print(c/b)



"asd1231970909中ㄚ"