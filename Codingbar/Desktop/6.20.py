'''
前綴和

求出最小連續子數組之和


'''
# n,m = map(int,input().split())

# k = list(map(int,input().split()))

# pre = []
# pre.append(0)
# c = 0
# for i in range(n):
#     c += k[i]
#     pre.append(c)

# minv = 10**9
# ans = 0
# for i in range(n-m+1):
#     # print(i,i+m)
#     temp = pre[i+m] - pre[i]
#     if temp < minv:
#         minv = temp
#         ans = i
# print(ans+1)

'''
前綴和簡單應用

點石成金

'''
# a=input().split() #2 1 3 0 2 8 5
# a=list(map(int,a))
# b=input().split() #1 0 1 1 0 1 0
# b=list(map(int,b))
# c=int(input()) #強制成功範圍

# #前綴和
# pre = [0]
# count = 0
# ans = 0
# for i in range(len(a)):
#     if b[i] == 0:
#         count += a[i]
#     else:
#         ans += a[i]
#     pre.append(count)

# maxv = -10**9
# for i in range(len(a)-c+1):
#     temp = pre[i+c] - pre[i]
#     if temp > maxv:
#         maxv = temp
# print(ans+maxv)


'''
前綴和簡單應用

(用前綴合去做)
輸入 一串數列 
輸入 index
輸入 target (保證不會大於數列總和)

當前index的數字 + 之後到終點索引值之間的數字 總和滿足大於等於 target ， 輸出該索引值


輸出
索引值



ex 1
2 1 5 4 3 5 3
0
8 

2
ex2
2 1 5 4 3 5 3
4
9

6
ex2 
2 1 5 4 3 5 3
5
20

3
'''
# All = list(map(int,input().split()))
# index = int(input())
# target = int(input())
# All_2 = []
# plus = 0
# for i in range(len(All)):
#     plus += All[i]
#     All_2.append(plus)

# a = max(All_2) - All_2[index]

# if a <= target:
#     for i in range(len(All_2)):
#         if All_2[i] > target:
#             print(i)
#             break
# else:
#     for i in range(len(All_2)):
#         if All_2[i] > target:
#             print(i)
#             break




'''
前綴和 進階練習
支點切割
https://zerojudge.tw/ShowProblem?problemid=f638
'''

'''
差分

差分 和 前綴和 區別
前綴和: 查詢區間和 O(1)

差分:   區間修改  O(1)
        查詢修改後的串列 O(n)


情境:
輸入一個數列
輸入n
接下來有n行
每一行輸入 c s e
代表 +c s起點 e終點
輸出修改完的數列


ex1
0 1 0 1 0 2 1
3
1 1 3
4 6 6
2 3 5

[0, 2, 1, 4, 2, 4, 5]


原: 0 1 0 1 0 2 1
2 3 5
    0 1 0 3 2 4 1

    0 1 -1 1 -1 2 -1
    0 1 -1 3 -1 2 -3    
    0 1  0 3  2 4  1

結論:
    (1) 先建立差分數列  (下一項-前一項)
        ex.
            原: 0 1 0 1 0 2 1
            差: 1 -1 1 -1 2 -1
    (2) c s e   c:+c    s:起點  e:終點
        差: 在s的值+c
            在e+1的值-c
    (3)全部修改完，在還原 累加

O(N*M)
10**4
'''

# a = list(map(int,input().split()))
# n = int(input())
# for i in range(n):
#     s = list(map(int,input().split()))
#     plus = s[0]
#     go = s[1]
#     end = s[2]
#     for j in range(go,end+1):
#         a[j] = a[j] + plus
# print(a)



'''
差分
https://leetcode.cn/problems/car-pooling/submissions/

'''
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         dif = [0]*1001
#         for i in trips:
#             dif[i[1]] += i[0]
#             dif[i[2]] -= i[0]
#         pre = []
#         total = 0
#         for i in dif:
#             total += i
#             pre.append(total)
#         for i in pre:
#             if i > capacity:
#                 return False
#                 break
#         else:
#             return True 
'''
差分進階練習
https://zerojudge.tw/ShowProblem?problemid=g597
'''

trips = [[2,1,5],[3,3,7]]
capacity = 4

'''

二分搜尋    條件: 串列必須是 小~大 大到小   O(logn)
            猜的數字一律固定在 下 ~ 上 的中間
下  上      log 統一都是2為底
0 ~ 100     n   每一次猜完都會使
#50             範圍變 一半
51 ~ 100    log8 = 3
#75
50 ~ 75
#63     62
63 ~ 75
#69     69
70 ~ 75
#73     72
70 ~ 72
#72     71  猜中
70 ~ 71
#70
71 ~ 71 
71

'''
# a = []
# for i in range(101):
#     a.append(i)
# print(a)

