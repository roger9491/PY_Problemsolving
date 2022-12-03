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
set() : 集合 不會有重複資料

建立 
s = set()

加入
s.add()

刪除
s.remove()

交集
a = set()
b = set()
c = a & b

聯集
a = set()
b = set()
c = a | b

'''
l = [1,2,3]
r = [2,3,4]

l = set(l)
r = set(r)

c = l & r
print(c)

'''

字典


dic = {鍵值:值}

如何取值?
    跟串列幾乎一樣
    鍵值取值
    <鍵值必須唯一>
    時間複雜度 O(1)
    為什麼?
    
新增資料
    ex  "黨靖騰":175
    dic["黨靖騰"] = 175     (鍵值不存在)

修該資料
    dic["黨靖騰"] = 180     (鍵值存在)

刪除    (特別注意確保要刪除的鍵值存在)
    del dic["鍵值"]

如何判斷鍵值有沒有存在?
    鍵值 in dic     布林值  #O(1)

    資料 in 串列    #O(n)

如何迭代字典?
    for i in dic:

字典長度
len(dic)    
'''
# dict = {}

# dict["老師"] = 175
# dict["礽臤"] = 171

# if "老師" in dict:
#     print("存在")
# print(dict)

# 如果key不存在
# a = input()
# if a in dict:
#     print(dict[a])
# else:
#     print("key不存在")


# for key in dict:
#     print(key, dict[key])

#   0  1 2 3 4


# a = [1,2,3,4,5]
# for i in a:
#     print(i)


# for i in range(len(a)):
#     print(i)

# dic = {"2":1, "3":2, "4":5}

#       1          2         0
# a = [["2", 1], ["3",2 ], ["4", 5]]


# lst = [5 , 1, 2]
# print(lst[1])   #O(1)
'''
實作 dict

原理: 在電腦的世界中，只要知道地址 我們就能最快的速度找到他，也就是 array ，只要知道
        索引值 就可以在 O(1) 時間 獲取值。

索引值 就是數字，所以只要把 key 值 透過某種方式 轉成數字，就行了!


key 值 -> 雜湊函式 -> address	O(1)

a = [1,2,3,4,5,7]
a[4]    O(1)

雜湊函式

https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8


import hashlib
m = hashlib.md5()
data = "G. T. Wang"

# 先將資料編碼，再更新 MD5 雜湊值
m.update(data.encode("utf-8"))

h = m.hexdigest()
print(h)

'''
# import hashlib
# m = hashlib.md5()	#實利化 物件導向
# data = "ADA"

# # 先將資料編碼，再更新 MD5 雜湊值
# m.update(data.encode("utf-8"))

# h = m.hexdigest()
# print(h)

# import hashlib

# def get_hashval(data):  #產生鍵值所對應的索引值
#     m = hashlib.md5()
#     # 先將資料編碼，再更新 MD5 雜湊值
#     m.update(data.encode("utf-8"))

#     h = m.hexdigest()
#     print(h)
#     hash_num = 0
#     for i in h:
#         hash_num += ord(i)
#     return hash_num % 20

# hash_table = [0]*20	# 0 ~ 19

# #加入
# while True:
#     key,value = input().split()
#     if key == "no":
#         break


#     index = get_hashval(key)
#     print(index)
#     if hash_table[index] == 0:
#         hash_table[index] = [key,value] 
#     else:	#	開放地址法
#         while hash_table[index] != 0:
#             index += 1
#             index = index % 20
#         hash_table[index] = [key,value]

# for i in hash_table:
#     print(i)

# # 查詢
# while True:
#     key = input()
#     if key == "no":
#         break
#     index = get_hashval(key)
#     print(index,hash_table)
#     while hash_table[index][0] != key:
#         index += 1
#         index %= 20
#     print(hash_table[index][1]) 


'''
專精第11單元

投票統計



未用dict 時間複雜度
dict    時間複雜度


dict = {鍵值:value}
dict[鍵值] = value


if a in b

for i in dict: 迭代鍵值


