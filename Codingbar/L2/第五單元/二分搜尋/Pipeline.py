n, k = map(int,input().split())


while True:
    try:
        #..code...

    except:
        break


a=input().split()
a=list(map(int,a)) #寶藏地點數=a[0]、道路數=a[1]
b=input().split()
b=list(map(int,b)) #寶藏價值
L=[] #移動路徑

R=[["x"]*a[0] for i in range(a[0])]
for i in range(a[0]):
    R[i][i]=i
for i in range(a[1]): #移動路徑
    c=input().split()
    c=list(map(int,c))
    R[c[0]][c[1]]=c[1]

for i in range(len(R)):
    for j in range(len(R)):
        for k in range(i,len(R[0])):
            #print(i,"i")
            #print(R[j][k],"R[j][k]",R[i],"R[i]")
            if i in R[j] and R[j][k]!="x":
                R[i][k]=R[j][k]
T=0
LL=0
for i in range(len(R)):
    for j in range(len(R[0])):
        if R[i][j]!="x":
            T+=b[j]
    if T>LL:
        LL=T
    T=0