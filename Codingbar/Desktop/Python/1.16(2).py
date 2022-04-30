'''
B. WeirdSort
泡沫排序思維實戰
https://codeforces.com/problemset/problem/1311/B

題目翻譯
https://www.luogu.com.cn/problem/CF1311B


[[1,2,3,4]]

1 3 5 7 9


13256
13311

12 321 12 213 


6
3 2     n , m
3 2 1   a   a[1] a[2] 2 3 1     a[1] a[2] 1 2 3
1 2     p   a[2] a[3] 2 1 3  
4 2
4 1 2 3     2 3     3 4
3 2
5 1
1 2 3 4 5
1
4 2
2 1 4 3
1 3
4 2
4 3 2 1
1 3
5 2
2 1 2 3 3
1 4


YES
NO
YES
YES
NO
YES
'''
# n = int(input())
# for m in range(n):
#     b = list(map(int,input().split()))
#     a = list(map(int,input().split()))
#     p = list(map(int,input().split()))
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])
#     a.sort()

#     for j in range(len(p)):
#         for i in range(len(p)):
#             if c[p[i]-1]>c[p[i]]:
#                 temp = c[p[i]-1]
#                 c[p[i]-1]=c[p[i]]
#                 c[p[i]]=temp
#     # print(c)
#     # print(a)
#     if c!=a:
#         print("NO")
#     elif c==a:
#         print("YES")

a = [2,3,4,5]
a = a.sort()
print(a)



'''
檢查有沒有走過

append(索引直的方式)
缺點: 事後再查詢這個索引直的時候，
    所需的時間複雜度 會根據你走路的數量決定 O(n)


O(1)
建立一個新的 複製版的串立
設定 初始值為 0

在電腦的世界裡，只要知道地址 時間複雜度 O(1)


'''

'''
None : 空
a = [2,3,4,5]
a = a.sort()
print(a)



串列.index(data)

大到小
a = [2,6,7,3,1]
a.sort(reverse = True)
b = sorted(a,reverse =  True)
print(b)

#數對排序
a = [[1,2],[1,4],[1,4,5],[1,4,4]]
a.sort()
print(a)


a = ['a','r','s','h']
a.sort()
print(a)

每一個文字，會用一個數字來代表他，ascii


如何獲得 字元 的 ascii
ord()
a = ['a','r','s','h']
a.sort()
for i in a:
    print(ord(i))

#判斷英文字母的方法
a = ord("a")
b = ord("z")

c = ord("A")
d = ord("Z")

string = input()
for i in string:
    if a <= ord(i) <= b or c <= ord(i) <= d:
        pass
    else:
        print(False)
        break
else:
    print(True)


盡量用內建的函式，


logn:
n = 4
logn = 2
n = 8 
logn = 3

logn < n
n*logn  < n*n


'''

a = list(map(int,input().split()))
b = []
e = []
ii =0
jj =0
g = False
f = 0
count = 10**9
dire = [[-1,0],[1,0],[0,-1],[0,1]]
for i in range(a[0]):
    c = list(map(int,input().split()))
    b.append(c)
d = [[0]*a[1] for i in range(a[0])]
for i in range(a[0]):
    for j in range(a[1]):
        if b[i][j]<count:
            count = b[i][j]
            x = i
            y = j
d[x][y]=1
while True:
    count = 10**9
    for k in range(len(dire)):
        now_i=x+dire[k][0]
        now_j=y+dire[k][1]
        if 0<=now_i<a[0] and 0<=now_j<a[1]:
            if b[now_i][now_j]<count and d[now_i][now_j]!=1:
                g = True
                count = b[now_i][now_j]
                ii = now_i
                jj = now_j

    if g==False:
        break 

    x = ii
    y = jj   
    d[x][y]=1
    g = False
for i in range(a[0]):
    for j in range(a[1]):
        if d[i][j]==1:
            f+=b[i][j]
print(f)


