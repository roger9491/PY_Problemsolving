a = [1,10.24,5,'ji3']   #串列   索引值 為什麼要有索引值:因為要有順序 為什麼要有順序? 
b =[ ]                  #a[索引值] :位置
c = []
s =""   #文字型態 空字串 1
a[0] = 2 #一個位置 就是者能放一個值
# 變數 
print(a[0])
print(a[1])
print(a[2])
print(a[3])

print("進入for")
b = [0,1,2,3]
for i in b:     #for i in :固定的格式 why? 因為她至始至終都只做同樣一件事 ? 迭代: 按照順序把資料帶出來
    print(i)  #會執行幾次? why 4 次? 因為a有 4 個資料                    1 10.24 5 'ji3'
    a[i] = 5
print(a)
a[0] = 5
a[1] = 5
a[2] = 5
a[3] = 5
a = [5,5,5,5]
print(a[0])
a[]
print(a)
#串列的長度     電腦的數字都是從0開始
for i in range(4): #range:產生數列 n筆數字      
    print(a[i])         

#range() 什麼是函式 ? 餵給他某個值 會產生出東西 值:參數 
#range(y) y:末項 
#range(x,y) x:首項  y:末項 
#range(x,y,-1)


'''
1 2 3 4 5 6 7 8 9 10
0 1 2 3 4 5 6 7 8 9
'''

'''for i in range():
for i in a: #a:串列
for i in s: #s: 文字型態
串列可以儲存多種資料
你要怎麼儲存?
''' 
#n = input() #文字型態
#n = int(input())
a = [] #建立串列 給予空串列
#a.append(n)  加入de


a = [1,2,3,4,5,7] #len(): 計算長度 串列,字串
b = []
c = len(a) - 1    #c: a的最後一個位置的索引值 
for i in range(c,-1,-1) 5 4 3 2
b.append(a)
print(b) 








for i in range(5):
    print("1")


