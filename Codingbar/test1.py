
t = []

for i in range(100):
    n = input()
    n = float(n)
    t.append(n)

test = []
s = -1
e = 0.1
for i in range(10):
    test.append([s,e])
    if i == 0:
        s = 0.1
        e = 0.2
    s = e
    e += 0.1
print(test)
t_sort = [0]*10
# for i in range(100):
    


