n,field=map(int,input().split())
felll=list(map(int,input().split()))
tall=list(map(int,input().split()))

felll.append(field)
fell=[]
for i in range(len(felll)):
    if i==0:
        fell.append(felll[0])
    else:
        fell.append(felll[i]-felll[i-1])

count=0
maxx=-111111111111
stackf=[fell[0]]
stackt=[]
for i in range(n):
    stackf.append(fell[i+1])
    stackt.append(tall[i])
    if tall[i]<=stackf[-2]:
        maxx=max(maxx,tall[i])
        count+=1
        del stackt[-1]
        stackf[-2]+=stackf[-1]
        del stackf[-1]
        
        while 1:
            if stackt:
                if stackt[-1]<=stackf[-1]:
                    maxx=max(maxx,stackt[-1])
                    count+=1
                    del stackt[-1]
                    stackf[-2]+=stackf[-1]
                    del stackf[-1]
                    
                else:
                    break
            else:
                break
    elif tall[i]<=stackf[-1]:
        maxx=max(maxx,tall[i])
        count+=1
        del stackt[-1]
        stackf[-2]+=stackf[-1]
        del stackf[-1]
        

print(count)
print(maxx)

'''
7 198 [52, 68, 106, 146, 157, 166, 198, 198] [65, 82, 96, 82, 84, 89, 51]

'''