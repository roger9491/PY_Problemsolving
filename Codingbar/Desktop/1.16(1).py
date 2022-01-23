'''
抽獎活動

33
Shan Dell Cart Mira
15 62 8 33




i = 0
j = len(list) - 1
目標
1 3 5 7 8 9 10
0     3     6   
'''


# prize=int(input())
# peo=input().split()
# l=list(map(int,input().split()))

# l1=sorted(l)

# x=0
# y=len(l1)-1
# count=0
# while 1:
#     count+=1
#     avg=(x+y)//2
#     if l1[avg]==prize:
#         print("得獎者為"+peo[l.index(prize)]+"(找",count,"次)")
#         break
#     elif l1[avg]>prize:
#         y=avg-1
#     elif l1[avg]<prize:
#         x=avg+1
#     if x>y:
#         print("無人得獎(找",count,"次)")
#         break








# target = int(input())

# name = input().split()

# num = list(map(int,input().split()))

# num2 = sorted(num)
# i = 0
# j = len(num) - 1
# c = 0
# while i <= j:
#     c += 1
#     mid = (i + j) // 2

#     if num2[mid] > target:
#         j = mid - 1
#     elif num2[mid] < target:
#         i = mid + 1 
#     else:
#         break 
# print(mid)
# if num2[mid] != target:
#     print("無人得獎(找",c,"次)")
# else:
#     print("得獎者為",name[num.index(target)],"(找",c,"次)")


'''
實作 add() 集合加入

'''

# from random import random


# a = set()       #建立集合
# a.add(1)
# a.add(1)
# a.add(2)
# print(a)
# a.remove(1)
# print(a)
# import random
# list1 = []
# for i in range(10):
# 	list1.append(random.randint(10,100))
# list1 = set(list1)

# print(len(list1))
# list1 = list(list1)
# print(list1)



'''
實作 & 交集

'''

# a = {1,2,3,4}
# b = {3,4,2}
# c = a & b
# c1 = a | b
# c2 = a - b
# print(c2)





'''
實作 聯集

'''


'''
實作 差集




'''

'''
dict 字典

dict: key:value

	建立: dict = {}
	新增資料: dic["d"] = 1234
	刪除資料: del dic["d"]
	取值: 跟串列一模一樣, key == index 
	判斷  if key in dict:	O(1)


串列模擬dict

ex 
0 1
a 13
b 53
c 65
b
c
a

output
53
65
13

'''
# dic = {'a':23423,'b':5,'c':21313}
# dic = {'a':23423,'b':5,'c':21313}	#字典
# a = "a"
# dic[a] = 1234 O(1)
# print(dic)


# a=[]
# b=[]

# for i in range(3):
#     x,y=input().split()
#     a.append(x)
#     b.append(y)

# for i in range(3):
#     n=input()
#     print(b[a.index(n)])	#O(n)
'''
實作 dict

原理: 在電腦的世界中，只要知道地址 我們就能最快的速度找到他，也就是 array ，只要知道
        索引值 就可以在 O(1) 時間 獲取值。

索引值 就是數字，所以只要把 key 值 透過某種方式 轉成數字，就行了!


key 值 -> 雜湊函式 -> address	O(1)
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
# m = hashlib.md5()	#實利化
# data = "ADASD"

# # 先將資料編碼，再更新 MD5 雜湊值
# m.update(data.encode("utf-8"))

# h = m.hexdigest()
# print(h)

# import hashlib


# def get_hashval(data):
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

#加入
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

#查詢
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

'''


'''
兩個數組的交集 (1)
https://leetcode-cn.com/problems/intersection-of-two-arrays/

'''


'''
兩個數組的交集 (2)
https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/submissions/

'''


# while True:
# 	try:

# 		n = int(input())
# 	except:
# 		break
# print(1)

while True:


	n = int(input())

print(1)

