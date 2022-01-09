import random

a = []
b = []

for i in range(7):
    a.append(random.randint(1,300))
    b.append(random.randint(40,100))
a.sort()







def t1(n, field, felll, tall):

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
    return [count,maxx]        

def t2(n, l, c, h):
    '''
    10 30 50
    11 15 5
    '''
    stack = []
    c = [0] + c
    c.append(l)
    h = [0] + h + [0]
    start = 0
    end = c[1]
    ans = 0
    max_h = 0
    for i in range(1,n):
        # print(i,start,ans,stack)

        if c[i] - h[i] >= start:
            ans += 1
            max_h = max(max_h,h[i])
        elif c[i] + h[i] <= c[i+1]:
            ans += 1
            max_h = max(max_h,h[i])
        else:
            # print(i)
            start = c[i]
            stack.append(i)
        while stack:
            if c[stack[-1]] - h[stack[-1]] >= start:
                ans += 1
                max_h = max(max_h,h[stack[-1]])
                del stack[-1]
            elif c[stack[-1]] + h[stack[-1]] <= c[i+1]:
                ans += 1
                max_h = max(max_h,h[stack[-1]])
                start = c[stack[-1]-1]
                del stack[-1]
            else:
                break
    # print(i,start,ans,stack,max_h)
    if c[n] - h[n] >= start:
        ans += 1
        max_h = max(max_h,h[n])
    elif c[n] + h[n] <= l:
        ans += 1
        max_h = max(max_h,h[n])


    return [ans,max_h]


if t2(7,a[-1],a,b) != t1(7,a[-1],a,b):
    print("錯誤")
    print(7,a[-1])
    print(" ".join(list(map(str,a))))
    print(" ".join(list(map(str,b))))