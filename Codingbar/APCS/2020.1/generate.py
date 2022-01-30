import random   #隨機

print(5,5)
record = []
for i in range(5):
    a = []
    for j in range(5):
        n = random.randint(1,40)
        while n in record:
            n = random.randint(1,40)
        a.append(str(n))
        record.append(n)
    print(" ".join(a))

