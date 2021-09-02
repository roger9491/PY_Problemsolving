n = int(input())
num = list(map(int,input().split()))

temp = []

 
ans = 0
for i in range(n*2):
    flag = 0
    index = 0
    # print("i",num[i])
    for j in range(len(temp)):
        # print("j",temp[j])
        if temp[j] > num[i]:
            ans += 1
        elif temp[j] == num[i]:
            flag += 1
            index = j
        # print(record)
    if flag:
        del temp[index]
    else:
        temp.append(num[i])


print(ans)