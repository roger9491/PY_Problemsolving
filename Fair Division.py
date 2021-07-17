n = int(input())
for i in range(n):
    count = int(input())
    cands = list(map(int,input().split()))
    c1 = []
    c2 = []
    for i in cands:
        if i == 1:
            c1.append(1)
        elif i == 2:
            c2.append(2)
    c1 = len(c1)
    c2 = len(c2)

    if c2%2 == 0 and c1%2 == 0:
        print('YES')
    else:
        if c1 % 2 != 0 or c1 == 0:
            print('NO')
        else:
            print('YES')