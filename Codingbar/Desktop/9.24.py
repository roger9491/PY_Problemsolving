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