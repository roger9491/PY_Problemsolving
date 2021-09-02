n = int(input())

for i in range(n):
    a = int(input())

    m = list(map(int,input().split(" ")))

    ans = 0

    flag = True
    for x in range(a+1):
        flag = True
        for y in range(a-1):
            if m[y] > m[y+1]:
                flag = False
                index = y
                break
        # print(x,index,m)
        for y in range(index,a-1,2):
            if m[y] > m[y+1]:
                m[y],m[y+1] = m[y+1],m[y]
                
        if flag:
            break

    if x == 0:
        print(0)
    else:
        print(x) 
