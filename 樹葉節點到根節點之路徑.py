'''
使用dfs，碰到葉節點時，在Note裡存放屬於該節點的路徑。
我這邊使用鄰接表的方式儲存(應該是這樣吧?)

'''
Node = [[] for i in range(80)]             
Note = [[] for i in range(80)]
leaf = []

def dfs(root,path):
    if len(Node[root]) == 0:         #沒有子節點代表是葉節點
        leaf.append(root)            #儲存所有葉節點，因為題目說要按照大小印，當初我就因為這個一直沒過
        for i in range(len(path)-1,0,-1):     #利用Note儲存路徑，從尾巴開始放，這樣印出來就正的走(好像也沒必要?)
            Note[root].append(path[i])        
        return                             
    path.append(root)                 #不是葉節點就當作路徑儲存
    for i in range(0,len(Node[root])):          #那就按照該節點有的子節點搜尋所有路徑
        dfs(Node[root][i],path)
    del path[-1]                      #當搜過該節點的話要記得刪除

def clearchild():                    #初始化
    for i in range(80):
        Node[i].clear()
        Note[i].clear()
        leaf.clear()

while True:
    try:
        s = int(input())
        for i in range(s):
            path = []
            clearchild()
            ns = int(input())
            for i in range(ns):
                node = input().split(",")
                
                if node[1] == "99":               #當第二個數字是99 代表第一個數字是root
                    root = int(node[0])
                else:
                    Node[int(node[1])].append(int(node[0])) #儲存節點
            if ns == 1:           #有可能輸入一個邊  那就直接印出 %d:N
                print(node[0]+":N")
                print("")
            else:
                dfs(root,path)
                leaf.sort()        #題目要求按照大小順序印
                for i in range(0,len(leaf)):   
                    end = len(Note[leaf[i]])-1          #儲存該節點"最後一個"元素的索引直
                    if end + 1 == 0:
                        print(str(leaf[i])+":N")
                    else:
                        string = ""
                        string = string + str(leaf[i]) + ":{"
                        for x in range(0,end):
                            string = string + str(Note[leaf[i]][x])+","
                        string = string + str(Note[leaf[i]][-1])+"}"
                        print(string)
                print("")
    except:
        break