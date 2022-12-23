'''
1.dfs 搜索所有點

'''
# def dfs(i,j):
#     print("索引值",i,j)
#     print(matrix1[i][j])
#     print(record)
#     # input()

#     for x in dir:
#         now_i = i + x[0]
#         now_j = j + x[1]
#         if 0 <= now_i < 3 and 0 <= now_j < 3:
#             if matrix1[now_i][now_j] not in record:
#                 record.append(matrix1[now_i][now_j])    #紀錄
#                 dfs(now_i,now_j)    #走這條路

# matrix1 = [[1,2,3],
#            [4,5,6],
#            [7,8,9],]
# record = [1]    #用來記錄你走過路
# #       下     右    上     左
# dir = [[1,0],[0,1],[-1,0],[0,-1]]
# dfs(0,0)


# import sys	#必須先匯入sys
# for i in sys.stdin: #無限的輸入
#     n = int(i)
#     for i in range(n):
#         a = sys.stdin.readline().strip()
#         print(a)

'''
獨眼怪走迷宮1
'''


""" 




1. 暴力

猜密碼問題

8
_ , _ , _ ,_ ,_ ,_ ,_ , _ 
218340105584896

數字 小寫 大寫

2. 動態規劃

3. 貪心

4. 分治法






"""



'''
嘗試依照規律寫出遞迴




'''
# def f(n, s):
#     if n == 0:
#         return    
#     for i in range(3):
#         if n == 2:
#             print((i+1))
#         else:
#             print(10**(2-n) * s + (i+1))
#         f(n - 1, (i+1))

# f(2, 0)




# def f(n):
#     if n==4:
#         return
#     print(n)
#     if n>=1:
#         for i in range(1,4):
#             print(10*n+i)
#     f(n+1)
# f(0)






# def dfs(s, x):
#     if s == 0:
#         return
#     for i in range(3):
#         if s == n:
#             print((i + 1))
#         else:
#             print((i + 1) + (10**(n - s)) * (x + 1))
#         dfs(s - 1, i)

# n = int(input())
# dfs(n, 0)

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

def f(n,m):
    global ans
    if n==0:
        return
    for i in range(m+1):
        ans += str(i)
        if len(ans)==x:
            print(ans)
            ans = ans[:-1]
            continue
        f(n-1,m)
        ans = ans[:-1]
ans= ""
n,m=map(int,input().split()) 
x=n
f(n,m)

# st = ""
# def dfs(l,n):
#     global st
#     if l == 0:
#         print(st)
#         return
#     l = l - 1
#     for i in range(n+1):
#         st += str(i)
#         dfs(l,n)
#         st = st[:-1]

# a = input().split()
# lenth = int(a[0])
# num = int(a[1])
# dfs(lenth,num)

# n, m = map(int,input().split())

# def dfs(n, m, st):
#     if n == 0:
#         t.append(st)
#         return
#     for i in range(m+1):
#         st += str(i)
#         dfs(n-1, m, st)
#         st = st[:-1]

# t = []
# dfs(n,m, "")
# for i in t:
#     print(i)

""" 
分蘋果


"""
# def dfs(index):
#     global minv
#     if index == n:
#         a1 = 0
#         a2 = 0
#         for i in range(n):
#             if t[i] == 0:   
#                 a1 += a[i]
#             else:
#                 a2 += a[i]
#         minv = min(minv, abs(a1-a2))
#         return
#     for i in range(2):
#         t[index] = i
#         dfs(index+1)
# n = int(input())
# a = list(map(int,input().split()))
# t = [-1]*n
# minv = 10**9

# dfs(0)
# print(minv)

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


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         def f(count):
#             global ans 
#             if count == n:
#                 return 1
#             elif mem[count] != -1:
#                 return mem[count]

#             total = 0
#             for d in [1,2]:
#                 if count + d <= n:
#                     total += f(count + d)
#             mem[count] = total
#             return mem[count]
#         count = 0
#         ans = 0
#         mem = [-1]*(n + 1)
#         return f(0)

# /*
# 01. L1-5-1 爬樓梯(I)
# 暴力法 優化成 記憶化搜索
# */


