'''
這題是NP 完全問題，也就是求一個圖裡最大完全子圖的問題，首先了解什麼是完全圖，完全圖就是 每'任意' 兩點都有一個邊直接相連，
換句話說就是 (有一個點 可以連到這張圖所有的點(一定有一條邊存在)) 對於這張圖每一個點都符合這種性質，給一個例子 v = [1,2,3]
e = [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)] 當然無向圖可以在作化簡
你可以看到 3個點的完全圖 每一個點 degree 都是 2， 如果再試多一點例子，你會發現 4個點的完全圖 每一點的degree都是3
5 點完全圖，degree = 4 .....
所以如果了解這個特性，這題就很簡單了，你只要先找出最大degree 然後把所有符合這個degree的點都拿出來，去測有沒有剛好 degree+1個
點都有邊相連，有的話degree+1就是答案 ，沒有的話 degree-1 往下尋找，以此類推。所以本質就只是窮舉法，只是利用到圖的概念。
再來要考慮的是，你找的 同個degree的點 數量可能會大於 degree+1，所以你就要先列出所有組合(長度為degree+1)，然後再去測，
那如何找出，所有組合就用dfs~~

            m 個數 取 n個組合 以下為[1,2,4,5,6] 取 3個例子
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

思路就是先只固定一個，然後剩下的去做排列，先不管剩下的如何排列，先講為什麼只固定一個，因為不管剩下如何排列，只要固定的
那一個換，組合又變不一樣，那要注意的是剩下的排列不能選之前固定的，因為如果選到之前的，假設選到n，那就會跟之前固定n的組合重複到


'''
def generateCombinations(nums, start, k):   #nums:串列 start:開始位置 c:當前組合 k:指定組合長度 
    if len(c) == k:     #長度為k時 加入 組合集   
        res.append(c[:])
        return
    for i in range(start, len(nums)):   #Start 開始 每經過一次遞迴就 +1 代表能選的也在變少
        c.append(nums[i])
        generateCombinations(nums, i+1, k)  #下一層的起始位置要比上一層還要多1 這樣能確保必定不會重複
        del c[-1]                       #搜尋完就把沒有固定好的點 刪掉
    return res

def max_clique(maxd):
    for degree in range(maxd,0,-1):     #從最大degree開始尋找，往下
        temp = []                       #存放 大於等於 degree的度數 ，為什麼是大於等於 因為有些點可能會多連其他點，並不影響完全圖
        for i in node_list:
            if node_degree[i] >=  degree:
                temp.append(i)  # 大於 該度數 的節點串列
        tempset = generateCombinations(temp, 0, degree+1)     # set 集合了當前 大於等於degree的節點的所有組合
        for i in tempset:           #去試每一種組合
            flag = False
            for x in i:
                for y in i:
                    if edges_matrix[x][y] == 0 and x != y:  #判斷 點有沒有相連，然後要避免 xy相等
                        flag = True
                        break
                if flag:    #只要有一個邊相連 就不用判斷了
                    break
            else:
                return degree+1
                    
nodes = list(map(int,input().split(" ")))
edges_matrix = [[0]*(nodes[0]+1) for i in range(nodes[0]+1)]

for i in range(nodes[1]):
    e = list(map(int,input().split()))
    edges_matrix[e[0]][e[1]] = 1
    edges_matrix[e[1]][e[0]] = 1

node_list = []  #頂點集合
for i in range(1,nodes[0]+1):
    node_list.append(i)

maxd = 0
node_degree = {}    #每個節點的degree
for i in node_list:
    node_degree[i] = 0

for i in node_list:     #注意:如果以後再使用字典那幾行，測資出現RE代表，字典沒有值，先宣告省事點。
    for j in node_list:
        if edges_matrix[i][j] == 1:
            node_degree[i] += 1
        
    if maxd < node_degree[i]:   
        maxd = node_degree[i]

c = []  #當前組合    
res = []    #不同組合的集合
ans = max_clique(maxd)

if ans:
    print(ans)
else:      
    print(1)
