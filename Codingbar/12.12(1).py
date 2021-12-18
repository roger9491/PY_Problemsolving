'''
week2 


'''


'''

e287: 機器人的路徑

'''
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
'''
1 有 1 的 or
1 不一樣的 and
1         xor
0 有 0  and
0 依樣的
0 都是 0 的


'''

# n = list(map(int,input().split()))
# a = n[0]
# b = n[1]
# c = n[2]
# d = False
# if (a and b) == c:
#     print("AND")
#     d = True
# if (a or b) == c:
#     print("OR")
#     d = True

# if c == 0:
#     if a == b :
#         print("XOR")
#         d = True
# elif c == 1:
#     if a != b:
#         print("XOR")
#         d = True

# if d == False:
#     print("IMPOSSIBLE")




# c=str()
# d={"0 1 0 1":"A","0 1 1 1":"B","0 0 1 0":"C","1 1 0 1":"D","1 0 0 0":"E","1 1 0 0":"F"}
# while True:
#     try:
#         a=int(input())
#         for i in range(a):
#             b=input() 
#             c=c+d[b]
#         print(c)
#     except:
#         break
'''
1    2      3 
2 3   3    


'''

a = input()
b = []
c = False
d = False
for i in a:
    b.append(i)
while True:
    if d == True:
        break
    for i in range(len(b)):
        if c == True:
            break
        for j in range(i+1,len(b)):
            if b[i] == b[j]:
                del b[j]
                c = True
                break
    else:
        d = True
    c = False
print(b)