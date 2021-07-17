t = int(input())
for i in range(t):
    s = input()
    t = [-1]*4
    t_max = [-1]*4

    for i in range(len(s)):
        if t[1] == -1 or t[2] == -1 or t[3] == -1:
            t[int(s[i])] = i
            t_max[int(s[i])] = i
        else:
            t_max[int(s[i])] = i 
            temp2 = t[:]
            temp3 = t_max[:]
            temp3.sort()
            temp2.sort()    
            if temp3[-1] - temp3[1] < temp2[-1] - temp2[1]:
                t = temp3[:]
    

    if t[1] == -1 or t[2] == -1 or t[3] == -1:
        print(0)
    else:
        t.sort()
        print(t[-1]-t[1]+1)