# a = "1 2 3 4 5"
# print(a.split())
# a = "1-2-3-4-5"
# print(a.split("-"))
# #type()  #確認型態
# t = a.split("-")
# print(type(t))
# a = "1-2-3--"
# print(a.split("-"))     #['1', '2', '3', '', '']  
#.split() 分割字串 => 串列
#.split() 功能 分割字串 重點: 西瓜刀

'''
首項
末項
間隔

2
5
2

35
'''
# string="123456"
# f=int(input())
# l=int(input())
# d=int(input())
# a=""
# for i in range(f,l,d):
#     a=a+string
# print(a)


'''
輸入 一行數字 中間會有空格
1 5 2 8 4


輸出
1 < 5
5 > 2
2 < 8
8 > 4

'''
# string=input("")
# c=string.split()
# a=list(map(int,c))
# b=len(a)
# for i in range(b):
#     print(i)
#     if a[i+1]>a[i]:
#         print(a[i]," < ",a[i+1])
#     elif a[i+1]<a[i]:
#         print(a[i]," > ",a[i+1])

# a=int(input())  #5
# b = []
# for i in range(a):
#     data=input("")
#     b.append(int(data))
# # print(b)
# # c=b.split()
# # d=list(map(int,c))
# '''
# 5 10 11 7 9 12
# [5,10,11,7,9,12]
# [5,10,11,7,9,12]
# []
# '''


# print("d",d)
# e=len(d)
# ans=""
# print("e",e)
# #有問題
# for q in range(e-1):
#     if d[q]<d[q+1]:
#         ans=ans+str(1)
#     elif d[q]>d[q+1]:
#         ans=ans+str(0)
# # for i in range(0):
# #     print(i)
# # for i in range(負):
# #     print(i)
# print(ans)
'''
5
10
11
7
9
12


1011    
'''
#split() 字串分割 => 串列
#str.join(串列名稱)  #  合併串列 => 字串    文字型態

a = ["a","b","c"]
t = "x".join(a)
print(t)
'''
作業
建立好串列
輸入 合併的文字

輸出 合併得結果



'''