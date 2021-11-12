# n,m = map(int,input().split())

# matrix = []
# for i in range(n):
#     a = list(map(int,input().split()))
#     matrix.append(a)

# record = [[0]*m for i in range(n)]
# dir = [[1,0],[0,1],[-1,0],[0,-1]]

# minv = 10**9
# index = 0
# for i in range(n):
#     for j in range(m):
#         if minv > matrix[i][j]:
#             minv = matrix[i][j]
#             index = [i,j]
# ans = 0
# flag = True
# while True:
#     record[index[0]][index[1]] = 1
#     ans += matrix[index[0]][index[1]]
#     minv = 10**9
#     temp_index = 0
#     for x in dir:
#         now_x = index[0] + x[0]
#         now_y = index[1] + x[1]
#         if 0 <= now_x < n and 0 <= now_y < m: 
#             # print(now_x,now_y)
#             # print(record)
#             if record[now_x][now_y] == 0:
#                 if minv > matrix[now_x][now_y]:
#                     minv = matrix[now_x][now_y]
#                     temp_index = [now_x,now_y]
#     if temp_index == 0:
#         break
#     index = [temp_index[0],temp_index[1]]
# print(ans)



n,m=map(int,input().split())
mapp=[]
for i in range(n):
    mapp.append(list(map(int,input().split())))
copymap=[[0]*m for i in range(n)]
start=1000000
y=0
for i in mapp:
    x=0
    for k in i:
        if k<start:
            start=k
            startx=x
            starty=y
        x+=1
    y+=1
direction=[[1,0],[-1,0],[0,1],[0,-1]]
add=0
copymap[startx][starty]=1
while True:
    minnnn=1000000
    for i in direction:
        if m>startx+i[1]>=0 and n>starty+i[0]>=0:
            if mapp[starty+i[0]][startx+i[1]]<minnnn and copymap[starty+i[0]][startx+i[1]]==0:
                minnnn=mapp[starty+i[0]][startx+i[1]]
                minnnnx=startx+i[1]
                minnnny=starty+i[0]
    if minnnn==1000000:
        print(add)
        break
    add+=minnnn
    startx=minnnnx
    starty=minnnny
    # print(startx,starty)
    copymap[starty][startx]=1