'''
(1)輸入n個數字，存進串列
(2)重複輸入一個數字,直到輸入0結束
    每輸入一個數字，串列所有數字+1，再把輸入的數字加進串列，並印出串列
ex 
input
5 1 4 5 2
1
7
3
2
0
output
[6, 2, 5, 6, 3, 1]
[7, 3, 6, 7, 4, 2, 7]
[8, 4, 7, 8, 5, 3, 8, 3]
[9, 5, 8, 9, 6, 4, 9, 4, 2]
'''

n = list(map(int, input().split()))

while True:
    num = int(input())
    if num == 0:
        break

    for i in range(len(n)):
        n[i] += 1
    n.append(num)
    print(n)