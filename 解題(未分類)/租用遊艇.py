'''
這題的矩陣是"鄰接串列"，一時半會還真看不出來....
題目 會給一個半矩陣 表示 出租站之間的租金，因為是一個半矩陣 所以基本上我們可以認定他 每一個出租站都可達到，只是金額不同
所以我們就是要從中找尋 最少花費，
而目標很明確 1 到 n ，
這時候 又可以聯想到 背包
n 是 size
每加入一個中轉站，代表每加入一個物品 必須更新
所以 如果 加入中轉站 造成的金額比較小就 更新
     否 就沿用上一次的
dp[i][j] = min(dp[i-1][j],dp[i-1][i]+matrix[i-1][j-i-1])
                (1)         (2)
(1) 之前的金額
(2) 新加入中轉站 所更新的金額

'''
n = int(input())

matrix = []
dp =[ [0]*(n+1) for i in range(n+1) ]
for i in range(n-1):        #鄰接表
    e = list(map(int,input().split()))
    matrix.append(e)

for i in range(2,n+1):      #初始化
    dp[1][i] = matrix[0][i-2]

for i in range(2,n+1):
    for j in range(1,n+1):
        if j > i:
            dp[i][j] = min(dp[i-1][j],dp[i-1][i]+matrix[i-1][j-i-1])    #狀態轉移
        else:   
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])