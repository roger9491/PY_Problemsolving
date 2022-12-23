'''
最遠距離

n個的點的樹，點的編號為1~n
問你q次 從s出發 距離s最遠的距離多少

輸入
第一行 n, q
接下來 n - 1 行，每行 a, b
接下來 q 行， 代表起點s

輸出 
最遠距離

input
8 3
5 6
1 5
4 6
7 1
3 5
8 6
2 8
5
3
2

output
3
4
5
'''
# def dfs(y,z):
#     global flag
#     for i in dic[y]:
#         if i not in c:
#             c.append(i)
#             flag+=1
#             dfs(i,z)
#             if y==z:
#                 ans.append(flag)
#                 flag=0
# dic={}
# n,q=map(int,input().split())
# for i in range(n-1):
#     a,b=map(int,input().split())
#     if a not in dic:
#         dic[a]=[b]
#     else:
#         dic[a].append(b)
#     if b not in dic:
#         dic[b]=[a]
#     else:
#         dic[b].append(a)
# c=[]
# for i in range(q):
#     flag=0
#     ans=[]
#     c=[]
#     x=int(input())
#     dfs(x,x)
#     big=ans[0]
#     for j in range(len(ans)):
#         if ans[j]>big:
#             big=ans[j]
#     print(big)


# def dfs(n):
#     global ans
#     global c
#     ans = max(ans, c)

#     for i in v[n]:
#         if record[i] == 0:
#             c += 1
#             record[i] = 1
#             dfs(i)
#             c -= 1

# n, q = map(int,input().split())

# v = {}
# for i in range(n-1):
#     a, b = map(int,input().split())
#     if a in v:
#         v[a].append(b)
#     else:
#         v[a] = [b]
    
#     if b in v:
#         v[b].append(a)
#     else:
#         v[b] = [a]

# for i in range(q):
#     s = int(input())
#     record = [0]*(n + 1) 
#     record[s] = 1
#     ans = 0
#     c = 0
#     dfs(s)
#     print(ans)






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
零錢問題
    (1) 定義問題    這裡定義的問題 要確保保有最優子結構

    (2) 狀態轉移    定義好問題就是快樂的找狀態轉移

'''



'''
題目練習
https://judge.tcirc.tw/ShowProblem?problemid=d066

'''