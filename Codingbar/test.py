import sys
c = set("ab")
# t = [c]*5000000
t = []

# for i in range(5000000):
#     t.append(set("a"))
c = []
for i in range(50000):
    c.append(i)
s=sys.getsizeof(c)
print(s/1024000)