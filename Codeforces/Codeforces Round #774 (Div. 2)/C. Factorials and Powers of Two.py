t = int(input())

for i in range(t):
    n = int(input())
    target = int(n**(1/2)) + 1

    l = []
    temp = 1
    c = 1
    while temp <= n:
        l.append(temp)
        c += 1
        temp *= c
    
    temp = 2
    while temp <= n:
        l.append(temp)
        temp *= 2

    l.sort()
    