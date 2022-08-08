def print_fmt(matrix, n):
    for i in range(n):
        for j in range(n):
            print(f'{matrix[i][j]:{" "}<{4}}',end="")
        print()


def test(matrix, a):

    #row
    for i in range(a):
        if i == 0:
            count = sum(matrix[i])
        else:
            if count == sum(matrix[i]):
                count = sum(matrix[i])
            else:
                return False

    #column
    for i in range(a):
        tmp = 0
        for j in range(a):
            tmp += matrix[j][i]
        if tmp == count:
            count = tmp
        else:
            return False
    
    #diagonal
    tmp = 0
    for i in range(a):
        tmp += matrix[i][i]
    
    if tmp == count:
        count = tmp
    else:
        return False
    
    tmp = 0
    for i in range(a):
        tmp += matrix[i][a-i-1]
    if tmp == count:
        count = tmp
    else:
        return False
   
    return True


n = int(input("輸入 n , 構造n階幻方 :"))

if n % 2 != 0:
    print("輸入為奇數階幻方，採用 Siamese方法 構造幻方")

    #建立方陣
    matrix = [[0]*n for i in range(n)]

    print("初始方陣:")
    print_fmt(matrix, n)

    #起始
    y, x = 0, n // 2
    number = 1
    while number <= n*n:
        # 填入數字
        matrix[y][x] = number

        # 遞增數字
        number += 1

        # 暫存 y, x
        tmpy, tmpx = y, x
        # 計算下一個位置
        y, x = ((y-1 + n) % n), ((x+1)%n)

        # 判斷接下來填的位置是否有數字
        # 有的話就填入當前位置下方
        if matrix[y][x] != 0:
            y, x = (tmpy+1)%n, tmpx
else:
    if n % 4 == 0:
        print("輸入為4M階幻方，採用 4M階幻方構造法 構造幻方")

        #初始化方陣
        matrix = []
        number = 1
        for i in range(n):
            t = []
            for i in range(n):
                t.append(number)
                number += 1
            matrix.append(t)

        print("初始方陣:")
        print_fmt(matrix, n)

        #初始化四頂點
        y1, x1 = 0, 0
        y2, x2 = 0, 3
        y3, x3 = 3, 0
        y4, x4 = 3, 3

        for i in range(n):
            for j in range(i+1, n):
                if ( i == j ) and (i+j) == (n-1):
                    continue
                if (i%4 == 0 or i%4 == 3) and (j%4 == 0 or j%4 == 3):
                    continue
                if (i%4 == 1 or i % 4 == 2) and (j%4 == 1 or j%4 ==2):
                    continue
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = tmp



# for i in range(n):
#     print(matrix[i])
print(n,"幻方:")
print_fmt(matrix, n)

print()
# 驗證幻方正確性
if test(matrix, n):
    print("演算法正確")
else:
    print("演算法不正確")