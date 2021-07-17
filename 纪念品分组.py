size = int(input())
n = int(input())
temp = []
t = []
for i in range(n):
    s = int(input())
    t.append(s)
for i in t:
    if i <= size:
        temp.append(i)
temp.sort()

ans = []
while temp:
    if temp[0] + temp[-1] <= size:
        if len(temp) >= 2:
            ans.append(temp[0]+temp[-1])
            del temp[0]
            del temp[-1]
        else:
            ans.append(temp[-1])
            del temp[-1]
    else:
        ans.append(temp[-1])
        del temp[-1]
print(len(ans))