#include <bits/stdc++.h>
# using namespace std;

# int record[1000000];
# int ans = 0;
# const int mod = 1e9+7;
# int ed;
# int dfs(int n)
# {
#     if (n == 0)
#     {
#         return 1;
#     }
#     else if (record[n] != -1)
#     {
#         return record[n];
#     }

#     long long tmp = 0;
#     for (int i = 1; i <= 3; i++)
#     {
#         if (n - i >= 0)
#         {
#             tmp = (tmp + dfs(n - i)) %1000000007;
#         }
#     }
#     record[n] = tmp;
#     return record[n];
# }

# int main()
# {

#     cin >> ed;
#     memset(record, -1, sizeof(record));
#     dfs(ed);
#     cout << record[ed];
# }
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
# n = int(input())
# dp = [0]*(n+1)
# dp[0] = 1
# dp[1] = 1
# for i in range(2,n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[n])


# /*
# 01. L1-5-1 爬樓梯(I)
# 記憶化搜索 優化成 遞推
# */

# // #include <bits/stdc++.h>
# // using namespace std;

# // int record[1000000];
# // int ans = 0;
# // const int mod = 1e9+7;
# // int ed;
# // int dfs(int n)
# // {
# //     if (n == 0)
# //     {
# //         return 1;
# //     }
# //     else if (record[n] != -1)
# //     {
# //         return record[n];
# //     }

# //     long long tmp = 0;
# //     for (int i = 1; i <= 3; i++)
# //     {
# //         if (n - i >= 0)
# //         {
# //             tmp = (tmp + dfs(n - i)) %1000000007;
# //         }
# //     }
# //     record[n] = tmp;
# //     return record[n];
# // }

# // int main()
# // {

# //     cin >> ed;
# //     memset(record, 0, sizeof(record));
    
# //     record[0] = 1;
# //     for (int i = 0; i <= ed; i++)
# //     {
# //         for (int j = 1; j <= 3; j++)
# //         {
# //             if(i - j >= 0){
# //                 record[i] = (record[i] + record[i-j]) %1000000007;
# //             }
# //         }
        
# //         // for (int i = 0; i <= ed; i++)
# //         // {
# //         //     cout << record[i] << " ";
# //         // }
# //         // cout << "\n";
        
# //     }
    

# //     cout << record[ed];
# // }

'''
作業
    02. L1-5-3 爬樓梯(II)
'''

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
零錢問題
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構

    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移


20,16,12,10,5,1
29

3
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
零錢問題    (優化版)
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構

    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移


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
搶分比賽


12  耐重
3 10 7 5    重量
4 15 10 7   分數

17
'''

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

w = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [[0]*(w+1) for i in range(len(a))]

def dfs(i, j):
    if i == -1 or j == 0:
        return 0
        
    print(i, j)
    if dp[i][j] != 0 :
        return dp[i][j]


    
    maxv = dfs(i - 1, j)

    if j >= a[i]:
        maxv = max(maxv, dfs(i - 1, j - a[i]) + b[i])
    dp[i][j] = maxv
    '''
    ans = max(dfs(i - 1, j), dfs(i - 1, j - a[i]) + b[i])
    
    '''
    for i in range(len(a)):
        print(dp[i])

    return maxv


print(dfs(len(a) - 1, w))


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
Limit = int(input())
Weight = list(map(int,input().split())) #重量
Scores = list(map(int,input().split())) #分數
dp = [[0]*(Limit+1) for i in range(len(Weight))]    #表格

for i in range(len(Weight)):
    for j in range(1,Limit+1):                      
        if j >= Weight[i]:  #15         7     +  dp[i][10 - 5]  7
            dp[i][j] = max(dp[i-1][j], Scores[i]+dp[i-1][j-Weight[i]])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])

'''
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構
        dp[i][j] : 放到第i項物品j耐重的情況下的最大價值
    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移



'''










'''
01背包問題:
有一個耐重為V的背包，n個物品，每個物品有Wi重量，價值Ci
W:物品list 重量
C:物品list 價值
定義:
    dp[i][j] : i:第i項物品放入，耐重為j的最大價值
