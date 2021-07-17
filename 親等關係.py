'''
做法很多種，可以當成圖用dfs圖搜，但有點麻煩，所以可以用父子關係來解，因為輸入始終只有一位父親，所以
我只要知道目標的所有祖先，然後比對哪一個祖先一樣，這樣兩者只要算出與該祖先的長度在相加就算出來了~~
'''
while True:
    try:
        tree = []       #儲存父與他的子節點關係
        path1 = []      #第一個目標  及  他的祖先都在這
        path2 = []      #同上

        ns = int(input())
        for i in range(ns):
            node = input().split(" ")
            tree.append(node)
        search = input().split(" ")  #目標
        a = search[0]       #目標一 因為等等會被他的祖先們替換 所以用變數
        path1.append(a)
        b = search[1]       #目標2
        path2.append(b)

        for i in range(ns):     #至多找ns次
            for i in range(ns):     #如何找到祖先們? 先把父親找出來，再去找父親的父親，然後再用父親的父親，去找父親的父親的父親.....(我是廢話)
                if a in tree[i]:    #判斷當前a的父親是誰
                    if tree[i][0] not in path1:     #有可能找到所有祖先了，但迴圈還在進行，確保不重複
                        path1.append(tree[i][0])    #加入祖先的行列
                        a = tree[i][0]              #a替換成父親，去找他的父親的父親
                        break
            for i in range(ns):     #同上
                if b in tree[i]:
                    if tree[i][0] not in path2:
                        path2.append(tree[i][0])
                        b = tree[i][0]
                        break
        if len(path1) == 1:                 #有可能剛好是根結點
            same = path1[0]
        else:
            for i in range(1,len(path1)):
                if path1[i] in path2:
                    same = path1[i]
                    break
    
        print(path1.index(same)+path2.index(same))
    except:
        break