t = int(input())
for i in range(t):
    a,b,n = map(int,input().split())
    a_list = list(map(int,input().split()))
    b_list = list(map(int,input().split()))
    t = []

    for i in range(n):
        t.append([a_list[i],b_list[i]])

    t.sort()
    index = 0
    while b > 0:
        for i in range(n):
            if b > 0 and t[i][1] > 0:
                b -= t[i][0]
                t[i][1] -= a
                break
        else:
            break
    for i in range(n):
        if t[i][1] > 0:
            print('NO')
            break
    else:
        print('YES')