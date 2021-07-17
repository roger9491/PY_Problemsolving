'''
題解:
題目是說要刪數，並求出最小的，我們可以反過來想，變 生成 最小的數，譬如說 題目給6個數字 ，要刪掉兩個， 不就是等於生成4個數字嗎?
我們來以生成 來思考 如何 生產出最小的數字，
首先 第一個數字 一定找最小的 毋庸置疑，但往後都是這樣找嗎?來看個例子~
ex 175438 刪1 ，也就是從中選出4個數 如果小到大找的話 ans: 17543  
很明顯 最佳解是 15438 所以問題在哪? 問題在你找的數 必須也要考慮位置
再一個例子 1638 刪1 很明顯的 是 138，所以從這兩個例子來看， 如果 要考慮的數字 中間只要相隔一個數字 而這個數字 比左右兩邊小
1  6     3     8 :6 與 8 就是要選的，不管怎麼樣 6的位置就是比 8 還要大，所以當然選 8 ，盡管今天 6換成4 也一樣，
      (中間的)
所以這就是 考慮位置， 所以今天有個 思路 就是 如果你的高位 是 比較小的數字 接下來的數字就選 低位的 ，而不考慮 比他高位的數字
1 3 4 2  9 9 9  刪2 ，也就是產出 5個數字， 1 一定選 再來是 2，那再來呢? 應該選3 還是 9?
當然選 9 ，因為我剛上述的 2 是高位 比較小的，所以剩下的數字盡量找低位，但是 但是
這個前提 是不是 2 的右邊的數字 的數量剛好 ''足夠''我們選出來的數? 沒錯 這是大前提
先整理 一 下我們目前想的思路， 先找最小的數字 假數 叫 a
並且 判斷 他的右邊的數字 足夠 選出剩下的數字， 是 就往右邊再找最小的數字
ex                                         否 你就必須 再 a 的左邊 找出一最小個數字 來湊 出足夠的數
1 5 3 6 8 7 8 2 9  3                         而這個是每一步都要做的判斷，例子
1   3 6   7   2 9
1   3 4   5   2 6 (順序)    這個例子 可以清楚的看到一個問題， 在第 6 個步驟 時有兩個數字可以選擇 8 與 9 很顯然 的 選擇 9
原因是 他位階比較低， 然後是 因為 2 的 原因。
同整一下 目前往右邊 看的情況 分成  右邊的數量 > 需要生產的數    解決
                                右邊的數量 == 需要生產的數   怎辦?
                                右邊的數量 < 需要生產的數    解決                
那剛好等於呢?
顯然的 是直接選 不用再比了

'''
def minv(start,end):    #索引值 start ~ end 尋找最小數字 並回傳該索引值 和 值
    minv = 10**9
    index = 0
    for i in range(start,end+1):
        if n[i] != 'x':
            if minv > int(n[i]):
                minv = int(n[i])
                index = i
    return index,minv

def right_interval(index):  #右邊 區間 還剩多少數字可選
    global length_d     #我們會需要 右邊到底
    c = 0
    for i in range(index,length_d):
        if n[i] != 'x':     #'x' 代表有選過 
            c += 1
    return c

def test_ans(length_d): #判斷 右邊 如果等於 需要的數 就不用再算下去了
    c = 0
    for i in range(length_d-1,-1,-1):
        if n[i] != 'x':
            c += 1
        else:
            if c == anumber - len(ans):
                return True
    return False

number = input()
d = int(input())
n = list(number)

ans = []
length_d = 0

for i in n:
    if i in '0123456789':
        length_d += 1       #計算長度 一般測資 用len()即可

anumber = length_d - d  #當前右邊 需要的數


index,v = minv(0,length_d -1) 
ans.append([index,v])   #我們把要加入的值 連同 索引值 加到串列裡，最後再靠排序 重現 題目所需的答案
n[index] = 'x'  #選過就給他個x
rightn = right_interval(index)  #右邊 區間 還剩多少數字可選(注意 會受到當前index影響)

a = rightn
start = 0
while len(ans) != anumber:
    if test_ans(length_d):  #測試 右邊的數量 == 需要生產的數
        for i in range(length_d-1,-1,-1):
            if n[i] != 'x':
                ans.append([i,n[i]])
                n[i] ='x'
                if len(ans) == anumber: #剛好 等於 跳開
                    break

    elif rightn > anumber-len(ans):     #右邊的數量 > 需要生產的數
        start = index + 1
        index,v = minv(index + 1,index+rightn)
        ans.append([index,v])
        n[index] = 'x'
        rightn = right_interval(index)
    else:
        index,v = minv(start,index - 1)     #右邊的數量 < 需要生產的數
        ans.append([index,v])
        n[index] = 'x'
        rightn = right_interval(index)
    
ans.sort()
ans1 = []

for i in ans:
    ans1.append(i[1])

while ans1[0] == 0:
    del ans1[0]
    if not ans1:
        break
    
if not ans1:
    print(0)
else:
    ans1 = list(map(str,ans1))
    print(''.join(ans1))



