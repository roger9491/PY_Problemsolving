'''
a = [0,1,2,3,4]  => 0 1 2 3 4


'''
'''
a = [0,1,2,3,4]
a = list(map(str,a))
s = ''
print("=".join(a))
'''
'''
e = list(map(int,input().split()))
new = []
for i in e:
    for j in new:   #檢查有沒有重複
        if j == i:
            break
    else:   #else:要執行的條件是 for迴圈執行完整才做 所以什麼時候不完整? break: 因為直接跳出for迴圈
        new.append(i)
print(new)
'''
'''
e = list(map(int,input().split()))
new = []
for i in e:
    flag = True
    for j in new:   #檢查有沒有重複
        if j == i:
            flag = False
    if flag:
        new.append(i)
            
print(new)
台大 清大 交大 成大 央大 師大 政大 台科
a = 10**9
b = 串列
for i in b:
    if a > i:
        a = i
'''
這個題目 你的解法的思想是什麼?
        大概的演算法?
        

c=int(input()) # 3!
b=1
e=0
for j in range(1,c+1,1):#1~3 1 2 3
    for i in range(1,j+1,1):#1 1~2 1~3
        b=i*b #b=1*1 2*1 1**2*3
    e+=b#1+2
    b=1
print(e)