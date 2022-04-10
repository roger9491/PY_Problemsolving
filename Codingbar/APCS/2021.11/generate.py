from random import random


import random
n,m = 7, 3

p,k = 2,3
print(n,m)
t = []
for i in range(m):
    a = random.randint(0,n-1)
    b = random.randint(0,n-1)
    while a == b:
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
    t.append(str(a))
    t.append(str(b))
print(" ".join(t))
print(p,k)
for i in range(p):
    t = []
    for j in range(k):
        a = random.randint(0,n-1)
        b = random.randint(0,n-1)
        while a == b:
            a = random.randint(0,n-1)
            b = random.randint(0,n-1)
        t.append(str(a))
        t.append(str(b))
    print(" ".join(t))

'''
7 3
5 1 2 4 5 2
2 3
1 6 4 6 6 4
1 3 4 1 1 6

'''