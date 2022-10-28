'''
j124: 3. 石窟探險
https://zerojudge.tw/ShowProblem?problemid=j124


2 6 0 8 14 0 0 0 10 0 4 0 0 

26


5 2 10 0 0 0 8 0 0 17 0 0 0

26

'''

def dfs(index, i):
    # print(index, i)
    global  ans
    
    if i == len(a) or a[i] == 0:
        return i

    if i != 0:
        ans += abs(a[index] - a[i])
    

    index = i
    if a[index] % 2 == 0:
        i = dfs(index, index + 1)
        i = dfs(index, i + 1)
    else:
        i = dfs(index, index + 1)
        i = dfs(index, i + 1)
        i = dfs(index, i + 1)

    return i




a = list(map(int,input().split()))
ans = 0 
dfs(0, 0)
print(ans)