# m,n,h=map(int,input().split())
# l=[[0]*n for i in range(m)]
# left=0
# for i in range(h):
#     r,c,t=map(int,input().split())
#     if t==0:
#         if left==0:
#             l[r][c]='+'
#             left=1
#         else:
#             l[r][c]='+'
#             left+=1#因找到最近木樁而停止
#             flag=1
#             temp=4
#             while flag and temp:
#                 temp=4#因超範圍停止
#                 f=1
#                 ds=[[1*f,0],[-1*f,0],[0,1*f],[0,-1*f]]
#                 for d in range(len(ds)):
#                     if 0<=r<ds[d][0] and 0<=c<ds[d][1]:
#                         if l[ds[d][0]][ds[d][1]]=='+':
#                             flag=0
#                             if d==0:
#                                 for j in range(1,1*f):
#                                     l[r+j][c]="-"
#                             elif d==1:
#                                 for j in range(-1,-1*f,-1):
#                                     l[r+j][c]="-"
#                             elif d==2:
#                                 for j in range(1,1*f):
#                                     l[r][c+j]="-"
#                             else:
#                                 for j in range(-1,-1*f,-1):
#                                     l[r][c+j]="-"
#                     else:
#                         temp-=1
#             f+=1
#             print(f)    
#         print(l)

n,m=map(int,input().split())
S=list(map(int,input().split()))
T=list(map(int,input().split()))
idx=list(map(int,input().split()))
l=[]
for i in range(n): 
    l.append([idx[i],i,S[i],T[i],0])
l.sort()
temp=[]
while len(l)!=1:
    for i in range(1,len(l),2):
        a,b,c,d=l[i-1][2],l[i-1][3],l[i][2],l[i][3]
        if a*b>=c*d:
            l[i-1][2]+=c*d//(2*b)
            l[i-1][3]+=c*d//(2*a)
            l[i][2]+=c//2
            l[i][3]+=d//2
            l[i][4]+=1
            if l[i][4]==m:
                temp.append(i)
                print(-1)
        else:
            l[i][2]+=a*b//(2*d)
            l[i][3]+=a*b//(2*c)
            l[i-1][2]+=a//2
            l[i-1][3]+=b//2
            l[i-1][4]+=1
            if l[i-1][4]==m:
                temp.append(i)
                print(-1)
    temp.sort()
    print("temp: ",temp)
    print(l)
    for i in range(len(temp)):
        print(len(l),m)
        '''
        直接刪除串列會使順序會亂掉
        '''
        del l[temp[i]-i]
    print("l",l)
    input()
    temp=[]
else:
    print(l[0][1])
