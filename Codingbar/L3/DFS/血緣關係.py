while True:
    try:
        def dfs(start):
            global depth
            global ans 
            # print(start)
            if t[start] == 0:
                return

            for i in t[start]:   #i 為孩子
                if record[i] == 0:
                    record[i] = 1
                    depth += 1
                    dfs(i)
                    record[i] = 0
                    ans = max(ans,depth)
                    depth -= 1


        n = int(input())
        
        t = [0]*n
        for i in range(n-1):
            a,b = map(int,input().split())
            if t[a] == 0 :
                t[a] = [b]
            else:
                t[a].append(b)
            
            if t[b] == 0:
                t[b] = [a]
            else:
                t[b].append(a)
        ans = 0
        depth = 0
        # print(t)
        for i in range(n):
            # print(t,i,n)
            if t[i] != 0:
                record = [0]*n
                record[i] = 1
                dfs(i)
        print(ans)
        
    except:
        break