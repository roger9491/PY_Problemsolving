'''
抽獎活動

33
Shan Dell Cart Mira
15 62 8 33
'''

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




'''
實作 & 交集

'''


'''
實作 聯集

'''


'''
實作 差集




'''


'''
實作 dict

原理: 在電腦的世界中，只要知道地址 我們就能最快的速度找到他，也就是 array ，只要知道
        索引值 就可以在 O(1) 時間 獲取值。

索引值 就是數字，所以只要把 key 值 透過某種方式 轉成數字，就行了!



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

# hash_table = [0]*20

# #加入
# while True:
#     key,value = input().split()
#     if key == "no":
#         break


#     index = get_hashval(key)
#     print(index)
#     if hash_table[index] == 0:
#         hash_table[index] = [key,value] 
#     else:
#         while hash_table[index] != 0:
#             index += 1
#             index = index % 20
#         hash_table[index] = [key,value]

# for i in hash_table:
#     print(i)

# #查詢
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


