'''
題目說: "每一區公所均可連線到其他各區公所" "最低成本" "每一條網路線均為雙向傳送"
基本上就是樹 無向圖 ，又是最低成本，所以這題就是最小生成樹
最小生成樹 : 使用greedy思想去解，我們先找最小的的成本邊，然後再找第2小的，再找第三小的.....直到找到 頂點數-1，但要注意
每一次找的時候要確保 不能形成環，樹沒有環，那要怎麼解決?
我們可以用集合的性質來確保，如何做: 首先 找的邊 會有兩個頂點，我們把這兩個頂點當成是一個集合， 然後接下來找的邊 也會有兩個頂點
我們再把他 檢查這個兩個點 有沒有 "其中一個" 在原本的集合裡(就是剛剛第一次所創的)，如果有不就代表 你現在找的邊 和之前找的邊有
連起來(想一下圖)，好 所以剛說的是 "其中一個"，那如果兩個都有在原本的集合裡(必須是同一個集合才算)，我們就放棄這個邊，再者 
兩個點都沒有 在原本的集合裡，就新創一個集合"包含"這兩點，對 集合可能有多個，所以 之後的每一次"新邊"加進來時，都必須要通過
每一個 原本就在的集合的檢驗才行。1."其中一個" 2."兩點同時在同集合" 3."以上都沒有" (檢驗順序想想看)
這邊說明一下 2. 的原理 
首先一個集合 裡有兩個點 所代表的意義 第一個可能:這兩個點就是形成一個邊
                                  第二個可能:有兩條 "邊" 連在一起 剛好組成一個集合，這兩個點就是 就是沒有相連的 兩端點

畫個圖就知道了， 所以這時候 當你把 重複把這兩個點 加入到一個集合時發生什麼事， 第一個:重複加入同一邊(所以基本不可能，題目說雙向)
                                                                        第二個:就會形成一個環
'''
def kruskal(graph,tree,length):  #graph 兩個點 成本  tree:找到的邊放在這  length:要找幾個邊
    set_list = []   #要維護的 集合 串列
    total = 0       #成本
    sorted(graph)   #先按照成本排序邊，greedy
    while len(tree) != length-1:    #要有 頂點數 - 1 個邊
        if search1(set_list,graph[0][0],graph[0][1]):   # 檢查 要加入的兩個點 有沒有  在同一個集合裡
            del graph[0]
            continue
        total += graph[0][2]        #成本加入
        tree.append([graph[0][0],graph[0][1]])  #邊
        if search2(set_list,graph[0][0],graph[0][1]):   #檢查是不是其中一個點在集合裡
            addset(set_list,graph[0][0],graph[0][1])    #加入集合
        else:
            set_list.append({graph[0][0],graph[0][1]})  #都沒有 就直接建立新集合
        del graph[0]        #記得檢查完 加完的邊要刪掉
    return total
        
def sorted(graph):
    for i in range(len(graph)-1):   #泡沫排序
        for j in range(len(graph)-1):
            if graph[j][2] > graph[j+1][2]:
                temp = graph[j]
                graph[j] = graph[j+1]
                graph[j+1] = temp

def search1(set_list,node1,node2):  #檢驗要加入的兩端點有沒有在同一個集合裡，造成循環
    for i in set_list:
        if node1 in i and node2 in i:
            return True

def search2(set_list,node1,node2):  #檢驗使否需要聯集
    for i in set_list:
        if node1 in i or node2 in i:
            return True

def addset(set_list,node1,node2):
    for i in range(len(set_list)):      #先選一個有關連的集合
        if node1 in set_list[i] or node2 in set_list[i]:
            set_list[i].add(node1)
            set_list[i].add(node2)
            temp = i
            break
    for i in range(len(set_list)):  #這裡加入集合的方式是先找到一個關聯的集合加入 ，這裡再做檢查有沒有需要聯集
        if i != temp:
            for j in set_list[i]:
                if j in set_list[temp]:
                    set_list[temp] = set_list[temp] | set_list[i]
                    del set_list[i]
                    return

while True:
    try:
        nm = list(map(int,input().split()))

        graph = []
        for i in range(nm[1]):
            e = input().split()
            e[2] = int(e[2])
            graph.append(e)

        node = []   #題目關係 要自己求出頂點數
        for i in graph:
            if i[0] not in node:
                node.append(i[0])
            if i[1] not in node:
                node.append(i[1])

        tree = []
        total = kruskal(graph,tree,len(node))
        string = ""     #輸出要按照題目格式
        for i in range(len(tree)-1):    #邊要按照字典排序
            for j in range(len(tree)-1):
                if len(tree[j][0]) == 3:
                    temp1 = 10
                else:
                    temp1 = int(tree[j][0][1])
                if len(tree[j+1][0]) == 3:
                    temp2 = 10
                else:
                    temp2 = int(tree[j+1][0][1])
                if temp1 > temp2:
                    temp = tree[j]
                    tree[j] = tree[j+1]
                    tree[j+1] = temp
                elif temp1 == temp2:    #當第一 個點一樣就要檢查第二個點
                    if len(tree[j][1]) == 3:
                        temp1 = 10
                    else:
                        temp1 = int(tree[j][1][1])
                    if len(tree[j+1][1]) == 3:
                        temp2 = 10
                    else:
                        temp2 = int(tree[j+1][1][1])
                    if temp1 > temp2:
                        temp = tree[j]
                        tree[j] = tree[j+1]
                        tree[j+1] = temp

        for i in range(len(tree)):
            if i == len(tree)-1:
                string += '('+tree[i][0]+" "+tree[i][1]+')'
            else:
                string += '('+tree[i][0]+" "+tree[i][1]+') '
        print(string)
        print(total)
    except:
        break