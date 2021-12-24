# with open("P.txt", "r") as f:
#     lines = f.readlines()
 

# def dfs(n):
#     # print("n",n)
#     global temp
#     temp += a[n]
#     # print("t",temp)
#     for way in t:
#         if way[0] == n:
#             if record[way[1]] == 0:
#                 record[way[1]] = 1
#                 dfs(way[1])
# while True:
#     try:
#         idx = 0
#         n, m = map(int,lines[idx].split())
#         idx += 1
#         a = list(map(int,lines[idx].split()))

#         t = []
#         idx += 1
#         for i in range(m):
#             b = list(map(int,lines[idx+i].split()))
#             t.append([b[0],b[1]])
#             t.append([b[1],b[0]])

#         record = [0]*n
#         ans = 0
#         for i in range(n):
#             if record[i] == 0:
#                 # print("i",i)
#                 temp = 0
#                 record[i] = 1
#                 dfs(i)
#                 ans = max(ans,temp)

#         print(ans)
#     except:
#         break





n,m,k = map(int, input().split())
L = [] #魔王路徑
P=0
LL=[[0]*(n) for _ in range(m)] #棋盤
for i in range(k):
    r,c,s,t=map(int,input().split())
    if r<0 or c<0:
        P=P+1
        L.append("pass")
    elif r>=n or c>=m:
        P=P+1
        L.append("pass")
    else:
        L.append([r,c,s,t])

# print(L,"L")
# for i in range(k):
#     print(i)
while P!=k:
    #print(P,k)
    #print(m,"M")
    for K in range(k):
        if L[K]=="pass":
            pass
        elif L[K]!="pass":
            LL[L[K][1]][L[K][0]]+=1 #L[c][r]
    for i in range(k):
        print(L[i][1]+L[i][3])
        A=int(L[i][1]+L[i][3])
        B=int(L[i][0]+L[i][2])
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
7 6
5 2 4 2 1 1 8
5 1
1 3
1 4
2 0
2 0
3 3


'''