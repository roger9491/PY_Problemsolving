'''
記憶化搜索


費氏數列    遞迴版
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)
'''

# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return f(n-1) + f(n-2)

# n = int(input())
# print(f(n))


'''
費氏數列    記憶化搜索
'''

# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif mem[n] != 0:
#         return mem[n]
#     '''
#     totoal = 0
#     判斷 mem[n-1] != 0
#         totoal += mem[n-1]
#     else:
#         f(n-1)
#     判斷 mem[n-2] != 0
#         totoal += mem[n-2]
#     return total
#     '''
#     mem[n] = f(n-1) + f(n-2)
#     return mem[n]

# n = int(input())
# mem = [0]*(n+1)
# print(f(n))

# dic = {}
# def f(n):
#     if n < 2:
#         return n
#     if n in dic:
#         return dic[n]
#     else:
#         dic[n] = f(n-1) + f(n-2)
#         return dic[n]
    
# print(f(50)) #8








# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif l[n] != -1:
#         return l[n]
#     l[n] = f(n-1) + f(n-2)
#     return  l[n]

# n = int(input())
# l = [-1]*(n+1)

# print(f(n))


'''
來進階一點的題目

走樓梯 如用暴力法解決?

核心思想 真的走過一遍

輸入
第幾層

輸出
走法數量


'''
# def f(n):
#     global count 

#     if n == end:
#         count += 1
#         return
#     else:
#         for i in [1,2]:
#             if n + i <= end:
#                 f(n+i)

# count = 0
# end = int(input())
# f(0)
# print(count)

# def f(n):
#     if n == 0:
#         return 1
#     elif mem[n] != 0:
#         return mem[n]
#     else:
#         temp = 0
#         for i in [1,2]:
#             if n - i >= 0:
#                 temp += f(n-i)
#         mem[n] = temp
#         return mem[n]

# count = 0
# end = int(input())
# mem = [0]*end
# f(end)
# print(mem[-1])



#第一種
#實際走過一遍
# def f(count):
#     global ans 
#     if count == n:
#         ans += 1
#     for d in [1,2]:
#         if count + d <= n:
#             f(count + d)
# n = int(input())
# count = 0
# ans = 0
# f(0)
# print(ans)

#第二種

# def f(count):
#     global ans 
#     if count == 0:
#         ans += 1
#     for d in [1,2]:
#         if count - d >= 0:
#             f(count - d)
# n = int(input())
# count = 0
# ans = 0
# f(n)
# print(ans)


# def f(count):
#     global ans 
#     if count == 0:
#         return 1
#     elif mem[count] != 0:
#         return mem[count]

#     total = 0
#     for d in [1,2]:
#         if count - d >= 0:
#             total += f(count - d)
#     mem[count] = total
#     return mem[count]

# n = int(input())
# count = 0
# mem = [0]*(n+1)

# f(n)
# print(mem[-1])




# #第一種方法
# def f(n):
#     global ans
#     if n == target:
#         ans += 1
#         return
#     if n + 1 <= target:   
#         f(n+1)
#     if n + 2 <= target: 
#         f(n+2)    

# target = int(input())
# ans = 0
# f(0)
# print(ans)

#第二種方法

# def f(n):
#     global ans
#     if n == 0:
#         ans += 1
#         return
#     for d in [1,2]:
#         if n - d >= 0:
#             f(n-d)

# target = int(input())
# ans = 0
# f(target)
# print(ans)

'''
分析寫法

優化
'''
# def f(n):
#     global ans
#     # print(n,l[n])
#     if n == 0:
#         return 1
#     elif l[n] != -1:
#         return l[n]
#     count = 0
#     for d in [1,2]:
#         if n - d >= 0:
#             count += f(n-d)
#     l[n] = count
#     return l[n]
# target = int(input())
# ans = 0
# l = [-1]*(target+1)
# f(target)
# print(l[-1])

'''
也可寫成 費式數列
'''



