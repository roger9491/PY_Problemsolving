#輸入
# weather = input("晴天")
# mood = input("心情好")
'''
or and 是邏輯運算符號
邏輯:布林值
True or False => True
Flase or True => True
+ - * / 是數字運算

'''
#or
# if weather == "yes" or mood == "yes":
#     print("想出去玩")

#and
# if weather == "yes" and mood == "yes":
#     print("出門玩")



#實現跟上面一樣功能的程式碼 不能用 or and

#輸入
# weather = input("晴天")
# mood = input("心情好")


#or
# if weather == "yes" or mood == "yes":
#     print("想出去玩")
# if weather == "yes":
#     print("想出去玩")
# elif mood == "yes":
#     print("想出去玩")

#and
# if weather == "yes" and mood == "yes":
#     print("出門玩")
# if weather == "yes":
#     if mood == "yes":
#         print("出門玩")



#判斷偶數
# num = 18
# if not (num % 2 != 0):
#     print("偶數")


# for abc in range(10):
#     print(abc)
'''
能讓使用著輸入五次成績

'''

#方法1
# number1 = int(input())
# number1 = int(input())
# number1 = int(input())
# number1 = int(input())
# number1 = int(input())

#方法2
# for i in range(5):
#     n1 = int(input())

'''
輸入 三筆學生成績
輸出 平均
'''
# total = 0
# for i in range(3):
#     n = int(input())
#     total = total + n
# print(total/3)

# a = [1,2,3,4,5]
# print(a[6]) #索引值必須是一個數字

# dic = {"冀衡":168,"柏勳":175}
# print(dic["冀衡"])
# print(dic["柏勳"])
# n = input()
# print(dic[n])

# if a in b
'''
if a in b
字串
if "cod"  in "coding":
    
串列
l = [1,2,3,4,"c"]    
if "c" in l

字典
dic = {"冀衡":168,"柏勳":175}

if "冀衡" in dic:

'''
'''
若是判斷 鍵值 存不存在

'''

# dic = {"冀衡":168,"柏勳":175}

# n = input()
# if n in dic:
#     print(dic[n])
# else:
#     print("無此資料")

'''
若是判斷資料呢?
'''
dic = {"冀衡":168,"柏勳":175}
# n = int(input())
# for i in dic:
#     if dic[i] == n:
#         print(i)
#         print("有此資料")

'''
事後增加資料

t = []
t.append(data)

字典?

dic[key] = value

串列修改
a = [1,2,3]
a[1] = 7

'''

# dic = {"冀衡":168,"柏勳":175}

# key = input()

# if key in dic:
#     print("有此資料")
# else:
#     value = int(input())
#     dic[key] = value

# print(dic)

'''
刪除

'''

# a = [1,2,3,4]
# del a[2]
# print(a)

dic = {"冀衡":168,"柏勳":175}
del dic["柏勳"]
print(dic)