狀態轉移:
    dp[i][j] = max(dp[i-1][j], dp[i-1][j-Wi]+Ci)
程式碼:
    for i in range(len(W)):
        for j in range(V):
            if j >= W[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]]+C[i])
            else:
                dp[i][j] = dp[i-1][j]

優化:

空間上: O(V*n) ==> O(V)
我們可以發現 dp[i][j] 是由 dp[i-1][j] 和 dp[i-1][j-W[i]]+C[i] 取最大而來，
若是把空間變1維 dp[i][j] ==> dp[j] ，意義變為j耐重的最大價值，也就是說我們捨棄
儲存前i項的耐重價值，因為由狀態轉移發現我們當前的狀態都是由前一項狀態而來的，
我們在放入新的物品之前，串列本身就是儲存前一項的值，所以沒必要每項都儲存起來。
然而 dp[i-1][j-W[i]]+C[i] 這個轉移式必須用到剩餘重量，為了避免放到重覆的，
我們的耐重迭代必須從大到小迭代。
程式碼:
    for i in range(len(W)):
        for j in range(V,-1,-1):
            if j >= W[i]:
                dp[j] = max(dp[j], dp[j-W[i]]+C[i])
程式碼:
    for i in range(len(W)):
        for j in range(V,w[i]-1,-1):
            dp[j] = max(dp[j], dp[j-W[i]]+C[i])


練習題
https://judge.tcirc.tw/ShowProblem?problemid=d075
'''


'''
完全背包

'''
# w = list(map(int,input().split())) #每個食物的飽足度    
# p = list(map(int,input().split()))  #每個食物價格
# length = len(w)     #有多少種
# dp = [[0]*101 for i in range(length)]   #表格
##直覺解法
#錯誤寫法
# for i in range(length):
#     for j in range(101):
#         if j >= w[i]:
#             for x in range(1,j // w[i] + 1):
#                 if j >= x*w[i]:
#                     dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]*x]+p[i]*x)
#                     #這裡的小細節，因為跟上一次比較所以並沒有保存最大值
#                     #它會嘗試的去兌換所有的同一種物品
#                 # print(i,j,dp[i][j],x)
        
#         else:
#             dp[i][j] = dp[i-1][j]
#     print(dp[i])

#正確解法
# for i in range(length):
#     for j in range(101):
#         if j >= w[i]:
#             total = 0
#             for x in range(1,j // w[i] + 1):
#                 total = max(total, dp[i-1][j-w[i]*x] + p[i]*x)
#             dp[i][j] = max(total, dp[i-1][j])
#         else:
#             dp[i][j] = dp[i-1][j]
    # print(dp[i])

## 原始解法
# for i in range(length):     #迭代每一種食物
#     for j in range(101):    #迭代每一個飽足度
#         if j >= w[i]:       #判斷飽足度能不能負荷食物
#             dp[i][j] = max(dp[i-1][j],dp[i][j-w[i]]+p[i])
#         else:                           #i:為什麼? i-1:食物只能是一個 i:食物無限
#             dp[i][j] = dp[i-1][j]
# dp = [0]*101
## 空間優化
# for i in range(length):
#     for j in range(101):
#         if j >= w[i]:       #判斷飽足度能不能負荷食物
#             dp[j] = max(dp[j],dp[j-w[i]]+p[i])
##找零錢解法
# for i in range(101):
#     for j in range(len(w)):
#         if i >= w[j]:
#             dp[i] = max(dp[i], dp[i-w[j]] + p[j])
# print(dp[-1][-1])

'''
進階練習題
https://codeforces.com/problemset/problem/189/A

