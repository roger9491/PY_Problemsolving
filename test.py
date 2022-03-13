def sor(s):
    return (len(s),s,a)

m = ["12","12314","123123","123141"]
m = m[::-1]
print(m)
print(sorted(m, key = sor))

