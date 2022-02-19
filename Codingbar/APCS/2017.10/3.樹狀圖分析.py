'''
9 
1 6 
3 5 3 8 
0 
2 1 7 
1 9 
0 
1 2 
0 
0 

'''
# import sys
# sys.setrecursionlimit(100001)  
# def dfs(node):
#     if node not in dic:
#         return
#     # print(node)
#     temp = 0
#     for i in dic[node]:
#         dfs(i)
#         temp = max(temp, height[i])

#     height[node] = temp + 1
#     # print(node,height)

# n = int(input())

# height = [0]*(n + 1)

# dic = {}
# child = [0] * (n+1)
# for i in range(n):
#     a = list(map(int,input().split()))

#     if a[0] == 0:
#         pass
#     else:
#         dic[i+1] = a[1:]
#         for j in range(a[0]):
#             child[a[1+j]] = 1
# # print(dic)
# for i in range(n+1):
#     if child[i] == 0:
#         root = i
# print(root)


# dfs(root)
# print(sum(height))

'''
需要有 函數運算的 stack版基礎 以及一點樹的概念
'''

def dfs(node):
    stack = [node]
    stack_back = []
    while stack:
        node = stack.pop()
        if node not in dic:
            height[stack_back[-1]] = max(height[stack_back[-1]], height[node] + 1)
            if not stack or dic_parent[node] != dic_parent[stack[-1]]:
                temp = 0
                for i in dic[stack_back[-1]]:
                    temp = max(temp, height[i])
                height[stack_back[-1]] = temp + 1
                del stack_back[-1]
            continue
        stack_back.append(node)
        for i in dic[node][::-1]:
            stack.append(i)

    while stack_back:
        temp = 0
        for i in dic[stack_back[-1]]:
            temp = max(temp, height[i])
        height[stack_back[-1]] = temp + 1
        del stack_back[-1]


n = int(input())

height = [0]*(n + 1)

dic = {}
dic_parent = {}
child = [0] * (n+1)
for i in range(n):
    a = list(map(int,input().split()))

    if a[0] == 0:
        pass
    else:
        dic[i+1] = a[1:]
        for j in range(a[0]):
            child[a[1+j]] = 1
            if a[1+j] not in dic_parent:
                dic_parent[a[1+j]] = i + 1
for i in range(n+1):
    if child[i] == 0:
        root = i
print(root)
dfs(root)
print(sum(height))