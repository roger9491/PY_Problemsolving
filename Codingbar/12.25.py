n,m,k = map(int, input().split())
L = [] #魔王路徑
P=0
LL=[[0]*(n) for _ in range(m)] #棋盤
for i in range(k):
    r,c,s,t=map(int,input().split())
    L.append([r,c,s,t])
# print(L)
# print(L,"L")
# for i in range(k):
#     print(i)
while P!=k:
    #print(P,k)
    #print(m,"M")
    for K in range(k):  #移動前的位置放炸彈
        if L[K] != "pass":
            # print(LL[L[K][1]][L[K][0]])
            LL[L[K][1]][L[K][0]]+=1 #L[c][r]
    for i in range(k):
        if L[i] != "pass":
            A=int(L[i][1]+L[i][3])  #c
            B=int(L[i][0]+L[i][2])  #r
            if A<0 or A>=int(m):
                L[i]="pass"
                P=P+1
            elif B<0 or B>=n:
                L[i]="pass"
                P=P+1
            elif LL[L[i][1]+L[i][3]][L[i][0]+L[i][2]]>=1:
                LL[L[i][1]+L[i][3]][L[i][0]+L[i][2]]+=100000
                L[i]="pass"
                P=P+1
            else:
                L[i][1]+=L[i][3]
                L[i][0]+=L[i][2]
    for i in range(m):
        for j in range(n):
            if LL[i][j]>=10000:
                LL[i][j]=0

T=0

for i in range(m):
    for j in range(n):
        if LL[i][j]!=0:
            T+=1
print(T)



'''
帳戶
    原本金錢    在一開始輸入
    存款    


'''