# while True:
#     try:
#         # code

#     except:
#         break

# a = [1,2,3]
# a.insert(2,6)
# print(a)


'''
實作 insert()

輸入 數列 
輸入 索引值
輸入 數字
( 索引值 < 書列長度)

ex
1 2 3 4 5 6
3
99


1 2 3 4 5 6 7 8 9 19
2
44

[1,2,3,99,4,5,6]

[]+[]



'''



# a = list(map(int, input().split()))
# index = int(input())
# n = int(input())

# new = []
# for i in range(len(a)):
#     if i == index:
#         new.append(n)
#         i -= 1
#     else:
#         new.append(a[i])
# print(new)


'''
功能 就是想要刪掉所有 字串字首是a的值

修改這段程式碼
達到功能
(1)
    過濾 O(n)
(2)
    刪除 O(n**2)
'''
# #       0       1           2       3       4
# l = ["apple","answer","anaconda","banana","candy"]
# l2 = []
# for i in range(len(l)): #0 1 2 3 4
#     if l[i][0] != "a":
#         l2.append(l[i])
# print(l2)

'''
複製串列
(1)
l = [1,2,3,4,5,6]

l2 = []
for i in l:
    l2.append(i)

(2) 只適用在一維串列
    l = [1,2,3,4]
    l2 = l[:]   #淺複製

(3)
    l = [1,2,3,4]
    l2 = l.copy()
'''



# a = 10
# b = 5

# b = a
# b = 1
# print(a,b)
