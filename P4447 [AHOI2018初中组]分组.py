n = int(input())
e = list(map(int,input().split()))
e.sort()
ans = []
while e:
    temp = []
    c = []
    for i in e:
        if not temp:
            temp.append(i)
            c.append(i)
        else:
            if i != temp[-1]:
                if i - temp[-1] == 1:
                    c.append(i)
                    temp.append(i)
                else:
                    break
    
    for i in c:
        del e[e.index(i)]
    ans.append(temp)

for i in range(len(ans)):
    for j in range(len(ans)):
        if i != j:
            if ans[j][0] - ans[i][0] == 1:
                ans[j].append(ans[i][0])
                del ans[i][0]
    
                temp = ans[j]
                del ans[i]
                del ans[ans.index(temp)]
                flag = True
                break
            elif ans[i][-1] - ans[j][-1] == 1:
                ans[j].append(ans[i][-1])
                del ans[i][-1]
                ans2.append(ans[i])
                ans2.append(ans[j])
                temp = ans[j]
                del ans[i]
                del ans[ans.index(temp)]
                flag = True
                break

        

minv = 10**9
for i in ans2:
    if len(i) < minv:
        minv = len(i)

print(minv)
