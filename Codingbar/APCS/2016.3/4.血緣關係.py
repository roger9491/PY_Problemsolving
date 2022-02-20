def dfs(i,j):
    if matrix[i][j] != -1


while True:
    # try:
        n = int(input())
        
        dic = {}
        root = [0] * n
        matrix = [[-1]*n for i in range(n)]
        leaves = []
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
        for i in range(n):
            if i not in dic:
                leaves.append(i)
        leaves.append(root)
        print("pair")
        ans = 0
        for i in range(len(leaves)):
            for j in range(i+1,len(leaves)):
                dfs(leaves[i],leaves[j])
                ans = max(ans, matrix[leaves[i]][leaves[j]])
        print(ans)

    # except:
    #     break