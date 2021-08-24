'''
輸入n個數字
再輸入一個a數字
檢查輸入n個數字裡有沒有小於a的，刪掉
檢查完印出串列(大到小) 可以用 串列.sort(reverse=True)
input
2 4 3 5 4 3 5
3
output
[5, 5, 4, 4, 3, 3]
'''

n = list(map(int, input().split()))
num = int(input())

a = []
for i in range(len(n)):
    if n[i] >= num:
        a.append(n[i])
a.sort(reverse=True)
print(a)
        