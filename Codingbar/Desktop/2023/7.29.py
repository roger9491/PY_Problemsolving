""" 
獨眼怪試密碼

n個數字 m種可能

#QUESTION

獨眼怪忘記自己保險庫的密碼了！

他只記得密碼共N個數字，且都介於0~M 之間。



#INPUT

輸入只有一行 N, M (2<=N<=10, 1<=M<=9) 。



#OUTPUT

請依照字典序輸出所有密碼可能讓獨眼怪參考。



2 1

00
01
10
11

"""

# 全域變數
# def dfs(c, m):
#     global s
#     if c == n :
#         print(s)
#         return

#     for i in range(m+1):
#         s += str(i)
#         dfs(c+1, m)
#         s = s[:-1]


# s = ""
# n, m = map(int,input().split())
# dfs(0, m)



# 區域變數
# n, m = map(int,input().split())

# def dfs(n, m, st):
#     if n == 0:
#         print(st)
#         return
#     for i in range(m+1):
#         st += str(i)
#         dfs(n-1, m, st)
#         st = st[:-1]

# t = []
# dfs(n,m, "")



'''
記憶化搜索


費氏數列    遞迴版
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)


'''
# def f(n):
#     if n==0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1)+f(n-2)

# n=int(input())
# print(f(n))




'''
費氏數列    記憶化搜索
'''

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


https://leetcode.com/problems/climbing-stairs/submissions/
https://leetcode-cn.com/problems/climbing-stairs/submissions/
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
#實際走過一遍 dfs 從零開始
# def f(count):
#     if count == n:
#         ans[0] += 1
#     for d in [1,2]:
#         if count + d <= n:
#             f(count + d)
# n = int(input())
# ans = [0]
# f(0)
# print(ans[0])

#實際走過一遍 dfs 從 n 開始
# def f(count):
#     if count == 0:
#         ans[0] += 1
#     for d in [1,2]:
#         if count - d >= 0:
#             f(count - d)
# n = int(input())
# ans = [0]
# f(n)
# print(ans[0])


#第二種 發現 global 不需要
# def f(count):
#     if count == 0:
#         return 1
    
#     t = 0
#     for d in [1,2]:
#         if count - d >= 0:
#             t += f(count - d)
#     return t

# n = int(input())
# print(f(n))

# 第三種 優化
# def f(count):
#     if count == 0:
#         return 1
#     elif mem[count] != -1:
#         return mem[count]
#     t = 0
#     for d in [1,2]:
#         if count - d >= 0:
#             t += f(count - d)
#     mem[count] = t
#     return t

# n = int(input())
# mem = [-1]*(n+1)
# print(f(n))




'''
零錢問題

dfs
'''
# def dfs(n):
#     global count
#     global ans
#     if n == 0:
#         ans = min(ans, count)
#         return
            
#     for i in a:
#         if n >= i:
#             count += 1
#             dfs(n - i)
#             count -= 1


# a = list(map(int,input().split(",")))
# m = int(input())

# ans = 10**9
# count = 0
# dfs(m)
# print(ans)

'''
零錢問題

分解子問題
'''
# a = list(map(int,input().split(",")))
# m = int(input())

# ans = 10**9
# count = 0
# def dfs(n):
#     if n == 0:
#         return 0
#     minv = 10**9
#     for i in a:
#         if n >= i:
#             minv = min(minv, dfs(n - i) + 1)
#     return minv      

# print(dfs(m))

''' 
零錢問題    優化版
20,16,12,10,5,1
29

3

'''
# a = list(map(int,input().split(",")))
# m = int(input())

# dp = [-1]*(m + 1)
# ans = 10**9
# count = 0
# def dfs(n):
#     if n == 0:
#         return 0
#     elif dp[n] != -1:
#         return dp[n]
#     minv = 10**9
#     for i in a:
#         if n >= i:
#             minv = min(minv, dfs(n - i) + 1)
#     dp[n] = minv
#     return dp[n]


# dfs(m)
# print(dp[m])



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


'''

'''
嘗試用遞推的方式解決
     迴圈
'''

# 費式數列

# n=int(input())
# if n == 0:
#     print(0)
# else:
#     mem = [0]*(n + 1)
#     mem[1] = 1
#     for i in range(2, n+1):
#         mem[i] = mem[i-1] + mem[i-2]

#     print(mem[n])

# 找零錢
# a = list(map(int,input().split(",")))
# m = int(input())

# dp = [10**9]*(m + 1)
# dp[0] = 0
# for i in range(1,m+1):
#     for j in a:
#         if i >= j and dp[i-j] != 10**9:
#             dp[i] = min(dp[i], dp[i-j] + 1)
# print(dp[m])

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

題目練習
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



'''
搶分比賽


12  耐重
3 10 7 5    重量
4 15 10 7   分數

17

12
3 10 7 5
4 15 10 7  
'''
# dfs
# w = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# ans = 0
# score = 0
# def dfs(i, j):
#     global ans
#     global score
#     if i == -1 or j == 0:
#         ans = max(ans, score)
#         return 
    
#     if j >= a[i]:
#         score += b[i]
#         dfs(i-1, j-a[i])
#         score -= b[i]

#     dfs(i-1, j)

# dfs(len(a) - 1, w)
# print(ans)



# 暴力
# w = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))


# def dfs(i, j):
#     if i == -1 or j == 0:
#         return 0
    
#     maxv = dfs(i - 1, j)

#     if j >= a[i]:
#         maxv = max(maxv, dfs(i - 1, j - a[i]) + b[i])
#     return maxv


# print(dfs(len(a) - 1, w))

# 記憶優化

# w = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# dp = [[0]*(w+1) for i in range(len(a))]

# def dfs(i, j):
#     if i == -1 or j == 0:
#         return 0
        
#     print(i, j)
#     if dp[i][j] != 0 :
#         return dp[i][j]


    
#     maxv = dfs(i - 1, j)

#     if j >= a[i]:
#         maxv = max(maxv, dfs(i - 1, j - a[i]) + b[i])
#     dp[i][j] = maxv
#     '''
#     ans = max(dfs(i - 1, j), dfs(i - 1, j - a[i]) + b[i])
    
#     '''
#     for i in range(len(a)):
#         print(dp[i])

#     return maxv


# print(dfs(len(a) - 1, w))


'''

重/價   0   1   2   3   4   5   6   7   8   9   10  11  12  
3/4     0   0   0   4   4   4   4   4   4   4   4   4   4      
10/15   0   0   0   4   4   4   4   4   4   4   15  15  15
7/10    0   0   0   4   4   4   4   10  10  10  15  15  15
5/7     0   0   0   4   4   7   7   7   11  11  15
4 15 10 7
    15  

表格初始值 = 0
dp[i][j] = dp[i-1]
dp = [[0]*13 for i in range(4)]

'''
# Limit = int(input())
# Weight = list(map(int,input().split())) #重量
# Scores = list(map(int,input().split())) #分數
# dp = [[0]*(Limit+1) for i in range(len(Weight))]    #表格

# for i in range(len(Weight)):
#     for j in range(1,Limit+1):                      
#         if j >= Weight[i]:  #15         7     +  dp[i][10 - 5]  7
#             dp[i][j] = max(dp[i-1][j], Scores[i]+dp[i-1][j-Weight[i]])
#         else:
#             dp[i][j] = dp[i-1][j]
# print(dp[-1][-1])





