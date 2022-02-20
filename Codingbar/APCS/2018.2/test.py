'''
7 1
2 4 1 3 7 6 9
0 1 2 3 4 5 6
m: 是索引值     1 ~ 5
'''
a = [2,4,1,3,7,6,9]
for i in range(1,6):
    m = i
    temp = 0
    for j in range(7):
        temp += a[j]*(j-m)
    print(m,temp)