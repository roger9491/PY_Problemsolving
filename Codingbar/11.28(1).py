# n = int(input())
# a = []
# c = []
# d = 0
# for i in range(n):
#     b = input()
#     a.append(b)
'''
a = [1,5,3,1,1,1]
d=1
i=0
a = [5,3,1,1,1]
i=1
a = [5,3,1,1,1]
i=2
a = [5,3,1,1]
i=3
a = [5,3,1]
i=4
錯誤
i=5

超出索引值
跳過某些數字

只能刪一個數字

6
1
5
3
1
1
1
1
字串.join(串列)
a = []
'''
# d = input()
# while True: #重複刪到每有重複為止
#     flag = True
#     for i in range(len(a)): #只刪一次
#         if a[i] == d:
#             del a[i]
#             flag = False
#             break
#     if flag:
#         break
# print(a)

'''
輸入 一行 n 個數字 控格格開 
二行 整數

輸出
索引值


ex
2 41 34 64 64 6
64


3

2 41 34 64 31 6
1


-1


index = 串列.index(資料)
'''
# a = [1,2,3,4]
# print(a.index(3))


'''
輸入 一行 n 個數字 控格格開 
二行 整數

輸出
整數的數量


2 41 34 64 64 6
64

2
'''
'''
不能用insert + 不能用串列 + 串列 
輸入 一行 n 個數字 控格格開 
二行 index
三行 data


輸出
整數的數量

2 41 34 64 64 6
5
99



2 41 34 99 64 64 6
'''
a=input().split()
index=int(input())
b=input()

ans = []
for i in range(len(a)):
    if i == index:
        ans.append(b)
    ans.append(a[i])

print(ans)

