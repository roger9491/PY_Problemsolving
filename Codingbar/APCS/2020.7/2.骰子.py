'''
https://zerojudge.tw/ShowProblem?problemid=f580

b = -1
5,1,2,6,3,4 => 5,3,2,6,4,1
n[1],n[3],n[4],n[5] = n[4],n[5],n[3],n[1]

b = -2
5,1,2,6,3,4 => 6,5,1,2,3,4
n[0],n[1],n[2],n[3] = n[3],n[0],n[1],n[2]

'''

# n,m = map(int,input().split())

# t = [["5","1","2","6","3","4"] for i in range(n)]

# # print(t)
# for i in range(m):
#     a,b = map(int,input().split())
    
#     if a > 0 and b > 0:
#         t[a-1],t[b-1] = t[b-1],t[a-1]
#     elif b == -1:
#         t[a-1][1],t[a-1][3],t[a-1][4],t[a-1][5] = t[a-1][4],t[a-1][5],t[a-1][3],t[a-1][1]
#     else:
#         t[a-1][0],t[a-1][1],t[a-1][2],t[a-1][3] = t[a-1][3],t[a-1][0],t[a-1][1],t[a-1][2]
#     # print(t)
# ans = []
# for i in range(n):
#     ans.append(t[i][1])
# print(" ".join(ans))
l=list(map(int,input().split()))
bean=[["5","1","2","6","3","4"] for i in range(l[0])]
print(bean)
for i in range(l[1]):
    n=list(map(int,input().split()))
    
    if n[1]>0:
        bean[n[0]-1],bean[n[1]-1]=bean[n[1]-1],bean[n[0]-1]
        
    elif n[1]==-1:
        bean_=bean[n[0]-1].copy()
        bean[n[0]-1][1]=bean_[4]
        bean[n[0]-1][3]=bean_[5]
        bean[n[0]-1][4]=bean_[3]
        bean[n[0]-1][5]=bean_[1]
        
    elif n[1]==-2:
        bean_=bean[n[0]-1].copy()
        bean[n[0]-1][0]=bean_[3]
        bean[n[0]-1][1]=bean_[0]
        bean[n[0]-1][2]=bean_[1]
        bean[n[0]-1][3]=bean_[2]
        
ans=[]
for i in range(l[0]):
    ans.append(bean[i][1])
print(" ".join(ans))