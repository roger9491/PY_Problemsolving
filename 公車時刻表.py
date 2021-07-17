n = int(input())
h,m = input().split()

time = []
for i in range(n):
    t = int(input())
    time.append(t)

p = input().split()

for i in p:
    h1 = int(h)
    m1 = int(m)
    for j in range(int(i)):
        m1 += time[j]
    h1 += (m1//60)
    h1 = h1%24
    m1 = m1%60
    h1 = str(h1).zfill(2)
    m1 = str(m1).zfill(2)
    print(h1+':'+str(m1))



'''
測資:
4
22 23
15
45
60
39
1 2 3 4
輸出:
22:38
23:23
00:23
01:02

'''