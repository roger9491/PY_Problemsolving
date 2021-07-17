t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    total = 0
    flag = 1
    while a:
        temp = a[:]
        for i in temp:
            total += i
            del a[0]
            if flag:
                if i % x != 0 or i == 0:
                    flag = 0
                else:
                    for y in range(x):
                        a.append(i//x)
        
    print(total)            