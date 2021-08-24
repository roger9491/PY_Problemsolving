tem = list(map(int,input().split()))

record = [0]*len(tem)


ans = []


for i in range(1,len(tem)-1):
    if tem[i-1] < tem[i]:
        flag = 0
        temp = []
        for j in range(i,len(tem)):
            if tem[j] == tem[i]:
                temp.append(j+1)
            elif tem[j] < tem[i]:
                flag = 1 
                break
            else:
                break
        if flag:
            if len(temp) > 1:
                ans.append([temp[0],temp[-1],tem[i]])
            else:
                ans.append([temp[0],tem[i]])
if not ans:
    print(0,0)
else:
    for i in ans:
        print(" ".join(list(map(str,i))))