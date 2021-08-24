
count = 0   #計算1有幾個
maxcount = 0 #儲存最多有幾個1

def dfs(row,column):
    global count #使用全域變數
    global maxcount #使用全域變數

    if row < 0 or column < 0 or row >= x or column >= x or recordmatrix[row][column] == True or matrix[row][column] != '1':
        return         #"超出方陣邊界" 或 "走過了" 或 "不是1" return 
    
    count += 1 #紀錄加1
    if count > maxcount:  #當前紀錄加完 跟之前的紀錄比較
        maxcount = count

    recordmatrix[row][column] = True #利用矩陣紀錄當前走過 
    dfs(row + 1,column)              #以下4行程式碼 表示當前共有4個方向會去試者走
    dfs(row,column+1)
    dfs(row-1,column)
    dfs(row,column-1)
    count -= 1                       # 走完要-1 表示紀錄退回去
    recordmatrix[row][column] = False  #當前走完 紀錄跟者初始化 下次從就能從另一個條路徑到達這個點
while True:
    try:
        count = 0
        maxcount = 0
        matrix = []
        x = int(input())
        for i in range(x):
            matrix.append(input())
        recordmatrix = [[False]*x for i in range(x)]
        dfs(0,0)    
        print(maxcount)
    except:
        break