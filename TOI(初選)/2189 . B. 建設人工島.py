def dfs(i):
    global cost
    if i == target:
        break

    for i in range(t):




n = int(input())

t = []

for i in range(n-1):
    n1 = input().split()
    t.append(n1)


destence = []
for i in range(n):
    for j in range(i+1,n):
        target = j
        cost = 0