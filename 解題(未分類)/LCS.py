'''
LCS 最常公共子序列
因為我們是判斷兩個字串，也就是說 我們可能今天 在不同的長度的情況下都分別 長度都不太一一樣，來個例子
A:    s a d s t o r y
B:    a d m i n s o r r y
    譬如說 A在長度為3時 B 在長度為5時 長度為 2 ad
          A在長度為5時 B 長度為1時   長度 1  a
          當然這個例子可能比較偏激，反正要明白的是 在不同長度下 或 同 長度下 所產生的 LCS長度會不一樣，
那要如何去解決這個問題呢? 首先 像這種 求最值得題目 我們不妨 先思考DP ，我們要求什麼? 兩個字串 的 LCS，所以 問題定義
dp[i][j] :求出 在A字串長度為i 以及 B字串長度為j時的 lcs，接這我們在想 他能不把問題 縮小 但是 也擁有 最優 子結構
也就是 縮小問題 的 最佳解 能不能 疊出 本來問題 的最佳解，答案是可以的 既然我們知道 
今天 A sad
    B  admins   這時候的長度 為2 現在我們把A












'''
a = input()
b = input()
al = len(a)
bl = len(b)
dp = [[0]*(bl+1) for i in range(al+1)]
for i in range(1,al+1):
    for j in range(1,bl+1):
        if i==4 or i == 3:
            print(a[i-1],b[j-1],dp[i-1][j-1])
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    print(dp[i])
print(dp[-1][-1])