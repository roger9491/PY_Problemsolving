a=list(map(int,input().split()))
c=[]
w=0
d=[]
k=0
r=0
for i in range(1,a[0]+1,1):
    c.append(i)   
w=[c]*a[0]
print(w)
while r<a[1]:
    r=r+1
    b=list(map(int,input().split()))
    for i in range(len(w)):
        z=i+1
        e=w[i]
        for j in e:
            if j==b[1] and z==b[0]:
                continue
            else:
               g=((z-b[0])**2+(j-b[1])**2)**0.5 #算出距離是否等於半徑
               if int(g)<=a[2]: #是的話探測到一個
                   k=k+1
print(k)