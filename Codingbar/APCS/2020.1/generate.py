import random

a = []
b = []

for i in range(7):
    a.append(random.randint(1,300))
    b.append(str(random.randint(40,100)))
a.sort()
a = list(map(str,a))
print(7,a[-1])
print(" ".join(a))
print(" ".join(b))