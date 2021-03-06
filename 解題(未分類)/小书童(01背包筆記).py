'''
01背包 筆記
最初我們學習的是 用二維dp去儲存狀態，所以我們不需要擔心重複加到，什麼意思呢?
先來了解 什麼是01 背包 : 你有一個背包，背包有容量，有容量代表能放的東西有限，既然你今天會帶背包代表你會放東西進去(廢話)
好 情境是 你要去偷東西，因為受到了背包的容量限制，所以能偷的東西有限，所以長得比較帥的小朋友就知道，你要偷出的東西數量是要能
剛好放進背包裡但是是價值總和是最高的組合，譬如說 今天 背包能 裝 4 個size ，今天能偷的東西有 
1 size 手機(ph) 2000
3 size 筆記型電腦(note) 3000
4 size 吉他(gt)  4000 
長得比較帥的你就知道，要偷 手機+筆記型電腦 1+3 == 4 size，價值為7000，
但今天如果 東西變多了 容量變多了 代表組合變多了 ，你沒辦法用腦袋直接選出時，就必須要用電腦算~
那解決這樣問題的方法，最常見就是使用dp ，先想想他有沒有 
1. 最優子結構 :這個問題 分成子問題是能最優的嗎? 合併成原來的問題也是最優的嗎?
ans:在求4size 時
2. 重複子問題 :我的理解:這個問題的子問題是有限的  
為了完整理解dp解01背包，我們把這個例子用dp的思想完整的思考一遍，
因為今天 容量大小 有4size，所以我們可以 1size  1size 的求
先從 只有 note 能偷開始
        1     2      3       4
note    0     0      3000    3000(因為能偷的只有note 容量4size也只能放3size最大價值的)
    (1 2 note 塞不下)
再來能偷的有 gt
        1       2       3       4
note    0       0       3000    3000    
gt      0       0       3000    4000 (我們知道上一次 4size時最大的只有note，但今天有新的能偷得所以要比較)
    (1 2 gt放不下 所以這個0 "沿用上一次的")
新加入 手機
        1       2       3       4
note    0       0       3000    3000    
gt      0       0       3000    4000
ph      2000    2000    3000    5000(那這邊有個細節 4size時 一樣要跟上一次比，而新加入的手機 1 size 所以還剩3size 所以要加3size最大的)
                                (這邊可以體現最優子結構)
所以你在決定每一次的時候 都要考慮上一次的最大 和 這一次新加入的東西 + 剩下容量能放的(參考上一次這個容量能求出最大的)














'''


n,m,k,r = list(map(int,input().split()))
nt = list(map(int,input().split()))
mt = list(map(int,input().split()))
mg = list(map(int,input().split()))


dp = [[0]*(r+1) for i in range(len(mg))]


for j in range(len(mt)):
    for i in range(mt[j],r+1):
        dp[j][i] = max(dp[j-1][i],dp[j-1][i-mt[j]]+mg[j])

            
for i in range(r+1):
    if dp[len(mt)-1][i] >=k:
        time = i
        break

time = r - time
total = 0
c = 0
for i in nt:
    total += i
    c += 1
    if total > time:
        c -= 1
        break
print(c)
        
