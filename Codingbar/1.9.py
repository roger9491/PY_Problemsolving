'''
前綴和

求出最小連續子數組之和


7 3
    1   2   6   1   1   7   1

0   1   3   9   10  11  18  19

0   1   2
1   2   3
2   3   4
3   4   5
4   5   6
0       2   => summ[3] - summ[0]
1       3   => summ[4] - summ[1]
2       4   => summ[5] - summ[2]
3       5   => summ[6] - summ[3]


'''
# n,m = map(int,input().split())

# k = list(map(int,input().split()))

# pre = []
# pre.append(0)
# c = 0
# for i in range(n):
#     c += k[i]
#     pre.append(c)

# minv = 10**9
# ans = 0
# for i in range(n-m+1):
#     # print(i,i+m)
#     temp = pre[i+m] - pre[i]
#     if temp < minv:
#         minv = temp
#         ans = i
# print(ans+1)

'''
前綴和簡單應用

點石成金




(1)球 1
(2) 前綴合 沒有1 
'''
# a=input().split() #2 1 3 0 2 8 5
# a=list(map(int,a))
# b=input().split() #1 0 1 1 0 1 0
# b=list(map(int,b))
# c=int(input()) #強制成功範圍

# #前綴和
# pre = [0]
# count = 0
# ans = 0
# for i in range(len(a)):
#     if b[i] == 0:
#         count += a[i]
#     else:
#         ans += a[i]
#     pre.append(count)

# maxv = -10**9
# for i in range(len(a)-c+1):
#     temp = pre[i+c] - pre[i]
#     if temp > maxv:
#         maxv = temp
# print(ans+maxv)


'''
前綴和簡單應用

(用前綴合去做)
輸入 一串數列 
輸入 index
輸入 target (保證不會大於數列總和)

當前index的數字 + 之後的數字 總和滿足大於等於 target ， 輸出該索引值


輸出
索引值



ex 1
2 1 5 4 3 5 3
0
8 

2
ex2
2 1 5 4 3 5 3
4
9

6
ex2 
2 1 5 4 3 5 3
5
20

3
'''
# a = list(map(int,input().split()))
# index = int(input())
# target = int(input())

# pre = [0]
# sum = 0
# for i in a:
#     sum += i
#     pre.append(sum)

# target += pre[index]
# if target > pre[-1]:
#     target -= pre[-1]
#     index = 0

# for i in range(index,len(pre)):
#     if pre[i] >= target:
#         print(i-1)
#         break




'''
前綴和 進階練習
支點切割
https://zerojudge.tw/ShowProblem?problemid=f638
'''



'''
https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
给定一个已按照 非递减顺序排列  的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

numbers = [2,7,11,15], target = 9
[1,2]

输入：numbers = [2,3,4], target = 6
输出：[1,3]


输入：numbers = [-1,0], target = -1
输出：[1,2]
'''


'''
https://leetcode-cn.com/problems/merge-sorted-array/

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。



'''



'''
搜查路徑平均


target位置為 0 且mid值平均為 10
'''

# target = int(input())
# num = list(map(int,input().split()))

# i = 0
# j = len(num) - 1
# average = 0
# c = 0
# while i <= j:
#     # print(i,j)
#     mid = (i + j) // 2
#     average += num[mid]
#     c += 1
#     if num[mid] == target:
#         print("target位置為",mid,"且mid值平均為",average//c)
#         break
#     elif num[mid] > target:
#         j = mid - 1
#     else:
#         i = mid + 1
# else:
#     print("找不到target且mid值平均為",average//c)





'''
二分搜尋

輸入一個數字n 
輸入 數列
不會輸入 大於 數列最大值
找出最靠近大於n的索引值(利用二分搜尋)


'''
# import random

# num = []
# c = random.randint(5,16)
# while len(num) < c:
#     n = random.randint(1,50)
#     if n not in num:
#         num.append(n)
# # print(num)
# target = random.randint(1,50)

# print(target)
# num.sort()

# print(num)
# i = 0
# j = len(num) - 1

# while i < j:
#     print(i,j)
#     mid = (i+j) // 2
#     if num[mid] > target:
#         j = mid
#     elif num[mid] == target:
#         i = mid + 1
#         break
#     else:
#         i = mid + 1

# print(i)





'''
二分搜尋 進階練習

圓環出口
https://zerojudge.tw/ShowProblem?problemid=f581

7 3
2 1 5 4 3 5 3
8 2 1 5 
9 4 3 5
12 3 2 1 5 4

4

4 3
1 3 5 7
4 1 3
1 4 8 12
4 1

'''
# n,m = map(int,input().split())
# p = list(map(int,input().split()))
# t = list(map(int,input().split()))

# sum_pre = [0]
# c = 0
# for i in range(n):
#     c += p[i]
#     sum_pre.append(c)

# # print(sum_pre)
# now = 1
# for x in t:
#     target = x + sum_pre[now-1]

#     if target > sum_pre[-1]:
#         target -= sum_pre[-1]
#         now = 1
#     i = now
#     j = n
#     while i < j:
#         mid = (i+j) // 2
#         if sum_pre[mid] == target:
#             now = mid + 1
#             break
#         elif sum_pre[mid] > target:
#             j = mid 
#         else:
#             i = mid + 1
#     else:
#         now = j + 1
#     now = ((now-1)%n+1)
# print(now-1)

'''
0 ~ 200
193
100  ~ 200大
100 ~　195       小

二分搜尋法 猜的數字 固定 當前範圍 一半
0 ~ 200
100  ~ 200
150 ~ 200
175 ~ 200
187 ~ 200   387 // 2 => 193
193 ~ 200
193 ~ 196
193 ~ 194
   193
0   2
1 2 3
i = 1
j = 2
i = 1 + 1
i == j


3
'''
# target = int(input())
# a = [1,2,3,4,5,6,7,8,9,10,11]
# i = 0
# j = len(a) - 1










# while i <= j:
#     mid = (i + j) // 2
    
#     if a[mid] > target:
#         j = mid - 1
#     elif a[mid] < target:
#         i = mid + 1
#     else:   #a[mid] == target
#         print(mid)
#         break
# else:
#     print("找不到")


'''
1 ~ 100     1 ~ 100 
<50  小     50
1 ~ 50      1 ~ 49
>25  大     25
25 ~ 50     25 ~ 50
<37  小     37
25 ~ 37     25 ~ 37
>31  大     31
31 ~ 37     31 ~ 37
<34         34
31 ~ 34     31 ~ 34
>32         32
32 ~ 34     32 ~ 34
33 == 33    33
break

'''
# target = int(input())
# a = [1,2,3,4,5,6,7,8,9,10,11]
# i = 0
# j = len(a) - 1

# while i <= j:
#     mid = (i + j) // 2

#     if a[mid] > target:
#         j = mid - 1
#     elif a[mid] < target:
#         i = mid + 1
#     else:
#         print(mid)
#         break
import random

num = []
c = random.randint(5,16)
while len(num) < c:
    n = random.randint(1,50)
    if n not in num:
        num.append(n)

target = random.randint(1,50)


n= target
l= num
print(target)

l1=sorted(l)
print(l1)
i=0
j=len(l)-1
flag=1
while i<=j:
    mid=(i+j)//2
    if n>l1[mid]:
        i=mid+1
    elif n<l1[mid]:
        j=mid-1
    else:
        print(mid+1)
        flag-=1
        break

if flag:
    print(mid)

