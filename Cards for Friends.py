n = int(input())
for i in range(n):
    w,h,n = map(int,input().split())
    c = 1
    if w%2 != 0 and h%2 != 0:
        if n == 1:
            print('YES')
        else:
            print('NO')
    else:
        while c < n:
            if w % 2 == 0:
                w = w // 2
                c *= 2
            elif h % 2 == 0:
                h = h // 2
                c *= 2
            else:
                print('NO')
                break
        else:
            print('YES')
