
n = int(input())
x1,y1,x2,y2 = list(map(int,input().split(" ")))   #x1 y1 x2 y2

maxv = (1+n)*n-1
total = 0
if y1 >= y2:
    maxy = y1
    miny = y2
    maxx = x2 
    minx = x1 
else:
    maxy = y2 
    miny = y1 
    maxx = x1 
    minx = x2

length = n*2 + 1
if y1 > length:
    topy = length
else:
    topy = y1
if x1 > length:
    topx = length
else:
    topx = x1
if y2 > n:
    total = maxv + 1
    for i in range(n,y2):
        total = maxv + 2*i
elif y2 == n:
    total = maxv

elif y2 < n:


if maxy >= n and n > miny:
    total = maxv
    lenup = maxy - n
    lendown = n - miny 
    for i in range(lenup)
        total += maxv + (1+2*i)
    for i in range(lendown):
        total += maxv + (1+2*i)

    dele = 0
    for i in range(1,minx):
        

    for j in range(maxx+1,length+1):

    
    


elif y2 >= n:



elif y1 <= n:








for i in range(y2,topy+1):

    if i >= n:
        temp1 = i % n + 1  
    else:
        temp1 = n - i + 1
    if j >= n:
        temp2 = j % n + 1 
    else:
        temp2 = n - j + 1
    if temp1 >= temp2:
        ans = temp1
    else:
        ans = temp2
    total += ans

print(total)
