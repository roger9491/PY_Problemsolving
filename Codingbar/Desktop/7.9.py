'''
10 20 30

1 2 3

5 6 7
'''
from re import L


a = ['a','b','c']
print(a)

'''
a+b+c



字串 => 串列 字串.split()
串列 => 字串

'''
a = "".join(a)
print(a)



'''
輸入一行字串，每個字串都會用空格分開
輸入一個字串
#join()不能用


ex
abc 456 ry
xxx


abcxxx456xxxry

["abc", "456", "ry"]
c = ""
c = c + a[0]
c = c + b
c = c + a[1]
c = c + b
'''
# l = ['1','2','3']
# print(" ".join(l))
# print(*l)


'''
輸入一個文字

輸出 字首掉到最後面

ex
apple

pplea



輸入字串
首相
末向
間隔
apple
1
3
1
輸出
print(a[1:3:1])
'''

n = input()

n += n[0]
s = ""
# for i in range(1,len(n)):
#     s += n[i]
s += n[1:]
print(s)

'''
實作replace
(不能用replace)

輸入原字串
輸入 替換目標
輸入 替換字原

輸出被替換後的字串
ex
(1)
12341235
1
x

x234x235
(2)
abacccbbae
a
999


999b999cccbb999e
(3)
663136681366
6
36

363631336368133636
print("663136681366".replace("6","36"))

自己用replace來檢驗
'''

