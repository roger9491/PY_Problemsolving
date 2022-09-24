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

