# n,l = map(int,input().split())
# c = list(map(int,input().split()))
# h = list(map(int,input().split()))
# '''
# 10 30 50
# 11 15 5
# '''
# stack = []
# c = [0] + c
# c.append(l)
# h = [0] + h + [0]
# start = 0
# end = c[1]
# ans = 0
# max_h = 0
# for i in range(1,n):
#     # print(i,start,ans,stack)
#     if c[i] - h[i] >= start or c[i] + h[i] <= c[i+1]:
#         if c[i] - h[i] >= start:
#             ans += 1
#             max_h = max(max_h,h[i])
#         elif c[i] + h[i] <= c[i+1]:
#             ans += 1
#             max_h = max(max_h,h[i])
#         while stack:
#             if c[stack[-1]] - h[stack[-1]] >= start:
#                 ans += 1
#                 max_h = max(max_h,h[stack[-1]])
#                 del stack[-1]
#             elif c[stack[-1]] + h[stack[-1]] <= c[i+1]:
#                 ans += 1
#                 max_h = max(max_h,h[stack[-1]])
#                 start = c[stack[-1]-1]
#                 del stack[-1]
#             else:
#                 break
#     else:
#         # print(i)
#         start = c[i]
#         stack.append(i)
# # print(i,start,ans,stack,max_h)
# if c[n] - h[n] >= start:
#     ans += 1
#     max_h = max(max_h,h[n])
# elif c[n] + h[n] <= l:
#     ans += 1
#     max_h = max(max_h,h[n])



# print(ans)
# print(max_h)


# '''
# 7 196
# 21 38 77 113 118 141 196
# 41 63 90 74 95 55 98
# 1
# 55


# '''
'''
[3, 200] [21, 38, 47] [45, 29, 43]


'''

n,l = map(int,input().split())
c = list(map(int,input().split()))
h = list(map(int,input().split()))
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
    # print(i,start,ans,stack)
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
elif c[n] + h[n] <= l:
    ans += 1
    max_h = max(max_h,h[n])
    print(stack)
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



print(ans)
print(max_h)


'''
7 196
21 38 77 113 118 141 196
41 63 90 74 95 55 98
1
55


'''