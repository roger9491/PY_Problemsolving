'''
差分作業

https://leetcode.cn/problems/car-pooling/submissions/

'''
# All = list(map(int,input().split()))
# All_cool = [All[0]]
# for i in range(len(All) - 1):
#     All_cool.append(All[i+1]-All[i])


# n = int(input())
# for i in range(n):
#     a = list(map(int,input().split()))
#     c = a[0]
#     s = a[1]
#     e = a[2]
#     All_cool[s] = All_cool[s] + c
#     All_cool[e+1] = All_cool[e+1] - c
# All_after = []
# f = 0
# for i in range(len(All_cool)):
#     f = f + All_cool[i]
#     All_after.append(f)
# print(All_after)


'''
如何求 字元的ascii
ord()
'''
# if ord('A') <= c <= ord('Z'):
#     print("大寫")
# k = int(input())
# All = input()
# All_num = []
# for i in range(len(All)):
#     if All[i] in "QWERTYUIOPASDFGHJKLZXCVBNM":
#         All_num.append(1)
#     else:
#         All_num.append(0)




# a = 0
# good_All = []
# small_All = []
# for i in range(a,len(All)): #0 ~ lne(all)
#     count = k
#     print(a)
#     for j in range(i,len(All)-1):
#         if count == 0 and All_num[j] != All_num[j+1]:
#             count = k
#             small_All.append(All[j+1])
#             a = a + 1
#         elif 0<count<=k and All_num[j] == All_num[j+1]:
#             count = count - 1
#             small_All.append(All[j+1])
#             a = a + 1
#         elif count == 0 and All_num[j] == All_num[j+1]:
#             a = a + 1
#             good_All.append(small_All)
#             small_All = []
#             break
#         elif 0<count<=k and All_num[j] != All_num[j+1]:
#             a = a + 1
#             good_All.append(small_All)
#             small_All = []
#             break
# print(good_All)

'''
0   1   0   1   0   2   1
                        5

0   1   -1  1   -1  2   -1  
                        3
0   1   0   1   0   2   5   


4 6 6
'''


'''
set() : 集合 不會有重複資料

建立 
s = set()

加入
s.add()

刪除
s.remove()

迭代集合
for i in set():

交集
a = set()
b = set()
c = a & b

聯集
a = set()
b = set()
c = a | b


作業: 決鬥吧遊戲Boy
'''

# l = {1,2,2,3}
# l = set()

# l.add(1)
# l.remove(1)

# a = [1,2,2,3]
# a = set(a)
# a = list(a)
# print(a)

# print(l)
# l = [1,"2","1","1",2,3]

# l2 = [1,2,3]
# l3 = l & l2

# print(l3)

# s = {}
# print(type(s))




'''

字典


dic = {鍵值:值}

如何取值?
    跟串列幾乎一樣
    鍵值取值
    <鍵值必須唯一>
    時間複雜度 O(1)
    為什麼?

取值
    dic["黨靖騰"]   O(1)

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
    for i in dic:   #迭代出來的是鍵值
'''


# a = input()

# dic[a] = 1

# dic[a] += 1
# dic = {"林政叡":190}
# # dic["林政叡"] = 200
# dic["黨靖騰"] = 175
# if "林政叡" in dic:
#     print("存在")

# for i in dic:
#     print(i)

# print(dic)



# dic = {"謝詠宸":153, "莊心睿":175 ,"李博凱":180,"謝詠宸":165 }
# dic["黨靖騰"] = 175
# dic["黨靖騰"] = 180
# # print(dic)
# # if "黨" in dic:
# #     del dic["黨"]
# # else:
# #     print("鍵值不存在")
# for i in dic:
#     print(dic[i])
# print(dic)
# key = []
# value = []


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

# num = []
# while True:
#     a = input()
#     if a == "no":
#         break
#     num.append(a)

# # num: 長度為n  
# for i in num:   #O(n)
#     if num.count(i)  > len(num)/2:
#         print(i)
#         break

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

# nums1 = [1,2,2,1]
# nums2 = [2,2]
# dic = {}
# for i in nums1:
#     dic[i] = 1

# ans = []
# for i in nums2:
#     if i in dic:
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


# '''
# X=list(map(int,input().split()))
# N=X[0]
# C=X[1]
# inf=list(map(int,input().split()))
# dic1={}
# times=0
# for i in inf:
#     if i in dic1:
#         dic1[i]+=1
#     else:
#         dic1[i]=1
# print(dic1)
# for i in dic1:
#     if dic1[i]+C in dic1:
#         times+=dic1[dic1[i]+C]*dic1[i]
#         print(dic1[dic1[i]+C]*dic1[i])
#     else:
#         continue
# print(times)
# n, c = map(int,input().split())

# a = list(map(int,input().split()))

# dic = {}

# for i in a:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# # print(dic)
# ans = 0
# # print(dic)
# for i in dic:
#     if i + c in dic:
#         ans += dic[i]*dic[i+c]
#     # if i - c in dic:
#     #     ans += max(dic[i],dic[i-c])

#     # print(ans)
# print(ans)


