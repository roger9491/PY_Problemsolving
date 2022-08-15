"""
血緣關係
https://zerojudge.tw/ShowProblem?problemid=b967


8
0 1
0 2
0 3
7 0
1 4
1 5
3 6

"""
import traceback

def dfs(node):
    if node not in dic:
        return 

    max1 = 0
    max2 = 0
    c = 0
    for i in dic[node]:
        dfs(i)
        # print(i)
        if height[i] > max1:
            max2 = max1 
            max1 = height[i]
        elif height[i] > max2:
            max2 = height[i]
        c += 1

    max1 += 1
    if c >= 2:
        max2 += 1
    # print(max1,max2)
    parent[node] = max1 + max2 
    height[node] = max1

    # print(node)
    # print(height)
    # print(parent)


while True:
    try:
        n = int(input())
        
        dic = {}
        root = [0] * n

        for i in range(n-1):
            a,b = map(int,input().split())
            if a in dic:
                dic[a].append(b)
            else:
                dic[a] = [b]

            root[b] = 1
        for i in range(n):
            if root[i] == 0:
                root = i
                break

        height = [0]*n
        parent = [0]*n
        # print(root)
        dfs(root)
        print(max(parent))
    except:
        break