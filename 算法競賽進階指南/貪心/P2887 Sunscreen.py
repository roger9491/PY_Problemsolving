'''
https://www.luogu.com.cn/problem/P2887

貪婪選擇性


'''

c, l = map(int,input().split())

c_t = []
for i in range(c):
    a = list(map(int,input().split()))
    c_t.append(a[::-1])

l_t = []
for i in range(l):
    a = list(map(int,input().split()))
    l_t.append(a)
c_t.sort()
l_t.sort()
ans = 0
for i in range(c):
    for j in range(l):
        if c_t[i][1] <= l_t[j][0] <= c_t[i][0] and l_t[j][1] > 0:
            ans += 1
            l_t[j][1] -= 1
            break
print(ans)


# c, l = map(int,input().split())

# c_t = []
# for i in range(c):
#     a = list(map(int,input().split()))
#     c_t.append(a)

# l_t = []
# for i in range(l):
#     a = list(map(int,input().split()))
#     l_t.append(a)

# c_t.sort(reverse=True)
# l_t.sort(reverse=True)
# # print(l_t)
# count = 0
# index = 0
# for i in range(c):
#     flag = False
#     # print(index,l_t[index][1])
#     while (not (c_t[i][0] <= l_t[index][0] <= c_t[i][1])) or l_t[index][1] <= 0:
#         index += 1
#         if index >= l:
#             flag = True
#             break
#     if flag:
#         break
       
#     if l_t[index][1] > 0:
#         l_t[index][1] -= 1
#         count += 1

#     # print(c_t,count,index)
# print(count)