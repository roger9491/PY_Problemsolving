way = [(1,0),(0,1),(-1,0),(0,-1)]
def dfs(i,j):
    if i < 0 or i > n-1 or j < 0 or j > n-1 or m_r[i][j] == 1:
        return 
    m_r[i][j] = 1
    print(i,j)
    print(m_r[i][j])

    for x in way:
        dfs(i + x[0],j + x[1])
    m_r[i][j] = 0






n = int(input())
m = []
m_r = [[0]*n for i in range(n)]
for i in range(n):
    w = list(input())
    m.append(w)

dfs(0,0)
