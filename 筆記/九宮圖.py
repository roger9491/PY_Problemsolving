import itertools





def test(matrix):

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



a = int(input("請輸入幻方邊長:"))


#建立幻方內容
matrix = []
for i in range(a*a):
    matrix.append(i+1)

perm = list(itertools.permutations(matrix,a*a))
print("ok")


# 測試符合規定
for lst in perm:
    matrix = []
    index = 0
    for i in range(a):
        t = []
        for j in range(a):
            t.append(lst[index])
            index += 1
        matrix.append(t)
    # flag = test(matrix)
    # if flag:
    #     print(a)
    #     break
else:
    print("此邊長無幻方")