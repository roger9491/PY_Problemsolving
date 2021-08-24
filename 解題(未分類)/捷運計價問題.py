'''
這題牽扯到圖 也就是捷運路線，然後題目要求最便宜的收費，
1. 基本票價
2.每三站加5元 ///////////////所以你必須記錄有幾站，而且必須考慮經過最少站
3.轉乘不同路線要"再"加5元 ////這題麻煩的地方，你在求經經過最少站的同時必須要考慮轉站，也就是 你會有種情況面臨 站數vs轉站，
所以不是越少站越好~

所以我們得路線實際上是有選擇的，也就是加權，所以在網路上搜尋 最短路徑+加權 應該會搜到 Dijkstra演算法
實際上還有其他演算法，但這個我認為比較直觀，比較貪心~~
怎麼的貪心法?
Dijkstra演算法:   (目標)尋找 起點 到所有點的最短路徑 ，可以解決有向圖，無向圖，但有加權路線的圖。
1.首先 路 會有 有訪問 和 沒訪問過的，所以你必須有兩個串列存放這些東西，我們 S:訪問過  U:沒訪問過
，那剛開始 S 只有起點 ，U 有所有點(除了起點)。
2.然後 先從 鄰近 S裡的 開始找"鄰近"的節點，並且選最短的路(這裡把加權最少當最短)，選重之後，(我們先稱這個點為 e)
加入 S 
U 刪掉
3.然後你必須要''更新'' ，加入 e 之後，檢查起點跟"各個"點的距離有沒有改變(因為這是我們的目標)，什麼意思?
當 e 加進來之後，有沒有點 是只要經過 e 反而路徑會變短(因為我們路徑都有所謂的值)，如果有 我們的路徑就改成
起點 -> e -> 該點，也就是 原本 起點到改點的距離 改成 起點到e再到該點的距離，符號化~~ 
    dis[i] = min(dis[i],dis[minv] + edge_martrix[minv][i])
說明: dis[i] 為存放起點到 i 點的距離 
     edge_martrix[minv][i] 為存放 minv 到 i 點的距離

所以理論你 3. 更新完 理論上"當下"最短的路徑就出來了，因為你會每個點都去檢查，貪心吧~
所以做這題前提目標是dp 熟應該就行了~~(轉站所累積的價格都跟前進到下一站有關)

所以你反覆去做 2. 3.  當 U 沒了程式就結束了~~

回到這題，你必須去修改一些東西 ，
紀錄 經過的點
轉站 + 5 元

'''
class price:                         #因為每個點都要記錄 
    def __init__(self,vertex,price):
        self.vertex = vertex        #經過的點數  拿來計算每三站要+5元
        self.price = price          #轉站的價格

def shortest_path(start,end):
    minv = start
    for i in vertex:
        if edge_matrix[visted[-1]][i] != 500:
            dis[i] = 1                         #初始化起點 鄰近的點的距離
            vertex_price[i].vertex = vertex_price[i].vertex + 1  #代表路徑有1了 因為是從起點 到 該節點
            if minv//100 != i // 100:                            #一樣要注意轉站的部分
                vertex_price[i].price = vertex_price[i].price + 5 

    while vertex:
        minv = start        #為了保持每一次minv都會被換
        for i in vertex:    #尋找鄰近 最短的點
            if dis[minv] > dis[i]:
                minv  = i
    
        visted.append(minv)     #選中 加入 訪問
        vertex.remove(minv)     #刪除 未訪問
   
        for i in vertex:        #更新 最短路徑
            if dis[i] < dis[minv] + edge_matrix[minv][i]:   #用 if  else 代替 min
                dis[i] = dis[i]
            else:
                dis[i] = dis[minv] + edge_matrix[minv][i]   #更新路徑
                vertex_price[i].vertex = vertex_price[minv].vertex + 1  #如果有更新代表 該節點(i) 與 起點 中間插入了一個節點(minv)              
                if i//100 != minv//100:                                 #那如果有加入中間節點 代表可能涉及轉站問題
                    vertex_price[i].price = vertex_price[minv].price + 5                  
                else:
                    vertex_price[i].price = vertex_price[minv].price
    vertex_price[end].price = vertex_price[end].price + vertex_price[end].vertex // 3 * 5 + 10    #依照題目算出價格
    return vertex_price[end].price

while True:
    try:
        vertex = []     #未訪問頂點集合
        visted = []     #訪問頂點集合
        maxv = 500      #隨便設一個大數 當作是 點 與 點 沒有連通的表示
        dis = {}        #依照題目輸入的格式，轉換成數字，因為要使用串列，使用dict可以動態儲存
        vertex_price = []       #每一點都有專屬的 路徑數  價格
        for i in range(500):    #初始化
            a = price(0,0)
            vertex_price.append(a)

        n = int(input())

        node_number = {}        #輸入的第一個轉換成英文 對應 的數字
        edge_matrix = [[maxv]*501 for i in range(501)]  #初始化 矩陣(路徑)
        num = 0                 # 我的想法是 英文代表 百位數字  + 數字 = 站點代表的索引值
        for i in range(n):
            edge = input().split(" ")
            if  edge[0][0] not in node_number:      #key唯一
                node_number[edge[0][0]] = num*100
                a = node_number[edge[0][0]] + int(edge[0][1:]) #[1:] 因為有可能數字 1 ~ 100
                num += 1
            else:
                a = node_number[edge[0][0]] + int(edge[0][1:])

            if edge[1][0] not in node_number:
                node_number[edge[1][0]] = num*100
                b = node_number[edge[1][0]] + int(edge[1][1:])
                num += 1
            else:
                b = node_number[edge[1][0]] + int(edge[1][1:])
            
            if a//100 == b//100:        #這邊我們要把轉站的路程的加權考慮進去
                edge_matrix[a][b] = 1   #轉站是另外加錢
                edge_matrix[b][a] = 1
            else:
                edge_matrix[a][b] = 5
                edge_matrix[b][a] = 5

            if a not in vertex:       #頂點集合
                vertex.append(a)
            if b not in vertex:
                vertex.append(b)

        for i in vertex:
            dis[i] = maxv   #初始化距離

        search = input().split(" ")
        start = node_number[search[0][0]] + int(search[0][1:])      #起點
        vertex.remove(start)    
        visted.append(start)    
        end = node_number[search[1][0]] + int(search[1][1:])        #目標點
        print(shortest_path(start,end))
        
    except:
        break