中文解釋
https://www.luogu.com.cn/problem/CF189A 
'''

'''
有限背包
'''


# money = int(input())    #金額
# num = list(map(int,input().split()))    #物品數量
# money1 = list(map(int,input().split())) #特價
# money2 = list(map(int,input().split())) #原價
 
# dp = [[0]*(money+1) for i in range(len(num))]   #表格

# for i in range(len(money1)):
#     for j in range(1,money+1):
#         if j >= money1[i]:  #金額能不能買物品
#             maxv = 0    #儲存最大金額
#             for r in range(1,num[i]+1):     #迭代所有的數量
#                 if j >= money1[i]*r :    
#                     # 條件1:金額要大於等於 成本 且 
#                     maxv = max(maxv,dp[i-1][j-money1[i]*r]+money2[i]*r)   #dp[i-1] :記得要減一，原因是如果不減一就會用到
#                 else:
#                     break
#             dp[i][j] = max(dp[i-1][j],maxv)     #當前用過的物品
#         else:
#             dp[i][j] = dp[i-1][j]
   
# print(dp[-1][-1])
'''
money = int(input())
num = list(map(int,input().split()))
money1 = list(map(int,input().split()))
money2 = list(map(int,input().split()))

for i in range(len(money1)):
    for j in range(num[i]-1):
        money1.append(money1[i])
        money2.append(money2[i])

length = len(money1)
dp = [[0]*(money+1) for i in range(length)]

for i in range(length):
    for j in range(1,money+1):
        if j >= money1[i]: 
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-money1[i]]+money2[i])
        else:
            dp[i][j] = dp[i-1][j]
	#print(dp[j])

print(dp[-1][-1])
'''


'''
進階練習題
python  64分即可 可以想想看滿分解 
https://www.luogu.com.cn/problem/P6771

恰好01
https://codeforces.com/problemset/problem/294/B
https://www.luogu.com.cn/problem/CF294B
'''


'''
LCS
Longest Common Subsequence

'''

# s1 = input()
# s2 = input()
'''
    b   s   b   i   n   i   n   m
j   0   0   0   0   0   0   0   0
m   0   0   0   0   0   0   0   1
j   0   0   0   0   0   0   0   1
k   0   0   0   0   0   0   0   1
b   1   1   1
k
j
k
v

    T   A   T   G   C   A
A   0   1   1   1   1   1
T   1   1   2   2   2   2
C   1   1   2   2   3   3
A   1   2   2   2   3   4
G   1   2   2   3   3   4
A   1   2   2   3   3   4
T


'''
# dp = [[0]*(len(s1)+1) for i in range(len(s2)+1)]

# for i in range(1,len(s2)+1):
#     for j in range(1,len(s1)+1):
#         if s1[j-1] == s2[i-1]:
#             dp[i][j] = max(dp[i][j-1],dp[i-1][j-1]+1)   #因為 當前一樣 上一次的前一個肯定沒有當前的+1
#         else:
#             dp[i][j] = max(dp[i][j-1],dp[i-1][j])
#             # dp[i][j] = dp[i][j-1]
# print(dp[-1][-1])

'''
https://leetcode-cn.com/problems/longest-increasing-subsequence/submissions/
LIS
Longest Increasing Subsequence

2, 1, 4, 3, 6, 7, 5

    2   1   4   3   6   7   5
2   1   0   0   0   0   0   0 
1   1   1   0   0   0   0   0
4   1   1   2   0   0   0   0
3   1   1   2   2   0   0   0
6   1   1   2   2   3   0   0
7   1   1   2   2   3   4   0
5   1   1   2   2   3   4

    10  9   2   5   3   7   101 18
10  1   0   0   0   0   0   0   0
9   1   1   0   0   0   0   0   0
2   1   1   1   1   0   0   0   0
5   1   1   1   2   0   0   0   0
3   1   1   1   2   
7   
101    
18

    4   10  4   3   8   9
4   1
10  1   2 
4   1   2   1     
3   1   2   1   1
8   1   2   1   1   2
9   1   2   1   1   2   3

狀態定義:
    dp[i]: 以索引值i結尾的最長上升長度

狀態轉移

    1 ~ i-1 :j
    if n[i] > n[j]:
        dp[i] = max(dp[j]+1)

