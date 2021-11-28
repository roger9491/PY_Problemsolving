'''

如何 讓 數列有小到大
i
[5,3,3,7,4,2]
index = 0
temp = 5

大於
[3,5,3,7,4,2]
i = 1
index = 0
temp = 5
index = 1

大於
[3,3,5,7,4,2]
i = 2
index = 1
temp = 5
index = 2

小於
[3,3,5,7,4,2]
i = 3
index = 3
temp = 7

大於
[3,3,5,4,7,2]
i = 4
index = 3
temp = 7
index = 4


大於
[3,3,5,4,2,7]
i = 5
index = 4
temp = 7
index = 5

a.sort()

quick sort() : 遞迴 分治 算法思想
merge sort()
'''

a = [3,3,5,4,2,7]   #n筆資料 O(n**2) 時間複雜度 泡沫排序 bubble sort  a.sort() O(nlogn)
for i in range(len(a) - 1)  #     0 1   2   3   4   .... n
    for j in range(1,len(a) - i):#n n-1 n-2 n-3         1 = n+n-1+n-2+...1 =>等差級數(a + b) * n / 2 => n**2 + n // 2
        if a[j-1] > a[j]:
            temp = a[j-1]
            a[j-1] = a[j]
            a[j] = temp
print(a)