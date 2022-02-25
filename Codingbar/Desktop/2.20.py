# p = [2,4,1,3,7,6,9]
# for i in range(1,6):
#     m = i
#     temp = 0
#     for j in range(7):
#         temp += p[j]*(j-m)
#     print(m,temp)

# def binarysearch(pre_sum,target):
#     n=0
#     m=len(pre_sum)-1
#     while m>=n:
#         mid=(m+n)//2
#         if pre_sum[mid]==target:
#             return ((mid)%P[0])
#         elif pre_sum[mid]<target:   #找到>=Sum且最接近的
#             n=mid+1
#         else:
#             if pre_sum[mid-1]<target:
#                 return ((mid)%P[0])
#             else:
#                 m=mid-1
# #圓環出口 出錯
# P=list(map(int,input().split()))
# inf=list(map(int,input().split()))
# tasks=list(map(int,input().split()))
# pre_sum=[]
# a=0
# for i in range(len(inf)):
#     a+=inf[i]
#     pre_sum.append(a)
# #用二分找出指定房間
# b=0
# now_tasks=0
# now_index=0
# for p in range(len(tasks)):
#     now_tasks+=tasks[p]
#     if now_tasks>pre_sum[-1]:
#         now_tasks-=pre_sum[-1]
#     print(p,binarysearch(pre_sum,now_tasks))
#     now_index+=binarysearch(pre_sum,now_tasks)
#     (now_index)=(now_index)%P[0]
#    # problem is 會回歸
# print(now_index)
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
'''
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

'''


'''
兩個數組的交集 (1)
https://leetcode-cn.com/problems/intersection-of-two-arrays/

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
'''
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
堆疊 

串列
push
    a.append()

pop
    del a[-1]
    a.pop() 刪除 + 取值


c/c++ 陣列 
先宣告陣列大小

(([])([]))

(([)

配對的時候發生?

'''

a=input()
b=[]
c=[]
for i in a:
    if i in '()/{/}[]':
        b.append(i)
print(b)
for j in range(len(b)):
    if b==[]:
        break
    for i in range(len(b)):
        if i==len(b)-1:
            break
        if b[i]+b[i+1] =="()"or b[i]+b[i+1] =="{}"or b[i]+b[i+1] =="[]":
            del b[i]
            del b[i+1]
            break
    print(j,b)
if b==[]:
    print('True')
else:
    print("False")


