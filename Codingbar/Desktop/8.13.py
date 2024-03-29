'''
大
小

(1)
小大 1K 小大小大 4
大小
小大|大小
大小|小大
(2) K
小*K大*K
大*K小*K
1 
aBBdaaa
aAAaaaa
小大 aA aAa aAaA aAaAa aAaAaA
大小 Aa AaA AaAa AaAaA AaAaAaAa
範例二：
3 
DDaasAAbbCC

範例三：
2 
aafAXbbCDCCC

範例四：
3 
DDaaAAbbCC
'''



'''
平方累加


輸入n 

4

階段性問題 (每一個階段的算法是一樣)
ex n == 1 階段性1問題
ex n == 2 階段性2問題
ex n == 3 階段性3問題
ex n == 4 階段性4問題
階段性2問題 = 1**2 + 2**2
階段性3問題 = 1**2 + 2**2 + 3**2
階段性4問題 = 1**2 + 2**2 + 3**2 + 4**2
階段性5問題 = 1**2 + 2**2 + 3**2 + 4**2 + 5**2
階段性問題:
    都是 由小到大 平方相加
    前面階段的總和 + 當前階段數字平方
    f(n-1)        + n**2

遞迴關係式
f(n) = f(n-1) + n**2

邊界
f(1) = 1
'''

# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return f(n-1) + n**2
# n = int(input())
# print(f(n))

'''
1 2 3 4 5 6 7 8 9

'''

# 當data裡面的值都是負，這段程式碼就無法找到最大值
# ma = 0
# data = [9,4,8,6]
# for i in data:
#     if i > ma:
#         ma = i
# print(ma)


# a = float("inf")    #最大值
# if a > 10**12:
#     print(1)
# else:
#     print(2)


'''
從輸入格式就可以判斷出，題目的數字範圍
最小值、最大值就可以設定成超出這個範圍的數字


常用
max(): 最大值
min(): 最小值
abs(): 絕對值

排序
a = []
a = sorted(a)
a = sorted(a,reverse=Ture)
a.sort(reverse = True)

n**2 + n
O(n**2)
O(nlogn)
n**2
nlogn

n = 10**5
n**2 = 10**10
'''



'''
遙近的距離

2
1 10 2 5 9 20 -4 11
1 2 3 4 5 6 7


-4 1 2 5 9 10 11 20
'''

'''
(1) 排序
時間複雜度O(nlogn)
'''
n = int(input())
for i in range(n):
    a = list(map(int,input().split()))  #1

    a.sort()    #排序 小~大     nlogn
    minv = 10**9            #   1
    for j in range(len(a)): #   n
        if minv > abs(a[j+1]-a[j]):
            minv = abs(a[j+1]-a[j])
    print(minv) #1
    #時間複雜度 1 + 1 + n + nlog => O(nlogn)

'''
log => 以2為底
白話文 log10 => 10 能被 2 除幾次
log10**3 = 10 => 10**3 能被 2 除幾次
              => 1000 能被 2 除幾次
        約等於 10

2**5 => 32
32*32 => 1024
2**5 * 2**5  = 1024 => 2**10 = 1024         
'''
'''
(2)暴力法

'''
n = int(input())
for i in range(n):
    a = list(map(int,input().split()))  #1

    minv = abs(a[0] - a[1])
    for i in range(len(a)): #要比較的基準
        for j in range(i+1,len(a)):
            if minv > abs(a[i]-a[j]):
                minv = abs(a[i]-a[j])
    print(minv)

