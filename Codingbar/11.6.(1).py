'''
方格棋盤路線

w=
2   -2  3   3
-6  5   2   -8
4   7   -5  4

dp
2   0   3   3   思考怎麼來的
-4  5   7   -1
0   12  7   11

dp[i][j]

二維矩陣
dp = [[0]*a for i in range(b)]

最大總和

左上到右下角
條件: 只能 往右 往下n

初始值:


狀態定義
    dp[i][j]: 路徑總和  
    每一格的最大值(路徑總和)why?
    因為答案是 上 左 求得而來

狀態轉移 (未完成) why?
    i==0 and j!=0:
        dp[0][j]=L[0][j]+dp[0][j-1]
    j==0 and i!=0:
        dp[i][0]=L[i][0]+dp[i-1][0]

            路徑總和                + 權值
    dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + w[i][j]
    路徑總和 


'''
# a=input().split()
# L=[]
# for i in range(int(a[0])):
#     b=input().split()
#     b=list(map(int,b))
#     L.append(b)
# dp=[[0]*int(a[1])for i in range(int(a[0]))]
# dp[0][0]=L[0][0]
# # print(dp,"DP")
# # 2 0 0 0 
# # 0 0 0 0
# # 0 0 0 0
# for i in range(len(L)):
#     for j in range(len(L[0])):
#         if i==0 and j!=0:
#             dp[0][j]=L[0][j]+dp[0][j-1]
#         elif j==0 and i!=0:
#             dp[i][0]=L[i][0]+dp[i-1][0]
#         else:
#             dp[i][j]=L[i][j]+max(dp[i-1][j],dp[i][j-1])
#         # print(dp)

# print(dp[-1][-1])


'''
LCS

    T   A   T   G   C   A
A
T
C
A
G
A
T






'''
'''
a = [1,3,4,5,6,7,8]
print(max(a))

印出最大值的索引值

5 4 15 1 19 8 9

'''
# a=[1,2,3,4,5,6,7,8]
# M=a[0]
# x=len(a)
# for i in range(1,x):
#     if a[i-1] > a[i]:
#         continue
#     else: #a[i-1] <= a[i]
#         M=a[i]
# print(M)

a = [5, 4 ,15, 1, 19, 8, 9]
maxv_i = 0
for i in range(1,len(a)):
    if a[maxv_i] < a[i]:
        maxv_i = i

print(maxv_i)
