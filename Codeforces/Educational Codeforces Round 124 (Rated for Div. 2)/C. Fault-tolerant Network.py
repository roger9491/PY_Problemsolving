'''
https://codeforces.com/contest/1651/problem/C
2
3
1 10 1
20 4 25
4
1 1 1 1
1000000000 1000000000 1000000000 1000000000

31
1999999998


a
b
(|is-a|+|it-a|)
(is+it)/2 - a

'''
def abst(a):
    if a < 0:
        return -a
    return a

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    targeta =(a[0] + a[-1]) 
    targetb = (b[0] + b[-1]) 
    
    temp = 10**9
    ansa = 10**9
    ansb = 10**9
    for i in range(1,n-1):
        if abst(a[i]*2 - targetb) < temp:
            temp = abst(a[i]*2 - targetb)
            ansa = a[i]
    temp = 10**9
    for i in range(1,n-1):
        if abst(b[i]*2 - targeta) < temp:
            temp = abst(b[i]*2 - targeta)
            ansb = b[i]
    temp1 = abst(a[0]-ansb) + abst(a[-1]-ansb) + abst(b[0]-ansa) + abst(b[-1]-ansa)
    temp2 = abst(a[0]-b[0]) + abst(a[-1]-b[-1])
    temp3 = abst(a[0]-b[-1]) + abst(b[0]-a[-1])
    temp4 = abst(a[-1]-b[0]) + abst(b[-1]-a[0]) 
    
    # print(temp1,temp2,temp3,temp4)
    print(min(temp1,temp2,temp3,temp4))
    
