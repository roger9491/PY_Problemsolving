'''
窮舉法 但不能不簡化的直接用4層for，python不行(SE)，c卻可以..
所可以空間換時間，把 row,column 方向拆開來算，找出各個方向最成本最小位置

ex
5 2 0 2 2
0 2 0 2 0
1 0 0 3 0

row: [6,4,0,7,2] 本來的3個row 變成一行
column: [11,4,4] 本來的5個column縮成一行

'''
def midnumber(temp,length):     #temp:其中一個方向的串列 length:長度 
    total = 0   #總和
    minv = 10**9   #儲存最小成本
    for i in range(length):
        total = 0   #每次算完初始化
        for j in range(length): 
            total += temp[j]*(abs(i-j))     #固定好要算的位置 其他點要移到這個位置所需的成本加倒 total
        if minv > total:
            minv = total
            ans = i 
    return ans


while True:
    try:
        n = list(map(int,input().split()))

        total_x = [0]*n[1]      #row
        total_y = [0]*n[0]      #column

        matrix = []
        for i in range(n[0]):
            e = list(map(int,input().split()))
            matrix.append(e)
            for j in range(n[1]):
                total_y[i] += e[j]      #壓縮成一行
                total_x[j] += e[j]

        print(midnumber(total_y,n[0])+1,midnumber(total_x,n[1])+1)

    except:
        break
