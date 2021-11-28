n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

list_a = a[1:]
list_b = b[1:]

count = 0
ans = 0
# print(list_a,list_b)
while count < 2**10:
    ans += 1
    count += 1
    if list_a[0] < list_b[0]:
        list_b.append(list_a[0])
        list_b.append(list_b[0])
        del list_a[0]
        del list_b[0]
    elif list_a[0] > list_b[0]:
        list_a.append(list_b[0])
        list_a.append(list_a[0])
        del list_a[0]
        del list_b[0]
    else:
        print(-1)
        break
    # print(list_a,list_b)
    if not list_a:
        print(ans,2)
        break
    elif not list_b:
        print(ans,1)
        break
else:
    print(-1)