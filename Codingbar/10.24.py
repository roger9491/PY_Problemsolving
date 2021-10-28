# a = [5,6,8,4,3]
# # a.sort()
# a = sorted(a)
# print(a)



'''
.split()    :分隔字串 => 串列
.join()     :合併串列 => 字串
a = ["1","1","1"]
b = "x".join(a)
print(b)
map(型態 , 串列) :轉串列裡的每個值得型態
a = [5,6,8,4,3]
a = list(map(str,a))
print("x".join(a))
'''


'''
實作 .join()

輸入 
第一行 文字 空格隔開
第二行 合併的文字

輸出
合併完的結果

ex
a b c d
12

a12b12c12d


'''
# s = input().split()
# a = input()
# ans = ""

# for i in range(len(s)):
#     if i == len(s) - 1:
#         ans += s[i]
#     else:
#         ans += (s[i] + a)
# print(ans)


# def s():
#     print(a + 1)
#     #小世界
# #----------
# #主世界
# a = 3
# s()

# def s():
#     a = 3
#     #小世界
# #----------
# #主世界

# s()
# print(a + 1)

# a = [7,2,3,5]
# pre = [7,9,12,17]



# def s():
#     global a    #宣告全域變數
#     a = a + 1
#     print(a + 1)

# a = 7
# s()

'''
輸入字串
判斷迴文
輸出 True/False
ex
121

121
True

122
221
False


12345
54321
False
'''
# # 54321
# string = "12345"
# temp = ""
# # range(首項,末項,-1)
# for i in range(len(string)-1,-1,-1):
#     temp += string[i]
# if temp == string:
#     print(True)
# else:
#     print(False)


10**6 ~ 10**7
n = 10**6
n**2
sorted()