def bs(f, target):
    global n
    if f == 1 or f == 2:
        a = matrix_x.copy()
    else:
        a = matrix_y.copy()
    print(a)
    i = 0
    j = n-1
    while i <= j:
        mid = (i + j) // 2
        if a[mid][0] == target:
            break
        elif a[mid][0] > target:
            j = mid - 1
        else:
            i = mid + 1

    return -1

n = int(input())

matrix_x = []
matrix_y = []
for i in range(n):
    x, y, t = map(int,input().split())
    matrix_x.append([y,x,t])
    matrix_y.append([x,y,t])
matrix_x.append([0,0])
matrix_y.append([0,0])
matrix_x.sort()
matrix_y.sort()
t = [matrix_x, matrix_y]
flag = 1    #1右 2左 3上 4下
xy = 0
cur = [0,0] 
ans = 0
flag_matrix = [[3,4,1,2],[4,3,2,1]]
'''
    1   2   3   4
0   3   4   1   2
1   4   3   2   1

'''
while True:
    if flag == 1:
        offset = 1
        target = cur[0]
        xy = 0
    elif flag  == 2:
        offset = -1
        target = cur[0]
        xy = 0
    elif flag == 3:
        offset = -1
        target = cur[1]
        xy = 1
    else:
        offset = 1
        target = cur[1]
        xy = 1
    print(flag, target, cur)
    c = bs(flag, target)
    print(c)
    if c == -1:
        break
    else:
        if target == t[xy][c+offset][0]:
            ans += 1
            cur = t[xy][c+offset][:]
            flag = flag_matrix[t[xy][c+offset][2]][flag]
        else:
            break
print(ans)