N = int(input())
x1, y1, x2, y2 = map(int,input().split())

#d = [abs(x1-n),abs(x2-n),abs(y1-n),abs(y2-n)]
#N = max(d)+1

matrix = []
for row in range(N,0,-1):
    now = []
    for column in range(N,row-1,-1):
        now.append(column)
    for i in range(2*row-2):
        now.append(column)
    for j in range(N-row):
        column = column+1
        now.append(column)
    matrix.append(now)
another = matrix.copy()
del another[-1]
another.reverse()
matrix += another

if x1 < x2 and y1 > y2:
    x1, y2, x2, y1 = y2, x2, y1, x1

total = 0
for i in range(x1-1,x2):
    for j in range(y1-1,y2):
        total += matrix[j][i]
print(total)