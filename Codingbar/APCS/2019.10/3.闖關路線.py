'''
https://judge.tcirc.tw/ShowProblem?problemid=d094

5 3 1 2
0 3 2 3 5
    1
        2
2

10 8 2 3
0 5 2 3 4 5 6 6 8 9
3

'''


# def bfs(node):
#     queue = [node]
#     record[node] = 1
#     global ans
#     global flag
#     while queue:
#         size = len(queue)
#         while size != 0:
#             size -= 1
#             node = queue.pop(0)
#             # print(node)
#             for i in way:
#                 next_node = node + i
#                 if 0 <= next_node < n:
#                     if next_node == p:
#                         flag = True
#                         ans += 1
#                         return
#                     next_node = a[node + i]
#                     if 0 <= next_node < n and record[next_node] == 0:
#                         # print("next",next_node)
#                         if next_node == p:
#                             flag = True
#                             ans += 1
#                             return
#                         queue.append(next_node)
#                         record[next_node] = 1
#         ans += 1

def dfs(node):


n, p, l, r = map(int,input().split())

a = list(map(int,input().split()))

record = [0]*n
way = [-l, r]
flag = False
ans = 0
bfs(0)
if flag:
    print(ans)
else:
    print(-1)