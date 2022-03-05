'''
https://www.luogu.com.cn/problem/P1102
P1102 A-B 数对


'''

n, c = map(int,input().split())

a = list(map(int,input().split()))

dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
# print(dic)
ans = 0
# print(dic)
for i in dic:
    if i + c in dic:
        ans += dic[i]*dic[i+c]
    # if i - c in dic:
    #     ans += max(dic[i],dic[i-c])

    # print(ans)
print(ans)


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
O(1)
'''
# def insert(val):    #(1) 0
#     global count
#     if count == len(array):
#         sum = 0
#         for i in range(len(array)): #O(n)
#             sum = sum + array[i]
#         array[0] = sum
#         count = 1
#     array[count] = val
#     count += 1

# n = int(input())   # 4
# array = [0]*n
# #len(array)
# count = 0
# insert(0)   #O(1)
# insert(0)   #O(1)
# insert(0)   #O(1)
# insert(0)   #O(1)

# insert(0)   #O(1)
# insert(0)   #O(n) 

'''

剑指 Offer 59 - II. 队列的最大值
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
人行道樹
'''



'''
 函數運算式求值
https://zerojudge.tw/ShowProblem?problemid=f640

砍樹
https://judge.tcirc.tw/ShowProblem?problemid=d030

'''

