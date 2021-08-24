n = int(input())
stone = list(map(int,input().split()))
stone.sort()
stone2 = []
while stone:
    if len(stone) >= 2:
        stone2.append(stone[-1])
        stone2.append(stone[0])
        del stone[0]
        del stone[-1]
    else:
        stone2.append(stone[0])
        del stone[0]
heigh = 0
total = 0
for i in stone2:
    total += (i - heigh)**2
    heigh = i
print(total)
