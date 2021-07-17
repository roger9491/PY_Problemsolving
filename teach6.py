'''
解題想法
    先重複輸入
    判斷 是不是no
    先檢查 輸入的有沒有匹配
    沒有的話才加入

演算法
重複 
   輸入
   判斷書入 是不是 no 是的話 就跳出 重複
   建立個變數 給他一個初始直
   for i in range(len()):
       判斷有沒有相等 第二個數字
        變數 設給他一個 a
        印出
        刪除
        break
    if 變數 != 'a':
        加入串列
    
串列裡的印出
for 

         字串得
else:
  '''   
n = 5
a = []
for i in range(n):
    a.append(i)
t = []
for i in range(n):
    t.append(a)

for i in range(n):
    print(t[i])
print(t[0][1])

t = [[0]*n for i in range(7)]
print(t)