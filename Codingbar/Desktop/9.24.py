import itertools
l = ["a", "b", "c", "d"]     # n
# 功能 產生所有排列組合
# 重複 vs 不重複
#　O(n**n)     O(n!)
# 時間複雜度?
# O(n!) => n ? n > 10 就無法被judge接受 
# 不被 judge 接受 10**6 ~ 10**7 1000000     10000000
l = itertools.permutations(l, 4)
for i in l:
    print(i)



'''
https://codeforces.com/problemset/problem/66/B
灌溉田地
'''


'''
https://www.luogu.com.cn/problem/P8301
娘子

'''



'''
1566. 重复至少 K 次且长度为 M 的模式
https://leetcode.cn/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

'''
# def f1(arr, m, k):
#     ans = 0
#     for i in range(len(arr) - m + 1):
#         c = 0
#         t = arr[i:i+m]
#         # print(t)
#         for j in range(i,len(arr) - m + 1, m):
#             if t == arr[j:j+m]:
#                 c += 1 
#                 ans = max(ans, c)
#             else:
#                 c = 0
#             # print(arr[j:j+m], c)
#     if ans >= k:
#         return True
#     else:
#         return False

# arr = [3,2,2,1,2,2,1,1,1,2,3,2,2]
# m = 3
# k = 2
# print(f1(arr, m, k))

'''

index = 起點 0

a = 串列
0 , 1

0 1 2 3
index = 2
1 0
range(2)
'''

# for i in range(index, len(a):

# # 倒者數
# for i in range(index - 1, -1, -1):


# data = [1,2,3,4]
# for index in data:
#     print(index, i)
#     if i % 2 == 0:
#         data[index] = 99
#         # i = 99
# print(data)

# [1, 2, 3, 4]


a = ["1", "2", "3"]
print(" ".join(a))