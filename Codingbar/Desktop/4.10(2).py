from functools import cmp_to_key
def f(a,b):
    if int(a+b) < int(b+a):
        return -1   #交換 a 和 b
    else:
        return 1

n = int(input())

t = []
for i in range(n):
    num = input()
    t.append(num)

# for i in range(n):
#     for j in range(n-1-i):
#         if int(t[j]+t[j+1]) < int(t[j+1] + t[j]):
#             temp = t[j]
#             t[j] = t[j+1]
#             t[j+1] = temp
t.sort(reverse=True,key=cmp_to_key(f))

# 5 5111
# 5111 521
# 5215111
print("".join(t))