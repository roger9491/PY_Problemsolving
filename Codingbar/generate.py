import random

print(7,5,10)
for i in range(7):
    temp = []
    for j in range(5):
        temp.append(str(random.randint(1,30)))
    print(" ".join(temp))
temp = []
for i in range(10):
    temp.append(str(random.randint(0,1)))
print(" ".join(temp))