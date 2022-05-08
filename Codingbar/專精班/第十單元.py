'''
重複輸入
輸入no停止
輸入存到串列



輸入一個數字n，輸出n在串列的個數

# 重複輸入數字n
# 輸出n 在串列的個數
# 直到輸入no停止

印出串列的長度
ex
1
1
2
2
no
1
2
2
2
no
4


'''
c = []
while True:
    a = input("")
    if a == "no":
        break
    else:
        c.append(int(a))
b = int(input())
t = 0
for i in range(len(c)):
    if b == c[i]:
        t += 1
print(t)




"""
投票統計

"""

# t = []
# while True:
#     n = input()
#     if n == "no":
#         break
#     t.append(n)

# for i in range(len(t)):
#     if t.count(t[i]) > len(t) // 2:
#         print(t[i])
#         break


'''
隱藏謊言前置

輸入 1 + n 列，
第一列輸入 n 
接下來輸入n個數

印出串列
'''

'''
重複輸入長度為2字串 英文配數字
輸入no結束
若是字串的數字能被2整除就印出來

'''

'''
成雙成對
s6
c6
s9
h3
d9
c4
no

s6 c6
s9 d9
['h3', 'c4']
'''

# t = []
# while True:
#     n = input()
    
#     if n == "no":
#         break
    
#     for i in range(len(t)):
#         if t[i][1] == n[1]:
#             print(t[i],n)
#             del t[i]
#             break
#     else:
#         t.append(n)
# print(t)