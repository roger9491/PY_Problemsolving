m,n,h=map(int,input().split())
l=[[0]*n for i in range(m)]
left=0
for i in range(h):
    r,c,t=map(int,input().split())
    if t==0:
        if left==0:
            l[r][c]='+'
            left=1
        else:
            l[r][c]='+'
            left+=1#因找到最近木樁而停止
            flag=1
            temp=4
            while flag and temp:
                temp=4#因超範圍停止
                f=1
                ds=[[1*f,0],[-1*f,0],[0,1*f],[0,-1*f]]
                for d in range(len(ds)):
                    if 0<=r<ds[d][0] and 0<=c<ds[d][1]:
                        if l[ds[d][0]][ds[d][1]]=='+':
                            flag=0
                            if d==0:
                                for j in range(1,1*f):
                                    l[r+j][c]="-"
                            elif d==1:
                                for j in range(-1,-1*f,-1):
                                    l[r+j][c]="-"
                            elif d==2:
                                for j in range(1,1*f):
                                    l[r][c+j]="-"
                            else:
                                for j in range(-1,-1*f,-1):
                                    l[r][c+j]="-"
                    else:
                        temp-=1
            f+=1
            print(f)    
        print(l)
    # elif t==1:
    #     l[r][c]=0
    #     for j in range(1,1*F):

'''






'''