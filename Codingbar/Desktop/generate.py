import random

c = random.randint(1,5)
print(9,c)
t = []
for i in range(9):
    t.append(str(random.randint(1,100)))
print(" ".join(t))