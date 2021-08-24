'''
                start
               |            |              |
               1            2              4
               |           |  |           |
          2    4   5      4    5         5  
        |      |    |    |      |       |  
    4  5 6   5 6    6   5 6      6      6
    m 取 n 個
從圖中可以看到，一開始先確定 在確定下一個數字，直到滿足 n 個，第 n 個是 去除之前確定所剩下的，
也就是說第 n 個並沒有只確定一個， 也就是這些數字是下一次還能選的，那程式遞迴到底之後會回去，在從剩下那些能選的集合中挑選
當作回去的那一層，以此類推。
所以我們可以用for迴圈來迭代能選的數字，那每一次迴圈都要遞迴，因為選過的是字不能再選，所以 參數要+1            

這題的思路就是先只固定一個，然後剩下的去做排列，先不管剩下的如何排列，先講為什麼只固定一個，因為不管剩下如何排列，只要固定的
那一個換，組合又變不一樣，那要注意的是剩下的排列不能選之前固定的，因為如果選到之前的，假設選到n，那就會跟之前固定n的組合重複到


'''
def combine(nums, k):   #num串列    k:取幾個
    res = []
    generateCombinations(nums, 0, [], k, res)
    return res

def generateCombinations(nums, start, c, k, res):
    if len(c) == k:     #長度為k時 加入 組合集   
        res.append(c[:])
        return
    for i in range(start, len(nums)):   #Start 開始 每經過一次遞迴就 +1 代表能選的也在變少
        c.append(nums[i])
        generateCombinations(nums, i+1, c, k, res)
        c.pop()
    return

a = [1,2,4,5,6]
res = combine(a,3)
print(res)