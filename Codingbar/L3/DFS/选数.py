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
    if num == 2:
        return True
    for i in range(2,int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True
def dfs(index):
    global ans
    # print(index, t, length)
    if len(t) == k:
        # print(t)
        if isprime(sum(t)):
            ans += 1
        return

    for i in range(index,length):
        t.append(a[i])
        dfs(i+1)
        del t[-1]



n, k =map(int,input().split())
a = sorted(list(map(int,input().split())))
length = len(a)
ans = 0
t = []
dfs(0)
print(ans)