N, M, K = map(int, input().split())
Q = []
for _ in range(N):
    Q.append(list(map(int, input().split())))
     
cost = [0 for _ in range(K)]
for k in range(K):
    c = list(map(int, input().split()))
    traffic = [[0 for i in range(M)] for j in range(M)]
    for i in range(N):
        for j in range(M):
            traffic[c[i]][j] += Q[i][j]
    print(traffic)
             
    for i in range(M):
        for j in range(M):
            if i == j:
                cost[k] += traffic[i][j]
            else:
                if traffic[i][j] <= 1000:
                    cost[k] += traffic[i][j] * 3
                else:
                    cost[k] += 1000 * 3
                    cost[k] += (traffic[i][j] - 1000) * 2
                     
print(min(cost))
            

            '''
            [0, 0, 0]
[[1450, 1220, 1700, 1590], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
18000
[0, 1, 2]
[[500, 400, 800, 200], [500, 400, 100, 600], [450, 420, 800, 790], [0, 0, 0, 0]]
14480
[0, 2, 2]
[[500, 400, 800, 200], [0, 0, 0, 0], [950, 820, 900, 1390], [0, 0, 0, 0]]
15860
[2, 1, 2]
[[0, 0, 0, 0], [500, 400, 100, 600], [950, 820, 1600, 990], [0, 0, 0, 0]]
13880
[1, 1, 1]
[[0, 0, 0, 0], [1450, 1220, 1700, 1590], [0, 0, 0, 0], [0, 0, 0, 0]]
            
            
            '''