# target = int(input())
# i = 0   #下界
# j = 100 #上界

# while i <= j: 
#     mid = (i+j) // 2
#     print(i,j)
#     if a[mid] == target:
#         print(mid)
#         break
#     elif a[mid] > target:
#         j = mid - 1
#     else:
#         i = mid + 1
'''
建立一個串列 串列大小為 20~40
隨機加入數字(1,40) 湊滿這個大小

排序

輸入一個數字 

去搜尋這個數字 存在 印出 索引值
            不存在 印出 不存在

'''
# import random

# length = random.randint(20,40)
# print(length)
# a = []

# while len(a) < length:
#     n = random.randint(1,60)
#     if n not in a:
#         a.append(n)
# a.sort()
# print(a)

# target = int(input())
# i = 0   #下界
# j = length - 1 #上界

# while i <= j: 
#     mid = (i+j) // 2
#     if a[mid] == target:
#         print(mid)
#         break
#     elif a[mid] > target:
#         j = mid - 1
#     else:
#         i = mid + 1
# else:
#     print("不存在")

'''
二分搜尋+前綴和 進階練習

圓環出口
https://zerojudge.tw/ShowProblem?problemid=f581

7 3
2 1 5 4 3 5 3
8 2 1 5 
9 4 3 5
12 3 2 1 5 4

4

4 3
1 3 5 7
4 1 3
1 4 8 12
4 1

0  1   2   3  4   5   6   7
2, 9, 14, 15, 16, 18, 19 20

i = 4
j = 4

i = 4 + 1 = 5
17
'''
# import random

# t = []
# for i in range(7):
#     t.append(random.randint(1,20))

# t.sort()
# target = random.randint(1,20)
# print(target)
# print(t)
# i = 0
# j = len(t)-1

# while i <= j:
#     mid = (i + j) // 2

#     if mid > target:
#         j = mid - 1
#     elif mid < target:
#         i = mid + 1
#     else:
#         print("找到了",mid)
#         break

'''
目標  得到目標再串列裡的個數 O(n)

二分搜尋
n/2 n/2/2 n/2/2 
10**6

log10**6 = 20

2**10 == 10*3
2**20 == 10**6
2**30 = 2**10x2**10
O(logn) = 3
'''





'''
e283: APCS 類似題 - 小崴的特殊編碼
1.減少空白字元
2.轉換成某種數字
ex 0101 ==> 5

a = [0,0,0,0,0,'a','c','d',...]
ans =ans + a[5]
'''
# while True:
#     try:
#         n = int(input())
#         ans = ""
#         for i in range(n):
#             cool = input()
#             if cool == "0 1 0 1":   #5
#                 ans = ans + "A"
#             elif cool == "0 1 1 1": #6
#                 ans = ans + "B"
#             elif cool == "0 0 1 0": #7
#                 ans = ans + "C"
#             elif cool == "1 1 0 1":
#                 ans = ans + "D"
#             elif cool == "1 0 0 0":
#                 ans = ans + "E"
#             elif cool == "1 1 0 0":
#                 ans = ans + "F"
#         print(ans)

#     except:
#         break
# 
'''
    盡量變數不要設太多

'''
# # look = list(map(int,input().split()))
# a = look[0]
# b = look[1]
# n = int(input())
# times = 0

# for i in range(n):
#     All = list(map(int,input().split()))

#     good_a = 0
#     bad_a = 0
#     good_b = 0
#     bad_b = 0

#     total_a = 0
#     total_b = 0
#     for i in range(len(All)-1):
#         # if All[i] == a:
#         #     good_a += 1
#         # elif All[i] == -a:
#         #     good_a -= 1
#         # elif All[i] == b:
#         #     good_b += 1
#         # elif All[i] == -b:
#         #     good_b -= 1
#         if  All[i] == a:
#             good_a = good_a + 1
#         elif  All[i] == -a:
#             bad_b = bad_b + 1
#         elif  All[i] == b:
#             good_b = good_b + 1
#         elif  All[i] == -b:
#             bad_b = bad_b + 1
#     total_a = good_a - bad_a
#     total_b = good_b - bad_b
#     if total_a> 0 and total_b > 0:
#         times = times + 1
# print(times)


