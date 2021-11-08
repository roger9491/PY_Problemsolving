'''
輸入 整數
判斷 是不是質數

是 True
否 False

'''
# n = int(input())
# for i in range(2,n):    #2 ~ n - 1
#     if n % i ==0:
#         print('False')
#         break
# else:   #for 沒有遇到 break時 就會執行
#     print('True')

# n = int(input())
# a = 0
# for i in range(2,n):
#     if n % i ==0:
#         a += 1
#         break

# if a == 0:
#     print('True')
# else:
#     print('False')

'''
range(末項): 產生數字 0 ~ 末項 - 1
range(首項,末項) 產生 首項 ~ 末項-1
range(首項,末項,間隔)
'''

'''
輸入
首項
末項
間隔

輸出
字串

2
5
2

35
'''
# string = "1234567"

# s = ""
# a ="1"
# b ="2"
# s = a + b   #"12"


# s = "1-1-1--"
# print(s.split("-"))
'''
被分割的字串.split(分割的基準)


字串 =split()=> 串列

如過 轉換串列裡的資料型態
map(型態 , 串列 )   
int()   轉整數
str()   轉文字
list() : 串換成串列
'''
# a = list(map(int,input().split()))
# t = 0
# a = list(map(int,a))
# # for i in range(len(a)):
# #     t += int(a[i]) 

# print(a)


'''
6 3 1 6 16 3

6 > 3
3 > 1
1 < 6
6 < 16
16 > 3
'''
# a = input().split(' ')
# for i in range(len(a)-1):
#     if a[i] > a[i+1]:
#         print(a[i],'>',a[i+1])
#     else:
#         print(a[i],'<',a[i+1])

# a = input().split(' ')
# a = list(map(int,a))
# for i in range(1,len(a)):
#     if a[i] > a[i-1]:
#         print(a[i],'>',a[i-1])
#     else:
#         print(a[i],'<',a[i-1])

'''
串列 => 字串
"文字".join(串列)

分割字串 => 串列 split()
合併串列 => 字串 join()
'''
# a = ["34","ab","cc"]
# a = "+".join(a)
# print(a)


'''
c sa fggfd a
=

c=sa=fggfd=a
'''
a = input().split(' ')
add = input()
ans = ''
for i in range(len(a)-1):
    ans += a[i]
    ans += add
ans += a[-1]
print(ans)