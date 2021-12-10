# ans = ""
# for i in range(10):
#     ans = str(i) + ans 
# print(ans)

'''
輸入 一行 n 個數字
印出 數字之間的關係


ex
23 12 5 2 9 10 10

23 > 12
12 > 5
5 > 2
2 < 9
9 < 10
10 == 10


n = list(map(int,串列)) 轉 串列裡的所有值的型態

'''
# n = input()
# n = n.split(" ")
# n = list(map(int,n))
# for i in range(len(n)-1):
#     if n[i]>n[i+1]:
#         print(n[i],">",n[i+1])
#     elif n[i+1]>n[i]:
#         print(n[i],"<",n[i+1])
#     else:
#         print(n[i],"=",n[i+1])
'''
串列.split(字串) = > 串列
字串.join(串列) => 字串


'''
a = ["1","2"]
print("x".join(a))

'''
輸入 一行數字 空格分開 join(a)不能用
輸入 一個字串


輸出 合併完的字串


ex 
1 45 23 7
xx

1xx45xx23xx7
'''
# a=input()
# a=a.split()
# b=input()
# c=str()
# for i in range(len(a)):
#     if i !=len(a)-1:
#         a[i]=a[i]+b
    
# for i in a:
#     c=c+i

# print(c)
'''
if 字串 in 字串:
    a       b
輸入 
字串 a  (1)長度是固定 (2)他是連續的
字串 b 

印出True/False

ab
s = "adabc"
s[2] ~ s[3]

True

'''
# a = input()
# b = input()
# c = []
# d = []
# for i in range(len(b)):
#     if b[i] == a[0]:
#         if b[i:i+len(a)] == a:
#             print(True)
#             break
# else:
#     print(False)

'''
s = "1234567"
實作 s[首相:末向:間隔]




實作串列切片
a = [1,2,3,4,5,6]
輸入 
首相
末向
間隔

輸出 切片串列
ex
2
5
2

[3,5]
'''
a = [1,2,3,4,5,6]
b=int(input())
c=int(input())
d=int(input())
e=0
f=[]
if (c-b)%d==0:
    e=(c-b)//d
else:
    e=(c-b)//d+1
for i in range(e):
    f.append(a[b])
    b=b+d
print(f)