'''
DP Dynamic programming 動態規劃
他是一種算法思想 常見的算法思想 : 分治 貪心 窮舉
核心思想: 通過把原問題分解為相對簡單的子問題的方式求解複雜問題的方法。

我們先來看 能用動態規劃解決問題的條件
最佳子結構
    每個階段的最優解是由之前的某個或某些狀態而來的
重疊子問題
    不同階段的最優解含有重複的之前狀態的最優解
無後效性
    當前的狀態是由之前的狀態的最優解得來，而不管從何而來。
    最短路步數是無後效性的，但是最短路徑就有後效性
    
# 所以我們會發現用動態規劃解決的題目通常會用串列來記錄

實作方式:
    遞推
    記憶化搜索

回頭來看看之前寫的記憶化搜索，想想看如何轉成遞推?
費式數列 遞推

那回到小朋友走樓梯
    如何用動態規劃的方式思考? 如何用動態規劃解決?
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構
        dp[i]: 第i層的走法數量
    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移
        dp[0] = 1 邊界
        dp[1] = 1 邊界
        dp[i] = dp[i-1] + dp[i-2]

5 8
0 1 2 3 4 5
1 1 2 3    
dp[2] = dp[1] + dp[0]
dp[3] = dp[2] + dp[1]

dp[i] = dp[i-1] + dp[i-2]

https://leetcode.com/problems/climbing-stairs/submissions/
https://leetcode-cn.com/problems/climbing-stairs/submissions/
'''
'''
嘗試用遞推的方式解決
     迴圈
'''
n = int(input())
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])


'''
零錢問題
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構

    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移

'''



'''
題目練習
https://judge.tcirc.tw/ShowProblem?problemid=d066

'''










'''
01 背包
https://judge.tcirc.tw/ShowProblem?problemid=d075
'''

'''
分組背包
https://www.luogu.com.cn/problem/P1757
3 5
2
1 2
2 4
1
3 4
1
4 5 

8

'''

# m,n = map(int,input().split())

# item = {}
# for i in range(n):
#     a = list(map(int,input().split()))
#     if a[2] not in item:
#         item[a[2]] = [[a[0],a[1]]]
#     else:
#         item[a[2]].append([a[0],a[1]])
# print(item)
# dp = [[0]*(m + 1) for i in range(len(item))]
# print(len(dp))
# index = 0
# for i in item:
#     for j in range(m + 1):
#         maxv = -10**9
#         w = 0
#         for x in item[i]:
#             if j >= x[0]:
#                 if maxv < x[1]:
#                     maxv = x[1]
#                     w = x[0]
#         dp[index][j] = max(dp[index-1][j],dp[index-1][j-w] + maxv)
#     # print(dp[index])
#     index += 1
# dp = [0]*(m + 1)
# for i in item:
#     for j in range(m,-1,-1):
#         maxv = -10**9
#         w = 0
#         for x in item[i]:
#             if j >= x[0]:
#                 if maxv < x[1]:
#                     maxv = x[1]
#                     w = x[0]
#         dp[j] = max(dp[j],dp[j-w] + maxv)
#     # print(dp[index])
# # print(dp)
# print(dp[-1])



'''
https://codeforces.com/problemset/problem/294/B
背包問題
恰好裝滿的01背包

5
1 12
1 3
2 15
2 5
2 1
'''
# n1 = int(input())

# v = []
# w = []
# total_v = 0
# total_w = 0
# for i in range(n1):
#     a,b = map(int,input().split())
#     v.append(a)
#     w.append(b)
#     total_v += a
#     total_w += b

# dp = [[-10**9]*(total_v + 1) for i in range(n1)]

# for i in range(n1):
#     for j in range(total_v + 1):
#         if j == v[i]:
#             dp[i][j] = max(dp[i-1][j],w[i])
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j - v[i]] + w[i])
#         # elif j > v[i]:
#         #     dp[i][j] = max(dp[i-1][j], dp[i-1][j - v[i]] + w[i])
#         # else:
#         #     dp[i][j] = dp[i-1][j]
#     # print(dp[i])

# for i in range(1,total_v + 1):
#     if i >= total_w - dp[-1][i]:
#         print(i)
#         break


'''

L1          =>  L2          => L3
(APCS第一題)    (APCS第二題)    (Leetcode => APCS => 落谷 /Codeforces)


'''

'''
來進階一點的題目

走樓梯 如用暴力法解決?

核心思想 真的走過一遍

輸入
第幾層

輸出
走法數量


複習上週講到的走樓梯

'''

#第一種
#實際走過一遍
# def f(count):
#     global ans 
#     if count == n:
#         ans += 1
#     for d in [1,2]:
#         if count + d <= n:
#             f(count + d)
# n = int(input())
# count = 0
# ans = 0
# f(0)
# print(ans)

#第二種

# def f(count):
#     global ans 
#     if count == 0:
#         ans += 1
#     for d in [1,2]:
#         if count - d >= 0:
#             f(count - d)
# n = int(input())
# count = 0
# ans = 0
# f(n)
# print(ans)

