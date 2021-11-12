
'''
range(末項) : 產生數字不會到末項本身，預設是 0 開始
range(首項,末項) 產生數字不會到末項本身
range(首項,末項,間隔) ex 0 , 13 , 3 => 0 3 6 9 12

while 迴圈:

怎麼判斷 字串 在 字串裡
in
if a in b:

print("誠實村")
break 跳出迴圈

for....else: for迴圈完整執行完，else:才會執行
for     :

else:
'''

'''
判斷質數

質數:除了 一 和 自己 可以整除，其他數都不能整除
    
True/False


'''
'''
錯誤的時機?

前提是 n 不是質數

'''
# n=int(input())
# a=2
# for i in range(n):
#     if n%a==0:
#         print("False")
#         break
#     a+1
# else:
#     print("True")


'''
2 ~ n-1

'''
# n=int(input())

# for i in range(2,n):
#     if n%i==0:
#         print("False")
#         break
# else:     如果 迴圈成立(沒有被break) 就會 執行
#            True數字是質數
#           for 用來檢驗 數字有沒有被 2 ~ n-1整除
#     print("True")
'''
2 ~ n-1
迴圈不能搭配else

'''
# n=int(input())
# flag = 0
# for i in range(2,n):
#     if n%i==0: #(1) 檢驗 有沒有被 2 ~ n - 1 整除
#         print("False")
#         flag = 1
#         break

# if flag == 0:
#     print("True")   #(1)如果有成立   就不做

#1 3 6 7 8
n = input().split()

print(n)
'''
字串.split("基準"): 分割字串 => 串列
int(串列) 不行
int(值)

串列裡的每一個值都改型態
list(map(型態名稱,串列))
27 - 21 = 6
max(串列)   #找最大值
min(串列)   #找最小值
sum(串列)   #找總和
變數 = max(串列) - min(串列)

'''

# n=list(map(int,input().split()))
# totle=0
# buy=0
# for i in range(n[0]):
#     a=list(map(int,input().split()))
#     if max(a)-min(a)>=n[1]:
#         totle=totle+((a[0]+a[1]+a[2])//3)
#         buy+=1
#         # print(buy,totle)

# print(buy,totle)


'''
如何知道串列長度?
len(串列/字串) 

sum()，不能用
輸入一串數字 空格隔開
1 4 6 7
輸出 總和
18

max()

min()

'''

# n=list(map(int,input().split()))
# t=0
# for i in range(len(n)): #迭代串列
#       t=t+n[i]
#       print(t)
# print(t)

#程式 = 演算法 + 物件導向