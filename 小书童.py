'''
如果你能算出 k分以上最小時間，你就能使用貪心法求出 能做多少題，
所以你可能分兩部分
1. 算出 k分以上最小時間
2.貪心法求出 能做多少題(很簡單就不說了)

1.
所以 dp[j][i]: 有j個種類的作業 i分鐘內 最大分數 j:加入前j個作業種類的時間 所更新的狀態 i:時間
那按照剛學過的 01 背包 j:就是偷的東西種類的個數  i:就是背包的size
for j in range(len(mt)):
    for i in range(mt[j],r+1):
        dp[j][i] = max(dp[j-1][i],dp[j-1][i-mt[j]]+mg[j])
                                    上一個種類 第 i-mt[j]個時間的的最大分數 + 新作業所需mt[j]個時間，當前新加入的種類的分數  
那這就完成了~~
但是我們還可以進一步做空間上的優化
之前的種類我們其實不關心，我們只需關心 新加入種類 更新完的分數，我們只在意這個 所以我不必儲存之前種類 的分數，
所以dp[j][i] -> dp[i] =  max(dp[i],dp[i-mt[j]]+mg[j])
                        dp[i]:就已經是代表上一次的分數  , dp[i-mt[j]]+mg[j]:一樣
我們的迴圈設定也要改變，內層迴圈要改
先思考為什麼要改?
dp[i] =  max(dp[i],dp[i-mt[j]]+mg[j])
因為 dp[i-mt[j]]+mg[j] 因為這一句 會 + 到自己更新完的分數 導致 重複性加分
ex 會先跑到時間 10 分 (分數5分)， 當跑到時間 20 分時 就會在 加一次 5分
所以內層迴圈 必須改成 由大時間 跑到小時間~~


'''
n,m,k,r = list(map(int,input().split()))
nt = list(map(int,input().split()))
mt = list(map(int,input().split()))     #作業時間所儲存的串列
mg = list(map(int,input().split()))     #作業分數所儲存的串列


dp = [0]*(r+1)  #初始化


for j in range(m):    #m: 作業的數量
    for i in range(r,mt[j]-1,-1):   
        dp[i] = max(dp[i],dp[i-mt[j]]+mg[j])

            
for i in range(r+1):
    if dp[i] >=k:       #搜尋哪個時間 會達到及格分數
        time = i
        break

time = r - time     #剩下的分數
total = 0
c = 0               # 做幾題題目
for i in nt:        #nt:刷題時間的串列
    total += i
    c += 1
    if total > time:
        c -= 1
        break
print(c)
