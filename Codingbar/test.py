# 印出 1 ~ 999

# 所有 3位數 每一位數都不能一樣 並且是偶數


for i in range(1,999):
    i1 = str(i)
    if len(i1) < 3:
        i1 = "0" + i1
    i2 = set(i1)
    if len(i2) == 3 and i % 2 != 0 :
        print(i1)