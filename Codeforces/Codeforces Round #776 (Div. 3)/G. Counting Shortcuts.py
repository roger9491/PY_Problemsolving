'''
https://codeforces.com/contest/1650/problem/G

6 8
6 1
1 4
1 6
1 5
1 2
5 6
4 6
6 3
2 6
'''
def bfs(node):
    queue = [node]
    count1 = 0
    ans = 0
    flag = False
    temp = []
    while queue:
        size = len(queue)
        while size != 0:
            node = queue.pop(0)
            # print("node",node)
            for i in dic[node]:
                if path[i] == 0:
                    if count1 == 1 and i in temp:
                        ans += 1
                    if i == end:
                        flag = True
                        temp.append(node)
                        ans += 1
                    else:
                        path[i] = 1
                    queue.append(i)
            size -= 1
        
        if flag:
            count1 += 1
            if count1 == 2:
                return ans%((10 ** 9) + 7)
            for i in temp:
                path[i] = 0


t = int(input())
for i in range(t):
    input().strip()
    n, m = map(int,input().split())

    dic = {}
    start, end = map(int,input().split())
    for i in range(m):
        a,b = map(int,input().split())
        if a in dic:
            dic[a].append(b)
        else:
            dic[a] = [b]
        if b in dic:
            dic[b].append(a)
        else:
            dic[b] = [a]
    path = [0]*(n+1) 
    path[start] = 1
    ans = bfs(start)
    print(ans)
