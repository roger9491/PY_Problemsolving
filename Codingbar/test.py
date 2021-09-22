
a=input().split() #2 1 3 0 2 8 5
a=list(map(int,a))
b=input().split() #1 0 1 1 0 1 0
b=list(map(int,b))
c=int(input()) #強制成功範圍



for i in range(10):
    print(i)
while Ture:
    print(i)

while True:
    print(i)


print(i)
#前綴和
pre = [0]
c = 0
ans = 0
for i in range(len(a)):
    if b[i] == 0:
        c += a[i]
    else:
        ans += a[i]
    pre.append(c)
# 0 1 2 3 4 5  6-3 = 3 + 1
# 3 4 5
for i in range(len(a)-c+1):
    print(i)





'''
前綴和 => 最適合查看一個區間的數 預處裡
n 個數
n1 n2 n3 n4 .... nn     ni
前 i 個的總和

1 2 3 4   5  6   7 8
1 3 6 10 15 21 28 36 => sum[]
36 - 21 = 15 == 7+8

sum[8] == 36 ==> sum[7] + 8 ==> sum[6] + 7 + 8
sum[6] == 21
sum[8] - sum[6] ==> sum[6] + 7 + 8 - sum[6] == 7 + 8 ==15
O(1) sum[8] - sum[6] 
    sum[8] - sum[5] = 21

10 5
1 2 3 1 2 2 3 1 4 5
1

'''