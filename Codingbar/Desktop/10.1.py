'''
L2-1-符號不動冥王01

'''


'''
第一單元 
符號不動冥王
'''
# letter = "abcdefghijklmnopqrstuvwxyz"


# string = list(input())
# i = 0
# j = len(string) - 1
# while i < j:
#     if string[i] in letter and string[j] in letter:
#         string[i],string[j] = string[j],string[i]
#         i += 1
#         j -= 1
#     else:
#         if string[i] not in letter:
#             i += 1
#         if string[j] not in letter:
#             j -= 1

# print("".join(string))


'''

最大消波塊


'''

# a = list(map(int,input().split()))

# i = 0
# j = len(a) - 1
# ans = 0
# while i < j:

#     if ans < (j - i) * min(a[i],a[j]):
#         ans = (j - i) * min(a[i],a[j])
    
#     if a[i] > a[j]:
#         j -= 1
#     elif a[i] < a[j]:
#         i += 1
#     else:
#         i += 1
#         j -= 1
# print(ans)
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

 非递减數列
O(n)
'''

# numbers = [2,7,11,15]
# target = 9



'''
https://leetcode-cn.com/problems/merge-sorted-array/

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

nums1 = [1,3,5]
nums2 = [2,4]

O(n+m)
'''
# nums1 = [4, 5, 6, 10, 11, 13] 

# m = 3
# nums2 = [5, 9, 11, 13, 17, 19]
# n = 3
# left1=0
# left2=0
# #right1=len(num1)-1
# #right2=len(num2)-1
# new=[]
# while len(new)<len(nums1)+len(nums2):
#     print(left1,left2)
#     if nums1[left1]<=nums2[left2]:
#         if  left1 == len(nums1) - 1:
#             new.append(nums1[left1])
#             #加入後半部
#             new=new+nums2[left2:]
#             break   
#         new.append(nums1[left1])
#         left1+=1

#     else:
#         if  left2 == len(nums2) - 1:
#             new.append(nums2[left2])
#             #加入後半部
#             new=new+nums1[left1:]
#             break   
#         new.append(nums2[left2])
#         left2+=1

#     print(new)
# print(new)
    



'''
合併兩個 已排序數組
'''

'''
https://leetcode.cn/problems/shortest-distance-to-a-character/submissions/

 字符的最短距离

 https://leetcode.com/problems/shortest-distance-to-a-character/
'''

'''
Black and White Stripe
https://codeforces.com/problemset/problem/1690/D
'''
# t = int(input())
# for i in range(t):
#     n, m = map(int,input().split())
#     s = input()
#     #   0123
#     # bbwbw
#     w = 0
#     ans = 10**9
#     for i in range(n):
#         if i < m :
#             if s[i] == "W":
#                 w += 1
#         else:
#             ans = min(ans, w)
#             if s[i] == "W":
#                 w += 1
#             if s[i - m] == "W":
#                 w -= 1
#     ans = min(ans, w)
#     print(ans)

'''

點石成金

'''

# a = list(map(int,input().split()))

# b = list(map(int,input().split()))

# n = int(input())

# total = 0

# for i in range(len(a)): #n
#     if b[i]:
#         total += a[i]
# # print(total)
# maxv = 0
# for i in range(len(a)-n+1): #n /2
#     temp = 0
#     for j in range(i,i+n):  #n/2
#         if b[j] == 0:
#             temp += a[j]
#     maxv = max(maxv,temp)
# print(total + maxv)





'''
前綴和

求出最小連續子數組之和


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

輸入 數列
輸入一個數字n 
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
right = [6,2,1,5]
forward = [4,1,3,6]

向前 - 1
right[0] = forward[0]
right[2] = forward[2]
temp = forward[0]
forward[0] = forward[1]
forward[1] = forward[2]
forward[2] = forward[3]
forward[3] = temp
right = [4,2,3,5]
forward = [1,3,6,4]


'''
# a = list(map(int,input().split()))
# b = []
# right = [6,2,1,5]
# forward = [4,1,3,6]
# for i in range(a[0]):
#     b.append(1)
# for i in range(a[1]):
#     c = list(map(int,input().split()))
#     if c[1]==-1:
#         for j in range(len(forward)):
#             if b[c[0]-1]==forward[j]:
#                 if j==3:
#                     b[c[0]-1]=forward[0]
#                 else:
#                     b[c[0]-1]=forward[j+1]
#                 break
#             elif b[c[0]-1]==5 or b[c[0]-1]==2:
#                 b[c[0]-1]=3
#                 break
#     elif c[1]==-2:
#         for j in range(len(right)):
#             if b[c[0]-1]==right[j]:
#                 if j==3:
#                     b[c[0]-1]=right[0]
#                 else:
#                     b[c[0]-1]=right[j+1]
#                 break
#             elif b[c[0]-1]==3 or b[c[0]-1]==4:
#                 b[c[0]-1]=5
#                 break
#     elif c[0]>0 and c[1]>0:
#         temp = b[c[0]-1]
#         b[c[0]-1]=b[c[1]-1]
#         b[c[1]-1]=temp
# b = list(map(str,b))
# print(" ".join(b))

'''
135
13256
35001
1001


list():只能對可迭代的物件進行使用

'''
# while True:
#     # try:
#         n=int(input())
#         a = n
#         n = str(n)
#         n = list(n)
#         temp = []
#         temp = n.copy()
#         flag = False
#         for i in range(len(n)):
#             if int(n[i])%2==0:
#                 flag = True
#         if flag == False:
#             print(0)
#         elif flag == True:
#             flag = False
#             for i in range(len(n)):
#                 if flag == False:
#                     if int(n[i])%2==0:
#                         n[i]=int(n[i])+1
#                         flag = True
#                 elif flag == True:
#                     n[i]=1
#             flag = False
#             print(temp)
#             for i in range(len(temp)):
#                 if flag == False:
#                     if int(temp[i])%2==0:
#                         if temp[i]==0:
#                             temp[i]=9
#                         else:
#                             temp[i]=int(temp[i])-1
#                         flag = True
#                 elif flag == True:
#                     temp[i]=9

#                 print(i,temp)


#             n = list(map(str,n))
#             temp = list(map(str,temp))
#             n = "".join(n)
#             temp = "".join(temp)
#             if (int(n)-a)>(a-int(temp)):
#                 print(a-int(temp))
#             else:
#                 print(int(n)-a)


'''
等 dict
美麗的彩帶
https://zerojudge.tw/ShowProblem?problemid=e289

'''