'''
分析寫法

優化
'''
# def f(count):

#     if count == 0:
#         return 1
#     if mem[count]:
#         return mem[count] 

#     total = 0
#     for d in [1,2]:
#         if count - d >= 0:
#             total += f(count - d)
#     mem[count] = total
#     return mem[count]
# n = int(input())
# mem = [0]*(n + 1)
# count = 0
# ans = 0
# f(n)
# print(mem[-1])



# def f(count):   #count : 當前走到第幾層
#     if count == 0:  #走到底部 算一條路
#         return 1

#     if mem[count] != -1:
#         return mem[count]
#     total = 0
#     for d in [1,2]: #
#         if count - d >= 0:
#             total += f(count - d)
#     mem[count] = total
#     return mem[count] 
# n = int(input())
# count = 0
# ans = 0
# mem = [-1]*(n+1)
# f(n)
# print(mem[-1])

# def f(count):
#     global ans 
#     if count == 0:
#         return 1
#     elif mem[count] != 0:
#         return mem[count]

#     total = 0
#     for d in [1,2]:
#         if count - d >= 0:
#             total += f(count - d)
#     mem[count] = total
#     return mem[count]

# n = int(input())
# count = 0
# mem = [0]*(n+1)

# f(n)
# print(mem[-1])

'''
遞推

'''
# n = int(input())
# count = 0
# mem = [0]*(n+1)
# for i in range(n+1):    #0~n
#     if i == 0 or i == 1:
#         mem[i] = 1
#     else:
#         mem[i] = mem[i-1] + mem[i-2]
    

# print(mem[-1])


'''
DP Dynamic programming 動態規劃
他是一種算法思想 常見的算法思想 : 分治 貪心 窮舉
核心思想: 通過把原問題分解為相對簡單的子問題的方式求解複雜問題的方法。

我們先來看 能用動態規劃解決問題的條件
最佳子結構
    每個階段的最優解是由之前的某個或某些狀態而來的
重疊子問題
    不同階段的最優解含有重複的之前狀態的最優解
無後效性
    當前的狀態是由之前的狀態的最優解得來，而不管從何而來。
    最短路步數是無後效性的，但是最短路徑就有後效性
    
# 所以我們會發現用動態規劃解決的題目通常會用串列來記錄

實作方式:
    遞推
    記憶化搜索

回頭來看看之前寫的記憶化搜索，想想看如何轉成遞推?
費式數列 遞推

那回到小朋友走樓梯
    如何用動態規劃的方式思考? 如何用動態規劃解決?
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構
        dp[n]: 走到第n層有幾種走法
    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移
        dp[5] = dp[4] + dp[3]
        dp[n] = dp[n-1] + dp[n-2]
https://leetcode.com/problems/climbing-stairs/submissions/
https://leetcode-cn.com/problems/climbing-stairs/submissions/
'''
'''
嘗試用遞推的方式解決
     迴圈
'''

 



''' 
零錢問題
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構
        dp[n]:  n零錢的最少硬幣數量
    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移
        if n == 0:  #思考邊界
            dp[n] = 0
        else
            dp[n] = min(dp[n-c1],dp[n-c2]..dp[n-cn]) + 1
'''
# coins = list(map(int,input().split(',')))
# money = int(input())
# dp = [10**9]*(money+1)

# for i in range(money + 1):
#     if i == 0:
#         dp[0] = 0
#     else:   #i : 5
#         for j in coins: #1 2 3
#             if i >= j:
#                 dp[i] = min(dp[i], dp[i-j]+1)
#     print(i,dp)
# print(dp[-1])


'''
題目練習
https://judge.tcirc.tw/ShowProblem?problemid=d066

    (1) 定義問題    這裡定義的問題 要確保保有最優子結構
        dp[n]:  到達n的最小分數
    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移
        dp[n] = dp[n-1] + dp[n-2] 變化?

   index
    0 0
    1 0
    2 1
    3 2


https://judge.tcirc.tw/ShowProblem?problemid=d069

'''

# n = int(input())

# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return f(n-1) + f(n-2)

# n = int(input())


# def a(n):
#     if n == 0:
#         record[0] = 0
#         return 0
#     elif n == 1:
#         record[1] = 1
#         return 1
#     else:
#         if record[n]!= -1:
#             return record[n]
#         else:
#             record[n] = a(n-1) + a(n-2)
#             return record[n]
# record = [-1]*(n+1)

# print(a(n))
# print(f(n))