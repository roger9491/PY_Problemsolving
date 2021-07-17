'''
感覺理解完 背包 很多dp 我都會先以背包思考看看~~
首先 來講講我為什麼會往背包 思考
"选取和不超过S的若干个不同的正整数" 這是背包的size，
所以我們 會 一個size 一個size推，為什麼? 
我們可以思考 今天 s 的最大的约数之和 跟之前的size有沒有關聯?
看著 題目給的例子 11 是由 4 和 6 的約數和所組成的
我們再接者想 所以 s 是 4 時 ，4的約數和最大嗎?
小於4的數字有 1 2 3 ，
2 的約數:1
3 的約數 : 1
2 與 3不可能 因為 2+3>5，
4 的約數有 1 2 ，1+2 = 3
所以答案是 是
那6就不再贅述~
既然我們確定 s 可以由子問題推出，基本上這題就能確認能用 背包解，
每一個數字都是我們的物品，而s 就是我們的size
推一遍就有感覺了~~
這時如果同學你還不確定， 我們可以拿小數據算算看 假設 s:6
    1   2   3   4   5   6
1   
2
3
4
5
6
請同學自行填完~

所以 狀態轉移方程就出來了

dp[i][j] = max(dp[i-1][j],dp[i-1][j-i]+total_divisor[i])
                (1)         (2)
(1) 可能上一次的比較大，那當然這一次也能繼續沿用
(2) 可能當前的 數字的約數和 + (size - 當前數字)的約數和
                            (確保不超過 size)
'''
def total(x):   #約數和
    t = 0
    for i in range(1,x):
        if x%i == 0:
            t += i
    return t
    
n = int(input())
if n == 1:  #特例1
    print(0)
else:
    dp = [[0]*(n+1) for i in range(n+1)]
    total_divisor = [0]*(n+1)

    for i in range(1,n+1):      #初始化
        dp[2][i] = 1

    for i in range(1,n+1):
        total_divisor[i] = total(i)     #建立 約數和的表，不然會爆掉~~


    for i in range(2,n+1):      #從2開始
        for j in range(1,n+1):
            if j >= i:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-i]+total_divisor[i])
            else:   #j < i會是負數，當然沿用上一次的
                dp[i][j] = dp[i-1][j]

    print(dp[-1][-1])