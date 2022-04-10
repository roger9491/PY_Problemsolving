'''


A~Z 65~90
a~l 97~108

'''

m, n = map(int,input().split())

dic = {}

for i in range(n):
    s = input()

    target = 0
    temp = {}
    for i in s:
        i = ord(i)

        if i not in temp:
            if 65 <= i <= 90:
                target += 2**(i - 65)
            else:
                target += 1**(2*(i - 71))
            # print(i,target)
            temp[i] = 1
    if target in dic:
        dic[target] += 1
    else:
        dic[target] = 1

S = 2**m - 1
ans = 0
# print(dic)
for i in dic:
    com = i^S
    if com in dic:
        a = dic[com]
        b = dic[i]
        dic[com] -= min(a, b)
        dic[i] -= min(a, b)
        ans += min(a, b)        
print(ans)