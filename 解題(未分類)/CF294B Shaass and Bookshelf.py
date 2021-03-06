'''
題意:
    坦白說題意就是跟你說 有一些書，要你在 ，要你在 row的長度最小的情況下擺滿書，擺法就是把書立起來放，
    然後在立起來的書上能 水平擺書，但是不能超過 row
    ____
   |||||| :這樣放，所以每一本書 都有厚度也就是 row1[i]:第i本的厚度 ， 那放在上面的書(也就是水平放的書) 寬度為 row2[i]:第i本的寬度
   ，所以 求 立著的書的厚度總和盡量最小(水平的書不能疊，只能放一本)~

題解:
    我們 目標就是 在每一個 厚度的區間，盡量把寬的書用掉，這樣就不會放在上層造成浪費(因為上層水平的書的寬度總和必須小於立著的書的厚度總和)
    所以 我們就在 每一個厚度裡找出，用掉的最大寬度，
    ex     5               立著的書        水平的書
    (1)    1 12            1 12            1 3
    (2)    1 3             2 15            2 1
    (3)    2 15            2 5             水平寬度 4
    (4)    2 5             厚度為5
    (5)    2 1             厚度 >= 水平 正確

        所以 每一次增加一本書的時候，都要跟前面的放得書做比較，找出用掉最多寬度的書 
    比較表:
        厚度: 1     2       3       4       5       6       7       8
    書
    (1)      12    x       x        x       x       x       x       x
    (2)      12    15      x        x       x       x       x       x
    (3)      12    15      27       30      x       x       x       x
    (4)      12    15      27       30      32      35      x       x 
    (5)      12    15      27       30      32      35      33      36

    這時候我們就能找出 最小厚度 剛好放完書本
    還有一點要提醒，雖然 看起來是01背包，但今天你必須是恰好裝滿的01背包， 你的厚度不夠怎麼可以代表該厚度的最大寬度呢?
    (想要有點感覺的話，就寫個對拍程式，去看哪個範例會錯~~)

狀態轉移
    if t[i][0] <= j:
        matrix[i][j] = max(matrix[i-1][j],matrix[i-1][j-t[i][0]] + t[i][1])
    else:
        matrix[i][j] = matrix[i-1][j]
    

'''
n = int(input())    #n本書

t = []
for i in range(n):
    e = list(map(int,input().split()))
    t.append(e)         #t[i][0]:第i本書的厚度   t[i][1]:第i本書的寬度

size = 0
size2 = 0
for i in t:
    size += i[0]        #算出總厚度
    size2 += i[1]       #算出總寬度

matrix = [[-1000]*(size+1) for i in range(n)]

for i in range(n):
    matrix[i][0] = 0

for i in range(n):
    for j in range(1,size+1):
        if t[i][0] <= j:
            matrix[i][j] = max(matrix[i-1][j],matrix[i-1][j-t[i][0]] + t[i][1])
        else:
            matrix[i][j] = matrix[i-1][j]

for i in range(1,size+1):
    if i >= size2 - matrix[-1][i]:      #看看哪個厚度 剛好大於等於 剩下的寬度
        print(i) 
        break