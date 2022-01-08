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
ans = 0 
for i in range(n):
    a = list(map(int,input().split()))
    ans += sum(a)

print(ans)
'''
10**9   次方

10 11 12
13 2  3
14 1  4

'''