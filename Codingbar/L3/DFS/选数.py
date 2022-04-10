'''
https://www.luogu.com.cn/problem/P1036
dfs



3 7 12 19
3 7 12
3 7 19
3 12 19
7 12 19


4 3
3 7 12 19

1
'''
def isprime(num):
    for i in range(2,num**(1/2)+1):
        if num % i == 0:
            return False
    return True
def dfs(t):


n, k =map(int,input().split())
a = sorted(list(map(int,input().split())))
length = len(a)
dfs(a)