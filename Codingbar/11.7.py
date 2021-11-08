'''
串列 a
索引值取值
加入資料 a.append(data)
刪除 del a[index]

a = [1,2,3,4,5,6]
迭代串列
(1)for i in a:
(2)for i in range(len(a)):
        a[i]
(3)while 
i = 0
a = [1,2,3,4,5,6]
while i<len(a):
    print(a[i])
    i+=1

a.index(data):
'''

'''
a = [3, 14, 13, 1, 17, 8, 1]
印出最大值的索引值
[3, 14, 13, 1, 17, 8, 1]
temp
'''
a = [3, 14, 13, 1, 17, 8, 1]
temp = 0
for i in range(1,len(a)):
    if a[i] > a[temp]:
        temp = i

print(temp)

'''
a = 5 b = 4
a = 4 b = 5




a = [3, 14, 13, 1, 17, 8, 1]
a = [14, 13, 3, 1, 17, 8, 1]


a = "123"
a = a + "32"

a = " 123"
a += " "
a += "4"
文字相加
'''

# for i in range(4):  # 0 1 2 3   
#     k=6-2*i
#     print(" "*i+"*"*k)

for i in range(4):
    s = ""  #空字串
    for j in range(i):
        s = s + " "
    for i in range(6-2*i,0,-1):
        s = s + "*"
    print(s)
    