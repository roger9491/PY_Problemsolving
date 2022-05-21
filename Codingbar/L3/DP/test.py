n,k = map(int,input().split())
l = list(map(int,input().split()))
post = list(map(int,input().split()))
maxi = max(l)

i = 0
j = maxi

from copy import deepcopy as a

while i != j:
    now = (i + j)//2-1
    temp = []
    post1 = a(post)

    number = 0
    for k in range(len(l)):
        if l[k] >= now:
            number += 1
        elif l[k] < now:
            temp.append(number)
            number = 0
        if k == len(l) - 1:
            temp.append(number)
            number = 0

    while 1:
        if temp[0] - post1[0] > 0:
            temp[0] -= post1[0]
            del post1[0]
        elif temp[0] - post1[0] < 0:
            del temp[0]
        elif temp[0] == post1[0]:
            del temp[0]
            del post1[0]
        
        if not temp:
            flag = 1
            break
        if not post1:
            flag = 0
            break

    if flag == 1:
        j = now - 1
    else:
        i = now + 1

print(j)