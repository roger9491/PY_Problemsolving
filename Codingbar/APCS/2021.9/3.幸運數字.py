# from turtle import right


# n = int(input())
# a = list(map(int,input().split()))

# tree_list = [0]*(2**(int(n**(1/2)+1)-1))
# def fmin(i,j):
#     # print(i,j)
#     if i == j:
#         return i
#     else:
#         left = fmin(i,(i+j)//2)
#         right = fmin((i+j)//2+1,j)
#         # print("ans",left,right)
#         if a[left] > a[right]:
#             return right
#         else:
#             return left


# pre = [0]
# sum = 0
# for i in range(n):
#     sum += a[i]
#     pre.append(sum)

# l = 0
# r = n - 1

# while l <= r:
#     if l == r:
#         print(a[l])
#         break
#     else:
        
#         m = fmin(l,r)
#         # print(l,r,m)
#         if pre[m] - pre[l] > pre[r+1] - pre[m+1]:
#             r = m - 1
#         else:
#             l = m + 1
#     # print(l,r、；)



n = int(input())
a = list(map(int,input().split()))

p = [0]
minlist = []
for i in range(n):
    p.append(p[i]+a[i])
    minlist.append((a[i],i))
    
minlist.sort(reverse=True)

def fmin(i,j):
 while True:
  data,index = minlist.pop()
  if i <= index <= j:
   return index

def fsum(i,j):
    return p[j+1]-p[i]

l,r = 0,n-1
while l < r:
    m = fmin(l,r)
    lefts = fsum(l,m-1)
    rights = fsum(m+1,r)
    if lefts > rights: r = m-1
    else: l = m+1

print(a[l])
