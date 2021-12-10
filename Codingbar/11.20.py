'''
狀態定義:
    問最長共同子序列 長度

表格
i   T   A   T   G   C   A   j
A   0   1   1   1   1   1
T   1   1   2   2   2   2 
C   1   1   2   2   3   3
A   1   1   2   2   3   4
G   1   1   2   2   3   4
A   1   1   2   2   3   4
T   1   1   2   2   3   4

T   A   => T   A   T
A   1

T   A   T
A   1

A
T   A   T

(1) 當前的不一樣 把前面的狀態移過來
    dp[i][j] = dp[i][j-1]
(2) 一樣 dp[i][j] = dp[i-1][j] + 1

TAT
A

'''
a=input()
b=input()

"""
    T A T G C A
A   0 1 1 1 1 1 ###
T   1 1 2 2 2 2 
C   1 1 2 2 3 3
A   1 2 2 2 3 4
G   1 2 2 3 3 4
A   1 2 2 3 3 4
T   1 2 2 3 3 4


    T   A
A
T  
C
A
G       2/G
A       3/X
狀態定義:
    問最長共同子序列 長度

T A       (1)狀態轉移       (2) 子序列? 
ATCAG      比較方式


T A
ATCAGA    
            
dp[i][j] = dp[i-1][j] + 1
"""

# dp=[[0]*(len(a)+1) for i in range(len(b)+1)]


# #print(dp,"1")

# for i in range(1,len(b)+1):
#     for j in range(1,len(a)+1):
#         if b[i-1]==a[j-1]:
#             dp[i][j]=dp[i-1][j-1]+1
#         elif b[i-1]!=a[j-1]:
#             dp[i][j]= max(dp[i][j-1], dp[i-1][j])


#     print(dp[i],"2")

'''
    T   A   T   G   C   A
A
T               a
C           b   x
dp[i-1][j]
T   A   T   G
A   T
dp[i][j-1]
T   A   T
A   T   C

當前
T   A   T   G 
A   T   C 



A
G
AT





'''

'''
m x n
2   3
        0 1 2
    0   0 0 0
    1   0 0 0

'''
matrix = [[0]*3 for i in range(2)]
# 上    下      左      右
# i-1  i+1      j-1     j+1

dir = [[-1,0],[1,0],[0,-1],[0,1]]

for i in range(m):
    for j in range(n):
        for d in dir:
            x = i + d[0]    #方向
            y = j + d[1]
            if x < 0 or x >= m or y < 0 or y >= n:
                pass                                #條件
            else:
                #執行
            # if 0 <= x < m and 0 <= y < n:
            #       執行

    
