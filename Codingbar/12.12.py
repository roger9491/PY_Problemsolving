'''
二維矩陣練習

week2 邊緣偵測

'''
# def check(i,j):
#     dire = [[1,0],[0,1],[-1,0],[0,-1]]
#     for x in dire:
#         if g[x[0]+i][x[1]+j] == '0':
#             return False
#     return True



# n1 = int(input())
# n2 = int(input())

# g = []
# for i in range(n1):
#     s = input().split()
#     g.append(s)

# ans = [[0]*n2 for i in range(n1)]

# for i in range(n1):
#     for j in range(n2):
#         if g[i][j] == "0":
#             ans[i][j] = "_"
#         elif g[i][j] == "1":
#             if check(i,j):
#                 ans[i][j] = "_"
#             else:
#                 ans[i][j] = "0"
            
# for i in range(n1):
#     print(" ".join(ans[i]))
'''
監聽

'''
# queue = []

# while True:
#     n = input()
#     if n == "no":
#         break

#     n = int(n)
#     queue.append(n)

#     while queue[0] < queue[-1] - 86400:
#         del queue[0]

#     print(len(queue))


'''
均攤時間複雜度

每一次insert 花的時間複雜度是多少




'''


# def insert(val):
#     global count
#     if count == len(array):
#         sum = 0
#         for i in range(len(array)):
#             sum = sum + array[i]
#         array[0] = sum
#         count = 1
#     array[count] = val
#     count += 1

# n = int(input())
# array = [0]*n

# count = 0

'''
https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/


'''
# class MaxQueue:

#     def __init__(self):
#         self.queue = []
#         self.Monotonic_queue = []
#     def max_value(self) -> int:
#         if self.Monotonic_queue:
#             return self.Monotonic_queue[0]
#         else:
#             return -1
#     def push_back(self, value: int) -> None:
#         while self.Monotonic_queue and self.Monotonic_queue[-1] < value:
#             del self.Monotonic_queue[-1]
#         self.Monotonic_queue.append(value)
#         self.queue.append(value)
#     def pop_front(self) -> int:
#         if self.queue:
#             temp = self.queue.pop(0)
#             if temp == self.Monotonic_queue[0]:
#                 del self.Monotonic_queue[0]
#             return temp
#         else:
#             return -1

'''
人行道樹的高低起伏



'''

# a = list(map(int,input().split()))

# n = int(input())
# ans = []
# queue = []
# for i in range(len(a)):
#     while queue and a[queue[-1]] < a[i]:
#         del queue[-1]

#     queue.append(i)

#     while queue and queue[0] < (i - n + 1):
#         del queue[0]

#     if i >= n - 1:
#         ans.append(a[queue[0]])

# ans = list(map(str,ans))
# print(" ".join(ans))

'''
https://codeforces.com/problemset/problem/66/B
灌溉田地
'''

# n = int(input())

# t = list(map(int, input().split()))

# length = n
# maxv = 0
# temp = 0
# for i in range(length):
#     temp = 0
#     temp1 = t[i]
#     for j in range(i,-1,-1):
#         if temp1 >= t[j]:
#             temp += 1
#             temp1 = t[j]
#         else:
#             break
#     temp1 = t[i]
#     for j in range(i+1,length):
#         if temp1 >= t[j]:
#             temp += 1
#             temp1 = t[j]
#         else:
#             break
#     if temp > maxv:
#         maxv = temp
#     # print(i,temp)
# print(maxv)

'''
n 皇后


1           2           3       4       5
 
2 3 4 5     3 4 5         

4 - 1 = 3

0 - 3 = - 3
'''
# import itertools
# n = int(input())
# a = []

# for i in range(n):
#     a.append(i)

# ans = itertools.permutations(a,n)
# ans = list(ans)
# count = 0
# for x in range(len(ans)):
#     flag = False
#     for i in range(n):
#         for j in range(i+1,n):
#             if j - i == abs(ans[x][i] - ans[x][j]):
#                 flag = True
#                 break
#         if flag:
#             break
#     else:
#         count += 1

# print(count)

'''
第一單元 
符號不動冥王
'''



'''

最大消波塊


'''

# a = list(map(int,input().split()))

# i = 0
# j = len(a) - 1
# ans = 0
# while i < j:

#     if ans < (j - i) * min(a[i],a[j]):
#         ans = (j - i) * min(a[i],a[j])
    
#     if a[i] > a[j]:
#         j -= 1
#     elif a[i] < a[j]:
#         i += 1
#     else:
#         i += 1
#         j -= 1
# print(ans)

'''

點石成金

'''

a = list(map(int,input().split()))

b = list(map(int,input().split()))

n = int(input())

total = 0

for i in range(len(a)): #n
    if b[i]:
        total += a[i]
# print(total)
maxv = 0
for i in range(len(a)-n+1): #n /2
    temp = 0
    for j in range(i,i+n):  #n/2
        if b[j] == 0:
            temp += a[j]
    maxv = max(maxv,temp)
print(total + maxv)

'''
時間複雜度還是  n**2

問題出在 查詢 哪一個區間最大值 出現問題


獨立出問題就是
输入一个长度为n的整数序列。接下来再输入m个询问，每个询问输入一对l, r。
对于每个询问，输出原序列中从第l个数到第r个数的和。
'''