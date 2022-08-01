'''
c++ L1
動態規劃 02

'''

def dfs(n):
    if n == 0:
        return 1

    total = 0
    for i in range(k):
        if n - i - 1 >= 0:
            total += dfs(n-i-1)
    return total


n, k = map(int,input().split())

print(dfs(n))