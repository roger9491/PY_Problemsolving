s = input()

flag = False
ans = ""
num = ""
for i in range(len(s)):
    if s[i] in "0123456789":
        flag = True
        num += s[i]
    else:
        if flag:
            ans += s[i]*int(num)
            num = ""
            flag = False
        else:
            ans += s[i]

print(ans)