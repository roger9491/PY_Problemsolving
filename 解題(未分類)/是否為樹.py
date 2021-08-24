''' 樹的性質
1.連通圖
2.頂點數-1 == 邊數
3.不能有cycle

如果 2.和3.正確，1.必正確，因為在無向圖裡 頂點數-1 == 邊數 只會有兩種情況 有cycle的圖和tree (沒有連自己情況)
,我們只要再確保3.就必是tree。
2.很好解決，重點是3.
解法: 我們知道一個cycle的頂點 度數(頂點有幾條邊連)是必定都是2 也就是說他們度數必是同時相同，根據這個道理
我們可以對圖的度數進行刪減，而我們只對度數為1的點進行刪減，也就是如果刪到只剩cycle必定刪不掉，
也就是剩下cycle頂點同時為2刪不掉和 度數為0的頂點。
'''
def vertexdegree(matrix,vertries):                                                      
    vertex_degree = {}                                                                  
    for i in vertries:         #列出所有頂點對頂點的組合，找出該度數                                                         
        degree = 0                                                                     
        for j in vertries:                                                             
            if  matrix[i][j] == True:    #鄰接矩陣來判斷有沒有邊相連                                  
                degree = degree + 1      #度數+1
        vertex_degree[i] = degree
    return vertex_degree

def checkconnected(vertex_degree,matrix,vertries):
    while 1 in vertexdegree(matrix,vertries).values(): #3. 目標 度數只刪一 ，所以 刪完所有度數為1的
        a = []                                          #  我們要先找到所有度數為1的儲存起來  
        vertex_degree = vertexdegree(matrix,vertries)                                  
        for key in vertex_degree:               
            if vertex_degree[key] == 1:
                a.append(key)
        for i in a:                                     #刪掉度數為1的
            for j in vertries:
                matrix[i][j] = False
                matrix[j][i] = False
        if 1 not in vertexdegree(matrix,vertries).values():   #刪完之後馬上先判斷1不在 度數的串列裡，
            for i in vertexdegree(matrix,vertries).values():  
                if i > 1:                                     #再判斷 有沒有大於一以上的度數，如果有的話代表只剩 
                    return False                            #只剩度數大於1 和 度數0，那必定cycle
    return True    
                                                   
def vertex(edges):       #頂點用串列儲存起來
    vertries = []
    for i in edges:
        if int(i[0]) not in vertries:     
            vertries.append(int(i[0]))
        if int(i[1]) not in vertries:
            vertries.append(int(i[1]))
    return vertries

while True:
    try:
        n = int(input())
        for i in range(n):
            edges = []
            in_edges = input().split()
            for i in in_edges:
                a = i.split(",")   #去掉逗號
                edges.append(a)
            
            vertries = vertex(edges)  #頂點集合   
            max_vertex = max(vertries) #找出最大頂點
            matrix = [[False]*(max_vertex+1) for i in range(max_vertex+1)] #使用最大頂點建立陣列
            for i in edges:  
                matrix[int(i[0])][int(i[1])] = True     #利用鄰接矩陣儲存邊，因為是無向圖，所以另外一個方向也要
                matrix[int(i[1])][int(i[0])] = True

            checkedges = 0          #當初測試時，一直不過，因為當初想說是無向圖，應該不會重複輸入邊把?
            for i in vertries:          #後來測試會輸入重複得邊所以,必須知道有多少個邊，不然測試 2. 時會錯掉
                for j in vertries:
                    if matrix[i][j] == True:
                        checkedges = checkedges + 1
            
            vertex_degree = vertexdegree(matrix,vertries) #會傳出一個 dict型態的 頂點:度數
    
            if checkconnected(vertex_degree,matrix,vertries) and len(vertries) - 1 == checkedges / 2: #2. 3. 必須要同時符合]
                print("T")
            else:
                print("F")
              
    except:
        break