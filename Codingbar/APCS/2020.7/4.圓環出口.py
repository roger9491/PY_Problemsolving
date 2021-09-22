'''
7 3
2 1 5 4 3 5 3
8 2 1 5 
9 4 3 5
12 3 2 1 5 4

4

4 3
1 3 5 7
4 1 3
1 4 8 12
4 1

'''
n,m = map(int,input().split())
p = list(map(int,input().split()))
t = list(map(int,input().split()))

sum_pre = []
c = 0
for i in range(n):
    c += p[i]
    sum_pre.append(c)

now = 0
for x in t:
    if now == 0:
        for j in range(n):
            if sum_pre[j] >= x:
                now = (j + 1) % n
                break
    else:
        target = x + sum_pre[(now-1)%n]
        if target > sum_pre[-1]:
            target -= sum_pre[-1]
            now = 0
        i = now
        j = n-1
        while i <= j:
            mid = (i+j) // 2
            if sum_pre[mid] == target:
                now = mid + 1
                break
            elif sum_pre[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        else:
            now = i + 1
        now %= n
print(now)







# n,m = map(int,input().split())
# p = list(map(int,input().split()))
# t = list(map(int,input().split()))


# now = 0
# for i in range(m):
    
#     c = p[now]
#     while c < t[i]:
#         now = (now + 1) % n
#         c += p[now]
#     now = (now + 1) % n
   
# print(now%n)

