'''
3 4 5
500 400 800 200
500 400 100 600
450 420 800 790

#方案
0 0 0
城0 城1 城2 城3
伺0     
伺1   
伺2

0 1 2
城0 城1 城2 城3
伺0     
    伺1   
        伺2

0 2 2
城0 城1 城2 城3
伺0     
        伺1   
        伺2
2 1 2
城0 城1 城2 城3
        伺0     
    伺1   
        伺2
500 400 800 200
500 400 100 600
450 420 800 790
1 1 1
城0 城1 城2 城3
    伺0     
    伺1   
    伺2
'''

n,m,k = map(int,input().split())

q = []
for i in range(n):
    a = list(map(int,input().split()))
    q.append(a)

c = []
for i in range(k):
    a = list(map(int,input().split()))
    c.append(a)

minv = 10**9
for x in c:     #x代表 伺服器所在位置
    total = 0
    traffic = [[0]*m for i in range(m)]
    for i in range(n):
        for j in range(m):
            traffic[x[i]][j] += q[i][j]
    # print(x)
    # print(traffic)
    for i in range(m):  #伺
        for j in range(m):  #城市
            if i == j:   #x[i] 伺服器所在城市
                total += traffic[i][j]
            else:
                if traffic[i][j] > 1000:
                    total += (traffic[i][j] - 1000)*2
                    total += 1000*3
                else:
                    total += traffic[i][j]*3
    # print(total)
    if total < minv:
        minv = total
print(minv)
