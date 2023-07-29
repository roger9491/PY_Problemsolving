""" 
實作split

"""

""" 
字元版

ex 
    a = "5o4o1o2o"
    s = "o"

    c = ["5", "4", "1", "2", ""]
"""
a = "5oooooo4ooo1o2o"
s = "ooo"
c = []
tmp = ""
for i in range(len(a)):
    print(a[i], s)
    if a[i] != s:
        print("213124")
        tmp += a[i]
    else:
        print("1", i)
        c.append(tmp)
        tmp = ""
if a[len(a) - 1] == s:
    c.append("")
print(c)