n
O(n)
'''
# a = []
# dic = {}
# ans = []
# while True: # n
#     b = input()
#     if b == "no":
#         break
#     else:
#         b = int(b)
#         a.append(b)

# for i in range(len(a)): #n
#     dic[a[i]] = 0   #O(1)

# for i in range(len(a)): #n
#     dic[a[i]]+=1

# for i in dic:   # < n 
#     if dic[i]>len(a)/2: #
#         ans.append(i)

# for i in range(len(ans)):
#     print(ans[i])

# number_list = []
# count_list = []
# while True:
#     number = input()
#     if number=="no":
#         break
#     else:
#         number = int(number)
#         number_list.append(number)

# set_number = set(number_list)

# for i in (set_number) : #(n * n) = > O(n**2)
#     count = number_list.count(i)    #n
#     count_list.append(count)

# for j in range (len(count_list)):
#     if count_list[j] >= int(len(number_list)/2+1):
#         print(list(set_number)[j])
#         break

'''
兩個數組的交集 (1)
https://leetcode-cn.com/problems/intersection-of-two-arrays/

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
'''
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# dic = {}
# ans = {}
# for i in range(len(nums1)):
#     dic[nums1[i]] = 0
# for i in range(len(nums2)):
#     if nums2[i] in dic:
#         ans[nums2[i]] =0
# for i in ans:
#     print(i)

# return list(set(nums1) &　set(nums2))
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# ans = []
# for i in nums1:
#     if i in nums2 and i not in ans:
#         ans.append(i)
# print(ans)
#O(n**2)

# nums1 = [1,2,2,1]
# nums2 = [2,2]
# n1 = {}
# n2 = {}
# ans = []
# for i in nums1:
#     n1[i] = 1
# for i in nums2:
#     n2[i] = 1

# for i in n1:
#     if i in n2:
#         ans.append(i)
# print(ans)





'''
兩個數組的交集 (2)
https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/submissions/

'''
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# n1={}
# n2={}
# ans=[]
# a=0
# for i in nums1:
#     if i not in n1:
#         n1[i]=1
#     else:
#         n1[i]+=1
# for i in nums2:
#     if i not in n2:
#         n2[i]=1
#     else:
#         n2[i]+=1
# # print(n1)
# # print(n2)

# for i in n1:
#     if i in n2:
#         for j in range(min(n2[i],n1[i])):
#             ans.append(i)


# print(ans)
'''
https://www.luogu.com.cn/problem/P1102
P1102 A-B 数对

'''


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
差分

差分 和 前綴和 區別
前綴和: 查詢區間和 O(1)

差分:   區間修改  O(1)
        查詢修改後的串列 O(n)


情境:
輸入一個數列
輸入n
接下來有n行
每一行輸入 c s e
代表 +c s起點 e終點
輸出修改完的數列


ex1
0 1 0 1 0 2 1
3
1 1 3
4 6 6
2 3 5

[0, 2, 1, 4, 2, 4, 5]


原: 0 1 0 1 0 2 1
2 3 5
    0 1 0 3 2 4 1

    0 1 -1 1 -1 2 -1
    0 1 -1 3 -1 2 -3    
    0 1  0 3  2 4  1

結論:
    (1) 先建立差分數列  (下一項-前一項)
        ex.
            原: 0 1 0 1 0 2 1
            差: 1 -1 1 -1 2 -1
        
    (2) c s e   c:+c    s:起點  e:終點
        差: 在s的值+c
            在e+1的值-c
    (3)全部修改完，在還原 累加

O(N*M)
10**4
'''

# a = list(map(int,input().split()))
# n = int(input())
# for i in range(n):
#     s = list(map(int,input().split()))
#     plus = s[0]
#     go = s[1]
#     end = s[2]
#     for j in range(go,end+1):
#         a[j] = a[j] + plus
# print(a)



'''
差分
https://leetcode.cn/problems/car-pooling/submissions/

'''
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         dif = [0]*1001
#         for i in trips:
#             dif[i[1]] += i[0]
#             dif[i[2]] -= i[0]
#         pre = []
#         total = 0
#         for i in dif:
#             total += i
#             pre.append(total)
#         for i in pre:
#             if i > capacity:
#                 return False
#                 break
#         else:
#             return True 
'''
差分進階練習
https://zerojudge.tw/ShowProblem?problemid=g597
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


04. L1-4-4 奇怪的問題

#QUESTION

小明在桌上寫了N個數字，並且問小花好多次問題。

每次問題都是問小花 : 「桌上的數字裡面，小於 x 的最大數字是多少?」



#INPUT

輸入的第一行有兩個正整數 N、Q (1≤N,Q≤105)，代表桌上有幾個數字。

第二行有 N 個整數用空格隔開，代表桌上的這些數字(1≤數字≤1018 ) 。

接下來有 Q 行，每行有一個數字 x ，代表小明問小花的數字x(1≤x≤1018))。



#OUTPUT

依序輸出 Q 行，代表每次詢問的答案。

如果存在小於x的數字就輸出數字，否則請輸出none。


8 2
1 8 7 5 2 3 6 4
1
100

none
8

1 2 7 10 21 30
0 1 2 3  4  5
'''

# n, m = map(int,input().split())
# a = list(map(int,input().split()))
# a.sort()

# for i in range(m):
#     k = int(input())

#     l = 0
#     r = n - 1
#     index = 0
#     while l <= r:
#         mid = (l + r ) // 2
#         if a[mid] == k:
#             index = mid
#             break
#         elif a[mid] > k:
#             r = mid - 1
#         else:
#             l = mid + 1
#     else:
#         index = r

#     if a[index] >= k:
#         index -= 1

#     if 0 <= index < n:
#         print(a[index])
#     else:
#         print("none")





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
等 dict
美麗的彩帶
https://zerojudge.tw/ShowProblem?problemid=e289

'''