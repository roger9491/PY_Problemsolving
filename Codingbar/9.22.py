'''
自學:
bilibili 推薦
知乎
博客原


練習解題:
codeforces
落谷


輸入一個整數 判斷 是否是質數
True    False
a = {1:2}

2~(n-1)
'''

# n=int(input())
# s=2
# while n!=1:
#     if s==n:
#         print('True')
#         break
#     elif n%s==0:
#         print('False')
#         break
#     else:
#         s+=1

# n = int(input())
# for i in range(2,n):#2~n-1
#     if n % i == 0:
#         print('False')
#         break   #中斷迴圈
# else: #先決條件 迴圈執行完整
#     print("True")


#     #   0    1   2   3     4     5
# a = ["s6","c6","s9","h3","d9","c4"]
# for i in range(len(a)): #0 1 2 3 4 5    #末項本身不會產生
#     print("i",i)
#     print("a[i]",a[i]) #索引值取值
#     print(a[i][-1])
#     # print(a[i])

'''
二進制 2進位
10 進制

0 ~ 9

0       # 0
    1 個 # 1
1   0  # 2
11  # 3
100 # 4
101 # 5
110 # 6
111 # 7
1000 # 8
1   0   0   0
2**3 2**2    2**1    2**0

'''

n=input().split('1')
zero=0
a = "" 
for i in n:
    zero+=1
print(zero)
