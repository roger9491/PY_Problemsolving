'''
Petya是一個農夫，他有一排 n 塊的田地，每一個田地都有不同的高度，若
站在比較高的田地澆水，水自然會往比較低的田地流，這樣別的田地也能澆到水，但是
水在流的過程中可能會遇到高的田地，這樣水就被擋住了，試問站在一處澆水，最多能
澆到幾塊田地?

輸入:
第一行: 輸入一個整數 代表有多少塊田地
第二行: 輸入n個整數 代表每一個田地的高度
輸出:
印出一個數字，代表 最多有多少塊田地可以澆到水

'''
n = int(input())

t = list(map(int, input().split()))

length = n
maxv = 0
temp = 0
for i in range(length):
    temp = 0
    temp1 = t[i]
    for j in range(i,-1,-1):
        if temp1 >= t[j]:
            temp += 1
            temp1 = t[j]
        else:
            break
    temp1 = t[i]
    for j in range(i+1,length):
        if temp1 >= t[j]:
            temp += 1
            temp1 = t[j]
        else:
            break
    if temp > maxv:
        maxv = temp
    # print(i,temp)
print(maxv)