'''
# nums = [10,9,2,5,3,7,101,18]
# n = len(nums)
# dp = [0]*(n)
# for i in range(n):
#     dp[i] = 1
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j]+1)


#     print(dp)


# import random

# while True:
#     coins = [96,59,48,21,4]
#     money = random.randint(1,96)

#     #正確程式
#     coins = coins
#     money = money
#     dp = [10**9]*(money+1)

#     for i in range(money + 1):
#         if i == 0:
#             dp[0] = 0
#         else:   #i : 5
#             for j in coins: #1 2 3
#                 if i >= j:
#                     dp[i] = min(dp[i], dp[i-j]+1)
#         # print(i,dp)
#     # print(dp[-1])
#     ans1 = dp[-1]

#     #錯誤的程式
#     def a(x):
#         if x in dic:
#             return dic[x]
#         elif x<inf[-1]:
#             return 0
#         else:
#             p=[]
#             for i in inf:
#                 if x>i:
#                     p.append(a(x-i))
#             if 0 in p:
#                 p.remove(0)
#             if p==[]:
#                 return 0
#             else:
#                 return min(p)+1

#     #為何不遞迴加記憶化所需算的f(x)不適也比較少嗎
#     inf=coins
#     dic={0:0}
#     n=money
#     for i in inf:
#         dic[i]=1
#     #print(dic)
#     for j in range(1,n+1):
#         dic[j]=a(j)
#         #print(dic)
#     # print(dic)
#     # print(dic[n])
#     ans2 = dic[n]
#     print(ans1,ans2)
#     if ans1 != ans2:
#         print(coins,money)
#         break



'''
96,59,48,21,4
78
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

# def a(x):
#     # print(x)
#     if x in dic:
#         return dic[x]
#     elif x<inf[-1]:
#         return 0
#     else:
#         p=[]
#         for i in inf:
#             if x>i:
#                 p.append(dic[x-i])
#         # print(p)
#         while 0 in p:
#             p.remove(0)
#         # print(p)
#         if p==[]:
#             return 0
#         else:
#             return min(p)+1

# #為何不遞迴加記憶化所需算的f(x)不適也比較少嗎

# inf=list(map(int,input().split(",")))
# dic={0:0}
# n=int(input())
# for i in inf:
#     dic[i]=1
# #print(dic)
# for j in range(1,n+1):
#     dic[j]=a(j)
#     #print(dic)
# #print(dic)
# # for i in range(n+1):
# #     print(i,dic[i])
# print(dic[n])


'''
20,16,12,10,5,1
29
'''


'''
12
3 10 7 5
4 15 10 7


        0   1   2   3   4   5   6   7   8   9   10  11  12
3/4     0   0   0   4   4   4   4   4   4   4   4   4   4
10/15   0   0   0   4   4   4   4   4   4   4   15  15  15
7/10    0   0   0   4   4   4   4   10  10  10  14,15
5/7

14 = c[i]           +       dp[i-1][j-b[i]]
    第i個物品的價值         第i-2個物品的價值



(1)
定義問題
dp[i][j]:   目前放入i項物品的 j 耐重情況下的最大價值
(2)
狀態轉移
'''
a = list(map(int,input().split(",")))
n = int(input())
def f(n):
    global count
    if n == 0:
        record.append(count)
        return 0
    else:
        for i in range(len(a)):
            if n-a[i]>=0:
                count += 1
                f(n-a[i])
                count -= 1
count = 0
record = []
f(n)
print(min(record))

'''
'''

# def bfs():
#     global steps,L,R,n,P
#     queue=[0,"t"]
#     record={}
#     while queue:
#         now=queue.pop(0)
#         if now=="t":
#             steps+=1
#             queue.append("t")
#         else:
#             now=S[now]
#             if now==P:
#                 return True
#             else:
#                 if now>(n-1):
#                     continue
#                 else:
#                     for i in (-L,R):
#                         if now+i>0 and now+i<n and now+i not in record:#導致同層不同count
#                             queue.append(now+i)
#                             record[now+i]=1


# x=list(map(int,input().split()))
# n=x[0]
# P=x[1]
# L=x[2]
# R=x[3]
# steps=0
# S=list(map(int,input().split()))
# if bfs()==True:
#     print(steps)
# else:
#     print(-1)













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




